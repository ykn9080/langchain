


def tiktoken_len(text):
    import tiktoken
    tokenizer=tiktoken.get_encoding("cl100k_base")
    return len(tokenizer.encode(text))