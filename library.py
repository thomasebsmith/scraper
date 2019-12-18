from bs4 import BeautifulSoup
import requests

def scrape(spec):
  def recursive_scrape(scrape, html):
    if scrape == "html":
      return str(html)
    elif scrape == "text":
      return html.get_text()
    elif scrape == "text_nodes":
      # TODO
      return None
    elif type(scrape) is dict:
      return html.attrs.get(element["attribute"])
    # else: element should be an array of elements
    results = {}
    for el in scrape:
      to_scrape = el["scrape"]
      tags = html.select(el["selector"])
      if not el["select_all"] and len(tags) > 0:
        tag = tags[0]
        results[el["key"]] = recursive_scrape(to_scrape, tag)
      else:
        results[el["key"]] = [recursive_scrape(to_scrape, tag) for tag in tags]
    return results

  url = spec["url"]
  should_scrape_all = spec["scrape_all"]

  req = requests.get(url)
  if should_scrape_all:
    return req.text
  elements = spec["elements"]
  html = BeautifulSoup(req.text, "html.parser")
  if type(elements) != list:
    return None
  return recursive_scrape(elements, html)
