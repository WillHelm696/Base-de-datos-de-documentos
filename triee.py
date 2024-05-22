class Trie:
	root = None

class TrieNode: 
    parent = None
    children = None   
    key = None
    tf_idf=None
    isEndOfWord = False
####################################################################################

def insert(T, tupla):
    (string,tfidf)=(tupla[0],tupla[1])
    if T.root is None:
        newNode = TrieNode()
        #print("Insertado",string[0])
        newNode.key = string[0]
        newNode.children = [None,None]
        T.root = newNode
        if len(string) == 1:
            T.root.isEndOfWord = True
            T.root.tf_idf=tfidf
    add_trie(T.root, string,tfidf)

def add_trie(current,string,tfidf):
    if current is not None:
        if current.key == string[0]:
            string=string[1:]
            if not string:
                current.isEndOfWord = True
                current.tf_idf = tfidf
                return
            elif current.children[0] != None:
                #print("Hijo de",current.key)
                return add_trie(current.children[0],string)
            else:
                newNode = TrieNode()
                newNode.parent=current
                #print("Insertado como Hijo",string[0])
                newNode.key = string[0]
                newNode.children = [None,None]
                current.children[0] = newNode
                if len(string) == 1:
                    newNode.isEndOfWord = True
                    newNode.tf_idf = tfidf
            return add_trie(current.children[0],string)
        if current.children[1] != None:
            #print(current.key,"Hermano de",current.children[1].key)
            return add_trie(current.children[1],string)
        else:
            newNode = TrieNode()
            newNode.parent=current
            #print("Insertado como hermano",string[0])
            newNode.key = string[0]
            newNode.children = [None,None]
            current.children[1] = newNode
            if len(string) == 1:
                newNode.tf_idf = tfidf
                newNode.isEndOfWord = True
        #print(current.key,"Hermano de",current.children[1].key)
        return add_trie(current.children[1],string,tfidf)
####################################################################################
def search_tf_ifd(current,string):
    if current is None :
        if len(string) > 0:
            return False
        return True
    elif len(string) == 0:
        if current.isEndOfWord:
            return True
        return False
    
    if current.key == string[0]:
        #print("Buscar hijo",current.key)
        return find(current.children[0],string[1:])
    else:
        #print("Buscar hermano",current.key)
        return find(current.children[1],string)

def search(T,string):
    if T.root != None:
        return find(T.root,string)
    return False
####################################################################################
def find(current,string):
    if current is None :
        if len(string) > 0:
            return False
        return True
    elif len(string) == 0:
        if current.isEndOfWord:
            return True
        return False
    
    if current.key == string[0]:
        #print("Buscar hijo",current.key)
        return find(current.children[0],string[1:])
    else:
        #print("Buscar hermano",current.key)
        return find(current.children[1],string)

def search(T,string):
    if T.root != None:
        return find(T.root,string)
    return False
####################################################################################
def delete_node(current):
    if current!=None:
        #print(current.key)
        if current.isEndOfWord == False :
            if current.children[1] is None:
                #print("elimina",current.children[0].key)
                current.children[0]=None
        if current.parent is not None:
            if current.parent.children[1] is not None and current.parent.children[0] is not None:
                if current.key == current.parent.children[1].key:
                    current=current.parent
                    #print("elimina 1 de ",current.key)
                    current.children[1]=None
                    return
                    
                if current.key == current.parent.children[0].key:
                    current=current.parent
                    if current.parent is not None:
                        aux=current.parent
                        if current.key == aux.children[0].key:
                            aux.children[0]=current.children[1]
                        elif current.key == aux.children[1].key:
                            aux.children[1]=current.children[1]
                    return
            #print("SUBE")
            return delete_node(current.parent)

def delete_word(current,element):
    if current is None and len(element) > 0:
        return False
    elif current.key == element[0] and len(element) == 1:
        delete_node(current)
        return True
    if current.key == element[0]:
        return delete_word(current.children[0],element[1:])
    else:
        return delete_word(current.children[1],element)

def delete(T,element):
    Flag=False
    if T.root != None and len(element)>0:
        Flag = delete_word(T.root,element)
        if T.root.key == element[0] and Flag==True:
            if T.root.children==[None,None] is None:
                T.root=None 
            elif T.root.children[0] is None and T.root.children[1] is not None :
                T.root=T.root.children[1]
    return Flag
####################################################################################
def collect_words(node, prefix, words):
    if node is None:
        return
    # Agregar la clave actual al prefijo
    new_prefix = prefix + node.key if node.key else prefix
    # Si es el final de una palabra, agregar al resultado
    if node.isEndOfWord:
        words.append(new_prefix)
    # Recorrer ambos hijos: [0] es el hijo directo y [1] es el hermano
    collect_words(node.children[0], new_prefix, words)
    collect_words(node.children[1], prefix, words)  # note que se usa el prefijo sin añadir la clave actual

def get_all_words(T):
    words = []
    collect_words(T.root, "", words)
    return words