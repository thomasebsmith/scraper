from bs4 import BeautifulSoup
import requests

def scrape(spec):
  url = spec["url"]
  selectors = spec["selectors"]
  should_scrape_all = spec["all"]

  req = requests.get(url)
  results = req.text
  if not should_scrape_all:
    html = BeautifulSoup(req.text, "html.parser")
    results = []
    for selector in selectors:
      tags = html.select(selector)
      results.append([tag.get_text() for tag in tags])

  return {
    "results": results
  }
