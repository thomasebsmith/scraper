#!/usr/bin/env python3

import argparse
import json
import sys

import library

parser = argparse.ArgumentParser(
  description="Scrape the contents of an HTML page."
)
parser.add_argument(
  "scraping_spec_file",
  type=argparse.FileType("r"),
  nargs="?",
  default=sys.stdin,
  help="a JSON file containing information about what to scrape"
)
parser.add_argument(
  "--pretty-print",
  action="store_true",
  help="enable pretty-printing of JSON output"
)
args = parser.parse_args()
scraping_spec_file = args.scraping_spec_file
should_pretty_print = args.pretty_print

scraping_spec = json.load(scraping_spec_file)
scraping_spec_file.close()

"""
scraping_spec_file should be a JSON file in the format:
{
  "url": "<URL to scrape here>",
  "elements": [
    <element>,
    ...
  ],
  "headers": {
    "<header name>": "<header value>",
    ...
  },
  "scrape_all": <bool - whether to scrape entire page>
}
"""

result = library.scrape(scraping_spec)

if should_pretty_print:
  print(json.dumps(result, indent=4))
else:
  print(json.dumps(result))
