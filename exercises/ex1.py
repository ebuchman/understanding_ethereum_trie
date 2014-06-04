import sys
sys.path.append('src')
import trie, utils, rlp

#initialize trie
state = trie.Trie('triedb', trie.BLANK_ROOT)
state.update('\x01\x01\x02', rlp.encode(['hello']))
print state.root_hash.encode('hex')

