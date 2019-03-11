#!/usr/bin/env python3

"""
"""

import sys
import json
import argparse

from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import Citation, CitationItem
from citeproc import formatter
from citeproc.source.json import CiteProcJSON
from citeproc_styles import get_style_filepath

import fatcat_client
from fatcat_client.rest import ApiException
from fatcat_client import ReleaseEntity, ContainerEntity, ChangelogEntry
from fatcat_tools import uuid2fcid, entity_from_json, entity_to_dict, \
    release_to_elasticsearch, container_to_elasticsearch, \
    changelog_to_elasticsearch, public_api, release_to_csl


def run_transform_releases(args):
    for line in args.json_input:
        line = line.strip()
        if not line:
            continue
        entity = entity_from_json(line, ReleaseEntity, api_client=args.api.api_client)
        args.json_output.write(
            json.dumps(release_to_elasticsearch(entity)) + '\n')

def run_transform_containers(args):
    for line in args.json_input:
        line = line.strip()
        if not line:
            continue
        entity = entity_from_json(line, ContainerEntity, api_client=args.api.api_client)
        args.json_output.write(
            json.dumps(container_to_elasticsearch(entity)) + '\n')

def run_transform_changelogs(args):
    for line in args.json_input:
        line = line.strip()
        if not line:
            continue
        entity = entity_from_json(line, ChangelogEntry, api_client=args.api.api_client)
        args.json_output.write(
            json.dumps(changelog_to_elasticsearch(entity)) + '\n')

def run_citeproc_releases(args):
    for line in args.json_input:
        line = line.strip()
        if not line:
            continue
        entity = entity_from_json(line, ReleaseEntity, api_client=args.api.api_client)
        csl_json = release_to_csl(entity)
        # XXX:
        csl_json['id'] = "release:" + (entity.ident or "unknown")
        if args.style == "csl-json":
            args.json_output.write(json.dumps(csl_json) + "\n")
            continue
        bib_src = CiteProcJSON([csl_json])
        form = formatter.plain
        if args.html:
            form = formatter.html
        style_path = get_style_filepath(args.style)
        bib_style = CitationStylesStyle(style_path, validate=False)
        bib = CitationStylesBibliography(bib_style, bib_src, form)
        bib.register(Citation([CitationItem(csl_json['id'])]))
        # XXX:
        #args.json_output.write(
        #    json.dumps(release_to_csl(entity)) + '\n')
        lines = bib.bibliography()[0]
        if args.style == "bibtex":
            for l in lines:
                if l.startswith(" @"):
                    args.json_output.write("\n@")
                elif l.startswith(" "):
                    #print("line: START|{}|END".format(l))
                    args.json_output.write("\n  " + l)
                else:
                    args.json_output.write(l)
        else:
            args.json_output.write(''.join(lines) + "\n")
        print()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug',
        action='store_true',
        help="enable debugging interface")
    parser.add_argument('--host-url',
        default="http://localhost:9411/v0",
        help="connect to this host/port")
    subparsers = parser.add_subparsers()

    sub_transform_releases = subparsers.add_parser('transform-releases')
    sub_transform_releases.set_defaults(func=run_transform_releases)
    sub_transform_releases.add_argument('json_input',
        help="JSON-per-line of release entities",
        default=sys.stdin, type=argparse.FileType('r'))
    sub_transform_releases.add_argument('json_output',
        help="where to send output",
        default=sys.stdout, type=argparse.FileType('w'))

    sub_transform_containers = subparsers.add_parser('transform-containers')
    sub_transform_containers.set_defaults(func=run_transform_containers)
    sub_transform_containers.add_argument('json_input',
        help="JSON-per-line of container entities",
        default=sys.stdin, type=argparse.FileType('r'))
    sub_transform_containers.add_argument('json_output',
        help="where to send output",
        default=sys.stdout, type=argparse.FileType('w'))

    sub_transform_changelogs = subparsers.add_parser('transform-changelogs')
    sub_transform_changelogs.set_defaults(func=run_transform_changelogs)
    sub_transform_changelogs.add_argument('json_input',
        help="JSON-per-line of changelog entries",
        default=sys.stdin, type=argparse.FileType('r'))
    sub_transform_changelogs.add_argument('json_output',
        help="where to send output",
        default=sys.stdout, type=argparse.FileType('w'))

    sub_citeproc_releases = subparsers.add_parser('citeproc-releases')
    sub_citeproc_releases.set_defaults(func=run_citeproc_releases)
    sub_citeproc_releases.add_argument('json_input',
        help="JSON-per-line of release entities",
        default=sys.stdin, type=argparse.FileType('r'))
    sub_citeproc_releases.add_argument('json_output',
        help="where to send output",
        default=sys.stdout, type=argparse.FileType('w'))
    sub_citeproc_releases.add_argument('--style',
        help="citation style to output",
        default='csl-json')
    sub_citeproc_releases.add_argument('--html',
        action='store_true',
        help="output HTML, not plain text")

    args = parser.parse_args()
    if not args.__dict__.get("func"):
        print("tell me what to do!")
        sys.exit(-1)

    args.api = public_api(args.host_url)
    args.func(args)

if __name__ == '__main__':
    main()
