import sys
sys.path.append('src')
import trie, utils, rlp

#initialize trie from previous hash; add new entry with same key.
state = trie.Trie('triedb', '15da97c42b7ed2e1c0c8dab6a6d7e3d9dc0a75580bbc4f1f29c33996d1415dcc'.decode('hex'))
print state.root_hash.encode('hex')
print state.root_node
print ''
state.update('\x01\x01\x02', rlp.encode(['hellothere']))
print state.root_hash.encode('hex')
print state.root_node
# we now have two tries, addressed in the database by their respective hashes, though they each have the same key


