import requests


def get_text(url="http://www.gkc.org.uk/gkc/books/dickens_A_C_1.txt") -> str:
    return str(requests.get(url).content)
