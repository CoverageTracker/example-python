import pytest

from textkit.readability import count_syllables, flesch_kincaid_grade, grade_label


def test_count_syllables_simple_word():
    assert count_syllables("cat") == 1


def test_count_syllables_silent_e_is_trimmed():
    assert count_syllables("bike") == 1


def test_count_syllables_le_ending_not_trimmed():
    assert count_syllables("apple") == 2


def test_count_syllables_blank_string():
    assert count_syllables("   ") == 0


def test_flesch_kincaid_grade_simple_text_scores_low():
    grade = flesch_kincaid_grade("The cat sat on the mat. It was happy.")
    assert grade < 5


def test_flesch_kincaid_grade_raises_on_empty_text():
    with pytest.raises(ValueError):
        flesch_kincaid_grade("   ...   ")


@pytest.mark.parametrize(
    "grade,expected",
    [
        (2, "Elementary school"),
        (7, "Middle school"),
        (10, "High school"),
        (14, "College"),
        (20, "Graduate"),
    ],
)
def test_grade_label_bands(grade, expected):
    assert grade_label(grade) == expected
