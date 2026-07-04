import pytest

from textkit.slugify import is_slug, slugify


def test_slugify_basic_text():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_collapses_repeated_separators():
    assert slugify("  multiple   spaces--and--dashes  ") == "multiple-spaces-and-dashes"


def test_slugify_strips_accents():
    assert slugify("Café Münchën") == "cafe-munchen"


def test_slugify_raises_when_nothing_sluggable():
    with pytest.raises(ValueError):
        slugify("!!!???")


def test_is_slug_valid():
    assert is_slug("hello-world") is True


def test_is_slug_rejects_uppercase():
    assert is_slug("Hello-World") is False


def test_is_slug_empty_string():
    assert is_slug("") is False
