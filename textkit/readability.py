"""Flesch-Kincaid style readability scoring for plain text."""

from __future__ import annotations

import re


def count_syllables(word: str) -> int:
    """Rough heuristic syllable count for a single word."""
    word = word.lower().strip()
    if not word:
        return 0

    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)

    if word.endswith("e") and not word.endswith("le") and count > 1:
        count -= 1

    return max(count, 1)


def flesch_kincaid_grade(text: str) -> float:
    """Compute the Flesch-Kincaid grade level for `text`.

    Raises ValueError if the text has no scorable sentences or words.
    """
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    words = re.findall(r"[A-Za-z']+", text)

    if not sentences or not words:
        raise ValueError("text must contain at least one sentence and word")

    syllables = sum(count_syllables(w) for w in words)

    words_per_sentence = len(words) / len(sentences)
    syllables_per_word = syllables / len(words)

    grade = 0.39 * words_per_sentence + 11.8 * syllables_per_word - 15.59
    return round(grade, 2)


def grade_label(grade: float) -> str:
    """Map a numeric grade level to a human-readable band."""
    if grade < 0:
        return "Below grade level"
    if grade <= 5:
        return "Elementary school"
    if grade <= 8:
        return "Middle school"
    if grade <= 12:
        return "High school"
    if grade <= 16:
        return "College"
    return "Graduate"
