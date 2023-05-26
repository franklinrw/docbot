import re

from bs4 import BeautifulSoup
from markdownify import markdownify as md

# def replace_multiple_newlines(string):
#     pattern = r"\n+"
#     replacement = "\n"
#     result = re.sub(pattern, replacement, string)
#     return result


def html_as_markdown(html: str):
    soup = BeautifulSoup(html, "html.parser")

    # Strip unnecessary data
    for data in soup(
        [
            "style",
            "script",
            "header",
            "footer",
            "img",
            "textarea",
        ]
    ):
        # Remove tags
        data.decompose()

    return md(soup.body.text)