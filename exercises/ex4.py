import sys
sys.path.append('src')
import trie, utils, rlp

#initialize trie from previous hash; add new [key, value] where key has common prefix
state = trie.Trie('triedb', 'b5e187f15f1a250e51a78561e29ccfc0a7f48e06d19ce02f98dd61159e81f71d'.decode('hex'))
print 'using root hash from ex2b'
print rlp.decode(state.get('\x01\x01\x03'))
print ''
state = trie.Trie('triedb', 'fcb2e3098029e816b04d99d7e1bba22d7b77336f9fe8604f2adfb04bcf04a727'.decode('hex'))
print 'using root hash from ex3'
print rlp.decode(state.get('\x01\x01\x02'))
print rlp.decode(state.get('\x01\x01\x02\x55'))
print rlp.decode(state.get('\x01\x01\x02\x57'))
