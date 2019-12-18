from bs4 import BeautifulSoup
import requests

def scrape(spec):
  url = spec["url"]
  should_scrape_all = spec["scrape_all"]

  req = requests.get(url)
  results = req.text
  if not should_scrape_all:
    elements = spec["elements"]
    html = BeautifulSoup(req.text, "html.parser")
    results = {}
    for element in elements:
      to_scrape = element["scrape"]
      tags = html.select(element["selector"])
      result = None
      if to_scrape == "html":
        result = [str(tag) for tag in tags]
      elif to_scrape == "text":
        result = [tag.get_text() for tag in tags]
      # TODO: text_nodes
      else:
        # to_scrape is an attribute object
        result = [tag.attrs[to_scrape["attribute"]] for tag in tags]
      results[element["key"]] = result

  return results
