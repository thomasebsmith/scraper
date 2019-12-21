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

Main structure:
```js
{
  "url": "<URL to scrape>",
  "elements": [
    <element>,
    ...
  ],
  "scrape_all": true|false
}
```

`element`:
```js
{
  "key": "<key for results dictionary>",
  "scrape": "html"|"text"|"text_nodes"|{
    "type": "html"|"text"|"text_nodes"|"attribute",
    *"attribute": "<attribute>",
    *"regex": ["<find>", "<replace with>"],
    *"parse_as": "str"|"int"|"float"|"bool"
  }|[
    <element>,
    ...
  ],
  "selector": "<CSS selector>",
  "select_all": true|false
}
```
`*` denotes a field that is not always required.

Note that `elements` need not be present if `scrape_all` is true.

## System Requirements
Scraper requires:
- `python3`
- The Python `requests` library
- The Python `Beautiful Soup` library
