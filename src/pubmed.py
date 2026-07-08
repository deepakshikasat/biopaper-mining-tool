from __future__ import annotations
import time
import requests

def search_pubmed(query: str, retmax: int = 20) -> list[str]:
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": retmax}
    r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", params=params, timeout=30)
    r.raise_for_status()
    time.sleep(0.34)
    return r.json()["esearchresult"]["idlist"]
