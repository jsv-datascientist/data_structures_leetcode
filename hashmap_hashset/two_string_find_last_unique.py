def find_unique_string(words):
    # implement this
    duplicates = set()
    seen = set()
    for word in words:
        if word in seen:
            duplicates.add(word)
        else:
            seen.add(word)
    unique = set(words) - duplicates
    
    for word in reversed(words):
        if word not in duplicates:
            return word

    return ""

if __name__ == "__main__":
    print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
    print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
    print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []