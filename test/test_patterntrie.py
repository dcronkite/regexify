import re

from regexify.pattern_trie import PatternTrie


def test_pattern_matches_original():
    data = ['there', 'hi', 'python', 'pythons', 'hiya']
    trie = PatternTrie(*data)
    pat = re.compile(trie.pattern)
    for word in data:
        assert pat.match(word)
