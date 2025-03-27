import sys


class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.eow = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return cur.eow


def load_file_insert_tree(filename):
    trie = Trie()
    with open(filename, 'r') as f:
        for w in f:
            trie.insert(w.strip().lower())
    return trie


def split_words(text):
    word = ""
    words = []

    for c in text:
        if c.isalnum() or c == "'":
            word += c
        else:
            if word:
                words.append(word)
                word = ""

    if word:
        words.append(word)

    return words


def check_spelling(trie, text):
    words = split_words(text)
    errors = [w for w in words if not trie.search(w.lower())]

    if errors:
        for e in errors:
            text = text.replace(e, f"~~{e}~~")
        return text

    return None


def main():
    if len(sys.argv) != 3:
        print("Usage: python spell_checker.py <dictionary> <input>")
        sys.exit(1)

    dictionary_file = sys.argv[1]
    input_file = sys.argv[2]

    trie = load_file_insert_tree(dictionary_file)

    with open(input_file, 'r') as f:
        for line_number, l in enumerate(f, start=1):
            corrected = check_spelling(trie, l.strip())

            if corrected:
                print(f"{line_number}: {corrected}")


if __name__ == "__main__":
    main()
