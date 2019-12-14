#!/usr/bin/env python3

import json
import sys

import library

if len(sys.argv) != 2:
  program_name = "scraper"
  if len(sys.argv) >= 1:
    program_name = sys.argv[0]
  print("Usage: ", program_name, " <scraping spec file>")
  sys.exit(1)

[_, scraping_spec_file] = sys.argv

scraping_spec_file = open(scraping_spec_file)
scraping_spec = json.load(scraping_spec_file)
scraping_spec_file.close()

"""
scraping_spec_file should be a JSON file in the format:
{
  "url": "<URL to scrape here>",
  "selectors": ["<CSS selector here>", ...],
  "all": <bool - whether to scrape entire page>
}
"""

result = library.scrape(scraping_spec)

print(json.dumps(result))
