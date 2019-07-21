import string
alphabet = string.ascii_lowercase
punctuation = string.punctuation + " "
while True:
    text = input("Text: ")
    key = int(input("Key:"))
    mappings = dict(zip(alphabet, alphabet[key:] + alphabet[:key]))
    punctuation = dict(zip(punctuation, punctuation))
    mappings = {**mappings, **punctuation}
    print("".join([mappings[ch] for ch in text.lower() if ch in mappings.keys()]))
