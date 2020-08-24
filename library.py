import re

from bs4 import BeautifulSoup, element as bs4_element
import requests

class ScrapeSpecError(Exception):
  def __init__(self, message):
    super().__init__(message)

def __parse_as(value, type_string):
  converter = str
  if type_string == "int":
    converter = int
  elif type_string == "float":
    converted = float
  elif type_string == "bool":
    converter = bool
  try:
    return converter(value)
  except ValueError:
    return None

def __recursive_scrape(scrape, html):
  options = {}
  result = None

  if type(scrape) is dict:
    options = scrape
    scrape = scrape["type"]

  if scrape == "html":
    result = str(html)
  elif scrape == "text":
    result = html.get_text()
  elif scrape == "text_nodes":
    result = ""
    for child in html.children:
      if type(child) is bs4_element.NavigableString:
        result += child
  elif scrape == "attribute":
      result = html.attrs.get(options["attribute"])
  if result != None or type(scrape) != list:
    if "regex" in options:
      pattern = re.compile(options["regex"][0])
      result = pattern.sub(options["regex"][1], result)
    result = __parse_as(result, options.get("parse_as", "str"))
    return result

  # else: scrape should be an array of elements
  results = {}
  for el in scrape:
    to_scrape = el["scrape"]
    tags = html.select(el["selector"])
    if not el["select_all"] and len(tags) > 0:
      tag = tags[0]
      results[el["key"]] = __recursive_scrape(to_scrape, tag)
    elif not el["select_all"]:
      results[el["key"]] = None
    else:
      results[el["key"]] = [__recursive_scrape(to_scrape, tag) for tag in tags]
  return results


def scrape(given_spec):
  # Top-level spec defaults.
  spec = {
    "scrape_all": False
  };
  spec.update(given_spec);

  if "url" not in spec:
    raise ScrapeSpecError("No \"url\" parameter was provided for scraping.");
  url = spec["url"]

  should_scrape_all = spec["scrape_all"]

  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
  }
  if "headers" in spec:
    headers.update(spec["headers"])

  if not should_scrape_all and "elements" not in spec:
    raise ScrapeSpecError(
      "No \"elements\" parameter was provided for scraping."
    );

  req = requests.get(url, headers=headers)
  text = req.text
  if "initial_regex" in spec:
    pattern = re.compile(spec["initial_regex"][0])
    text = pattern.sub(spec["initial_regex"][1], text)

  if should_scrape_all:
    return text
  elements = spec["elements"]
  html = BeautifulSoup(text, "html.parser")
  if type(elements) != list:
    return None
  return __recursive_scrape(elements, html)
