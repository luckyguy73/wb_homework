from collections import defaultdict
from functools import reduce


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.setdefault(letter, {})
        node['*'] = None

    def _search(self, word):
        node = self.root
        for letter in word:
            if letter not in node: return {}
            node = node[letter]
        return node

    def search(self, word: str) -> bool:
        return '*' in self._search(word)

    def startsWith(self, prefix: str) -> bool:
        return bool(self._search(prefix))

# class Trie:
#     def __init__(self):
#         tree = lambda: defaultdict(tree)
#         self.root = tree()

#     def insert(self, word):
#         reduce(dict.__getitem__, word, self.root)['*']

#     def search(self, word):
#         return '*' in reduce(lambda d, c: d.get(c, {}), word, self.root)

#     def startsWith(self, prefix):
#         return bool(reduce(lambda d, c: d.get(c, {}), prefix, self.root))


# class Trie(collections.defaultdict):

#     def __init__(self):
#         super().__init__(Trie)

#     def insert(self, word):
#         if not word:
#             self['']
#         else:
#             self[word[0]].insert(word[1:])

#     def search(self, word):
#         if not word:
#             return '' in self
#         return word[0] in self and self[word[0]].search(word[1:])

#     def startsWith(self, prefix):
#         if not prefix:
#             return True
#         return prefix[0] in self and self[prefix[0]].startsWith(prefix[1:])