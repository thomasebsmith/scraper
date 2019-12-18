# Scraper
##### Easy-to-use Python script/library for scraping webpages

## Quick Start
```sh
$ git clone https://github.com/thomasebsmith/scraper.git
$ cd scraper
$ python3 __main__.py <scraping spec file>
```

## Scraping Spec File Format
Please note that this format is not yet implemented. See `__main__.py` for the
currently-supported format.

```json
{
  "url": "<URL to scrape>",
  "elements": [
    {
      "key": "<key for results dictionary>",
      "scrape": "html"|"text"|"text_nodes"|{
        "attribute": "<attribute>"
      },
      "selector": "<CSS selector>"
    },
    ...
  ],
  "scrape_all": true|false
}
```
Note that `elements` need not be present if `scrape_all` is true.

## System Requirements
Scraper requires:
- `python3`
- The Python `requests` library
- The Python `Beautiful Soup` library
