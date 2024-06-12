class Trie:
    root=None
class TrieNode:
    key=None
    parent=None
    children=None
    isEndOfWord=False
    tf=0
    palabras_totales=0

def insert(T, element):
    if T.root is None:
        newNode = TrieNode()
        newNode.key = None
        T.root = newNode
        T.root.parent = None
    T.root.palabras_totales=T.root.palabras_totales+1
    insert_R(T.root, element)

def insert_R(current, element):
    if current==None:
        return
    if len(element) < 1:
        current.isEndOfWord = True
        current.tf=current.tf+1
        return
    if current.children==None:
        current.children = []
    newChar = element[0]
    childNode = None
  # Check if a child node with the current character already exists
    for child in current.children:
        if child.key == newChar:
            childNode = child
            break
  # If no child node exists with the current character, create a new one
    if childNode is None:
        newNode = TrieNode()
        newNode.key = newChar
        newNode.parent = current
        current.children.append(newNode)
    else:
        newNode = childNode  #Assing childNode to newNode (for words containing other words)
    insert_R(newNode, element[1:])

#devuelve todas las palabras del trie con su tf
def get_words(root):
    words = {}
    get_wordsR(root,"",words)
    return words

def get_wordsR(node,current_word, words):
    if node!=None:
        if node.key!=None:
            current_word+=node.key
        if node.isEndOfWord:
            words[current_word]=node.tf
        if node.children!=None:
            for i in range(0,len(node.children)):
                aux=current_word
                get_wordsR(node.children[i],current_word,words)
                current_word=aux