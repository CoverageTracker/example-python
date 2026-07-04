"""URL-safe slug generation."""

from __future__ import annotations

import re
import unicodedata

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text: str, max_length: int = 50) -> str:
    """Convert `text` into a lowercase, hyphenated URL slug.

    Truncates to `max_length` without cutting a word in half. Raises
    ValueError if `max_length` isn't positive or the result would be empty.
    """
    if max_length <= 0:
        raise ValueError("max_length must be positive")

    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = _NON_ALNUM.sub("-", ascii_text.lower()).strip("-")

    if not slug:
        raise ValueError("text has no sluggable characters")

    if len(slug) <= max_length:
        return slug

    truncated = slug[:max_length]
    last_hyphen = truncated.rfind("-")
    if last_hyphen > 0:
        truncated = truncated[:last_hyphen]

    return truncated.strip("-")


def is_slug(value: str) -> bool:
    """Return True if `value` is already a valid slug."""
    if not value:
        return False
    return bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", value))
