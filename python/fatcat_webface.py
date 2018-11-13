#!/usr/bin/env python3

import argparse
from fatcat_webface import app

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug',
        action='store_true',
        help="enable debugging interface (note: not for everything)")
    parser.add_argument('--host',
        default="127.0.0.1",
        help="listen on this host/IP")
    parser.add_argument('--port',
        type=int,
        default=9810,
        help="listen on this port")
    args = parser.parse_args()

    app.run(debug=args.debug, host=args.host, port=args.port)

if __name__ == '__main__':
    main()
