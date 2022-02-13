from html.parser import HTMLParser
from typing import NamedTuple


class HTMLAttribute(NamedTuple):
    attribute: str
    value: str


class MyHTMLParser(HTMLParser):

    def __init__(self, data=None):
        super().__init__()
        self.document_tree = []
        self.current_node = []

        if data:
            self.feed(data)

    def __str__(self) -> str:
        if self.current_node:
            self.document_tree.append(self.current_node)
            self.current_node = []
        return f"{self.document_tree}"

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, MyHTMLParser):
            return str(self) == str(other)
        return False

    def build_attr_set(self, attrs) -> list:
        return_value = []  # set()

        for attr in attrs:
            # first attribute definition wins
            if attr[0] not in [x for x, y in return_value]:
                return_value.append(self.build_attr(attr))
        return sorted(return_value)

    @staticmethod
    def build_attr(attr) -> HTMLAttribute:

        match len(attr):
            case 2:
                return HTMLAttribute(attribute=attr[0], value=attr[1])
            case 1:
                return HTMLAttribute(attribute=attr[0], value="")
            case _:
                raise ValueError(f"{attr} is not an HTML attribute")

    def handle_starttag(self, tag, attrs):
        self.current_node.append((tag, self.build_attr_set(attrs)))

    def handle_endtag(self, tag):
        if self.current_node:
            self.document_tree.append(self.current_node)
            self.current_node = []

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.document_tree.append((tag, self.build_attr_set(attrs)))


def tags_equal(left: str = None, right: str = None) -> bool:
    if not (left and right):
        raise ValueError("Don't send me None!")

    left_parser = MyHTMLParser(left)
    right_parser = MyHTMLParser(right)

    return left_parser == right_parser


# Bonus 2
assert tags_equal("<OPTION NAME=hawaii selected selected SELECTED>", "<option selected selected name=hawaii>") is True

assert tags_equal("<p>", "<P>") is True
assert tags_equal("<b>", "<p>") is False
assert tags_equal("<img src=cats.jpg height=40>", "<IMG SRC=cats.jpg height=40>") is True
assert tags_equal("<img src=dogs.jpg width=99>", "<img src=dogs.jpg width=20>") is False

assert tags_equal("<img src=cats.jpg src=cats.jpg height=40>", "<IMG SRC=cats.jpg height=40>") is True
assert tags_equal("<img width=99 src=dogs.jpg>", "<img src=dogs.jpg width=20>") is False
assert tags_equal("<img width= 99  src=dogs.jpg>", "<img src=dogs.jpg width=20>  ") is False
assert tags_equal("<img src=cats.jpg height=40>", "<IMG SRC=cats.jpg height=40>") is True

# Bonus 1
assert tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_email>") is True
assert tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_username>") is False

# Bonus 3
assert tags_equal("<input value='hello there'>", '<input value="hello there">') is True
assert tags_equal("<input value=hello>", "<input value='hello'>") is True

assert tags_equal("<img type=checkbox checked>", "<Img type=checkbox>") is False
assert tags_equal("<input type=checkbox checked>", "<input type=checkbox CHECKED>") is True
assert tags_equal("<input type=checkbox checked>", "<input checked type=checkbox>") is True
