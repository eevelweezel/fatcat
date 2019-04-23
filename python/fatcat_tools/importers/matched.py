
import sys
import json
import sqlite3
import itertools
import fatcat_client
from .common import EntityImporter, clean, make_rel_url


class MatchedImporter(EntityImporter):
    """
    Importer for "file to crossref DOI" matches.

    These matches are currently generated by Internet Archive hadoop jobs
    written in scala (part of the 'sandcrawler' repo/project), but could be
    generated by other parties as well.

    Input format is JSON with keys:
    - dois (list)
    - sha1 (hex)
    - md5 (hex)
    - sha256 (hex)
    - size (int)
    - cdx (list of objects)
        - dt (optional; if included creates wayback link)
        - url
    - mimetype
    - urls (list of strings... or objects?)

    Future handlings/extensions:
    - core_id, wikidata_id, pmcid, pmid: not as lists
    """

    def __init__(self, api, **kwargs):

        eg_desc = kwargs.pop('editgroup_description',
            "Import of large-scale file-to-release match results. Source of metadata varies.")
        eg_extra = kwargs.pop('editgroup_extra', dict())
        eg_extra['agent'] = eg_extra.get('agent', 'fatcat_tools.MatchedImporter')
        super().__init__(api,
            editgroup_description=eg_desc,
            editgroup_extra=eg_extra,
            **kwargs)
        self.default_link_rel = kwargs.get("default_link_rel", "web")
        self.default_mime = kwargs.get("default_mime", None)

    def want(self, raw_record):
        return True

    def parse_record(self, obj):
        dois = [d.lower() for d in obj.get('dois', [])]

        # lookup dois
        re_list = set()
        for doi in dois:
            try:
                re = self.api.lookup_release(doi=doi)
            except fatcat_client.rest.ApiException as err:
                if err.status != 404:
                    raise err
                re = None
            if re is None:
                #print("DOI not found: {}".format(doi))
                pass
            else:
                re_list.add(re.ident)
        release_ids = list(re_list)
        if len(release_ids) == 0:
            self.counts['skip-no-doi'] += 1
            return None

        # parse URLs and CDX
        urls = set()
        for url in obj.get('url', []):
            url = make_rel_url(url, default_link_rel=self.default_link_rel)
            if url != None:
                urls.add(url)
        for cdx in obj.get('cdx', []):
            original = cdx['url']
            if cdx.get('dt'):
                wayback = "https://web.archive.org/web/{}/{}".format(
                    cdx['dt'],
                    original)
                urls.add(("webarchive", wayback))
            url = make_rel_url(original, default_link_rel=self.default_link_rel)
            if url != None:
                urls.add(url)
        urls = [fatcat_client.FileEntityUrls(rel=rel, url=url) for (rel, url) in urls]
        if len(urls) == 0:
            self.counts['skip-no-urls'] += 1
            return None

        size = obj.get('size')
        if size:
            size = int(size)

        fe = fatcat_client.FileEntity(
            md5=obj.get('md5'),
            sha1=obj['sha1'],
            sha256=obj.get('sha256'),
            size=size,
            mimetype=obj.get('mimetype'),
            release_ids=release_ids,
            urls=urls,
        )
        return fe

    def try_update(self, fe):
        # lookup sha1, or create new entity
        existing = None
        try:
            existing = self.api.lookup_file(sha1=fe.sha1)
        except fatcat_client.rest.ApiException as err:
            if err.status != 404:
                raise err

        if not existing:
            return True

        fe.release_ids = list(set(fe.release_ids + existing.release_ids))
        if set(fe.release_ids) == set(existing.release_ids) and len(existing.urls) > 0:
            # no new release matches *and* there are already existing URLs
            self.counts['exists'] += 1
            return False

        # merge the existing into this one and update
        existing.urls = list(set([(u.rel, u.url) for u in fe.urls + existing.urls]))
        existing.urls = [fatcat_client.FileEntityUrls(rel=rel, url=url) for (rel, url) in existing.urls]
        existing.release_ids = list(set(fe.release_ids + existing.release_ids))
        existing.mimetype = existing.mimetype or fe.mimetype
        existing.size = existing.size or fe.size
        existing.md5 = existing.md5 or fe.md5
        existing.sha256 = existing.sha256 or fe.sha256
        self.api.update_file(existing.ident, existing, editgroup_id=self.get_editgroup_id())
        self.counts['update'] += 1
        return False

    def insert_batch(self, batch):
        self.api.create_file_batch(batch,
            autoaccept=True,
            description=self.editgroup_description,
            extra=json.dumps(self.editgroup_extra))

