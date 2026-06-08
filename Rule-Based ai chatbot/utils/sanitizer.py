def sanitize(raw_text):
    return raw_text.lower().strip()


def is_empty(text):
    return not text