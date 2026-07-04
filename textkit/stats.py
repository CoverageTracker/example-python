"""Simple word-frequency statistics for plain text."""

from __future__ import annotations

import re
from collections import Counter

DEFAULT_STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "is", "it",
    "on", "for", "with", "as", "this", "that",
}


def tokenize(text: str) -> list[str]:
    """Lowercase word tokens from `text`, stripped of punctuation."""
    return re.findall(r"[a-z']+", text.lower())


def word_frequencies(
    text: str,
    stopwords: set[str] | None = None,
    top_n: int = 10,
) -> list[tuple[str, int]]:
    """Return the `top_n` most common words in `text`, excluding stopwords."""
    if top_n <= 0:
        raise ValueError("top_n must be positive")

    active_stopwords = DEFAULT_STOPWORDS if stopwords is None else stopwords
    tokens = [t for t in tokenize(text) if t not in active_stopwords]

    if not tokens:
        return []

    counts = Counter(tokens)
    return counts.most_common(top_n)


def most_common_word(text: str, stopwords: set[str] | None = None) -> str | None:
    """Return the single most frequent non-stopword in `text`, or None."""
    frequencies = word_frequencies(text, stopwords=stopwords, top_n=1)
    if not frequencies:
        return None
    return frequencies[0][0]
