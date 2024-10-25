# prompt.py
from dummy.file_ops import read_corpus
from dummy.token_ops import count_token

def report_count(token, file_path='/mnt/data/corpus.txt'):
    """Generate a report on how many times the token appears in the corpus."""
    text = read_corpus(file_path)
    count = count_token(text, token)
    print(f"The term {token} shows up in the corpus {count} times.")
