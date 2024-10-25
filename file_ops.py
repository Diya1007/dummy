# file_ops.py
def read_corpus(file_path):
    """Read the contents of the corpus file."""
    with open(file_path, 'r') as file:
        return file.read()
