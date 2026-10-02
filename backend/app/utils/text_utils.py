def trim_text(
    text: str,
    max_chars: int = 700
) -> str:

    if not text:
        return ""

    text = str(text).strip()

    if len(text) <= max_chars:
        return text

    return text[:max_chars] + "..."