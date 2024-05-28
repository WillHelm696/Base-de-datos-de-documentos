class Trie:
    root=None
class TrieNode:
    key=None
    parent=None
    children=None
    isEndOfWord=False
    tf=0


def insert(T, element):
    if T.root is None:
        newNode = TrieNode()
        newNode.key = None
        T.root = newNode
        T.root.parent = None
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
        #current.children = LinkedList()
        #current.children.head = None 

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
        #add(current.children,newNode)
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


def printTrie(node, level=0):

    if node is None:
        return

  # Print the current node's key (or "root" if it's the root node)
    if level == 0:  # Check if it's the root node
        print("root")
    else:
        print(" " * level + node.key +("*, tf=" if node.isEndOfWord else "")+(str(node.tf) if node.isEndOfWord else ""))  # Add * if it's the end of a word

  # Recursively print children with proper indentation
    if node.children:
        for child_node in node.children:
            printTrie(child_node,level + 4)  # Increase indentation level for children

#printTrie(T.root)

#search(T,element)
#Descripción: Verifica que un elemento se encuentre dentro del Trie
#Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
#Salida: Devuelve False o True  según se encuentre el elemento.

def search(T,element):
    if element==None or T==None:
        return 
    else:
        return searchFirst(T.root,element)
        
def searchFirst(root,element):
    if root.key!=element[0]:
        if root.children!=None:
            #print("hay children")
            root=searchChild(root.children,element[0])
            if root!=None:
                #print("se encontro el primer caracter")
                #print(root.key)
                #print(root.children[0].key)
                return searchR(root,element)
            else:
                return False
    elif root.key==element[0]:
        return searchR(root,element)

def searchChild(children,char):
    for i in range(0,len(children)):
        if children[i].key==char:
            return children[i]
    return None

def searchR(Tnode,element):
    #print("caracter a buscar",element[0])
    #print(Tnode.key)
    #print("fin de palabra",Tnode.isEndOfWord)
    if Tnode.key==element[0]:
            if len(element)==1:
                if Tnode.isEndOfWord==True:
                    #print("caso 2")
                    #print("True")
                    return True
                else:
                    #print("caso 3")
                    #print("False")
                    return False
            else:
                if Tnode.children!=None:
                    child=searchChild(Tnode.children,element[1])
                    if child!=None:
                        return searchR(child,element[1:])
                    else: 
                        return False
    else:
        #print("caso 5")
        return False
