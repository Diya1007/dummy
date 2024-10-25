# token_ops.py
def count_token(text, token):
    """Count the occurrences of the token in the text."""
    return text.lower().split().count(token.lower())
