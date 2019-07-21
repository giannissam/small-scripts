import string
alphabet = string.ascii_lowercase

while True:
    text, key = input("Text, key: ").split(",")
    key = int(key.lstrip())
    mappings = dict(zip(alphabet, alphabet[key:] + alphabet[:key]))
    print("".join([mappings[ch] for ch in text.lower() if ch in mappings.keys()]))
