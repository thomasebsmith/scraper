# Scraper
##### Easy-to-use Python script/library for scraping webpages

## Quick Start
```sh
$ git clone https://github.com/thomasebsmith/scraper.git
$ cd scraper
$ python3 __main__.py <scraping spec file>
```

## Scraping Spec File Format
This format is fully implemented.

Main structure:
```js
{
  "url": "<URL to scrape>",
  *"elements": [
    <element>,
    ...
  ],
  *"headers": {
    "<header name 1>": "<header value 1>",
    ...
  },
  *"scrape_all": true|false,
  *"initial_regex": ["<find>", "<replace with>"]
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

Note that `elements` need not be present if `scrape_all` is `true`, and
`scrape_all` defaults to false.

Also, the User-Agent header defaults to
`Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36`
if one is not provided.

## System Requirements
Scraper requires:
- `python3`
- The Python `requests` library
- The Python `Beautiful Soup` library
  - The `SoupSieve` library (often installed with `Beautiful Soup`)
