"""
Custom slugify for MkDocs TOC: for function-style headings (single name before '('),
strip everything after '(' so IDs are just the function name (e.g. gpio_set, connect).
Section headings like "GPIO (General Purpose...)" are slugified normally.
"""
import re


def slugify_name_only(value, separator):
    """
    Slugify for markdown.extensions.toc: takes (value, separator) per Python-Markdown.
    If heading looks like a function (single identifier followed by '('), use only
    that name as the slug. Otherwise slugify the full text (for section headings).
    """
    if not value:
        return "section"
    # Strip HTML tags (heading text may already be rendered)
    text = re.sub(r"<[^>]+>", "", value)
    text = text.replace("`", "").strip()
    idx = text.find("(")
    if idx >= 0:
        before = text[:idx].strip()
        # Only strip when part before '(' is a single identifier (no spaces) = function heading
        if before and " " not in before and re.match(r"^[\w.-]+$", before):
            text = before
    if not text:
        return "section"
    # Slugify: lowercase, keep underscores and alphanumeric, replace spaces with separator
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", separator, text).strip(separator)
    return text or "section"
