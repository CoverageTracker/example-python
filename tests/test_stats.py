import pytest

from textkit.stats import most_common_word, tokenize, word_frequencies


def test_tokenize_lowercases_and_strips_punctuation():
    assert tokenize("Hello, World! It's great.") == ["hello", "world", "it's", "great"]


def test_word_frequencies_excludes_default_stopwords():
    text = "the cat and the dog and the cat"
    assert word_frequencies(text, top_n=2) == [("cat", 2), ("dog", 1)]


def test_word_frequencies_with_custom_stopwords():
    result = word_frequencies("red green red blue", stopwords={"red"})
    assert result == [("green", 1), ("blue", 1)]


def test_word_frequencies_returns_empty_when_all_stopwords():
    assert word_frequencies("the a an") == []


def test_word_frequencies_raises_on_non_positive_top_n():
    with pytest.raises(ValueError):
        word_frequencies("hello world", top_n=0)


def test_most_common_word_returns_top_word():
    assert most_common_word("dog dog cat") == "dog"


def test_most_common_word_returns_none_for_empty_result():
    assert most_common_word("the a an") is None
