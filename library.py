import re

from bs4 import BeautifulSoup
import requests

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
    # TODO
    result = None
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


def scrape(spec):
  url = spec["url"]
  should_scrape_all = spec["scrape_all"]

  req = requests.get(url)
  if should_scrape_all:
    return req.text
  elements = spec["elements"]
  html = BeautifulSoup(req.text, "html.parser")
  if type(elements) != list:
    return None
  return __recursive_scrape(elements, html)
