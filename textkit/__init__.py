"""textkit — a small text-analysis toolkit.

Readability scoring, slug generation, and word-frequency statistics.
"""

from textkit.readability import flesch_kincaid_grade, grade_label
from textkit.slugify import is_slug, slugify
from textkit.stats import most_common_word, word_frequencies

__all__ = [
    "flesch_kincaid_grade",
    "grade_label",
    "is_slug",
    "slugify",
    "most_common_word",
    "word_frequencies",
]
