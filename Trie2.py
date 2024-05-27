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
#delete(T,element)
#Descripción: Elimina un elemento se encuentre dentro del Trie
#Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
#Salida: Devuelve False o True  según se haya eliminado el elemento.

def delete(T,element):
    words=0
    if T==None or element==None:
        return False
    else:
        if search(T,element)==False:
            return True
        else:
            if T.root.key!=element and T.root.children!=None:
                root=searchChild(T.root.children,element[0])
                if root!=None:
                    return deleteR(root,element,words)
                else:
                    return False
            else:
                return deleteR(T.root,element,words)

def deleteR(Tnode,element,words):
    for i in range(0,len(element)):
        if Tnode.isEndOfWord==True:
            words=words+1
        if Tnode.key==element[i]:
            if i==len(element)-1:
                words=words-1
                if Tnode.children==None and words==0:
                    #print("palabra única")
                    #deleteNode(Tnode,element,None)
                    return True
                elif Tnode.children!=None:
                    #print("es parte de una palabra más larga")
                    Tnode.isEndOfWord=False
                    return True
                else:
                    #print("contiene palabras más pequeñas")
                    #print(Tnode.key,"key")
                    Tnode.isEndOfWord=False
                    deleteNode(Tnode,element)
                    return False
            else:
                Tnode=searchChild(Tnode.children,element[i+1])
                

def deleteNode(node,element):
    for i in range(0,len(element)):
        #print(node.key,"key a borrar")
        #print(node.isEndOfWord,"end of word")
        parent=node.parent
        if len(node.parent.children)>1:
            parent.children.remove(node)
            break
        
        node.key=None
        node.children=None
        node=parent
    
#Implementar un algoritmo que dado un árbol Trie T, un patrón p (prefijo) y un entero n, 
#escriba todas las palabras del árbol que empiezan por p y sean de longitud n. 
def CommonPrefix(T,p,n):
    if T.root==None:
        return
    charFound="" #caracteres de p
    lastChar=findCommonPrefixR(T.root,p,p,charFound)
    if lastChar==None:
        return None
    words=[]
    foundWord=p #inicio
    return findwordsPrefix(lastChar,words,n,foundWord,p)

def findCommonPrefixR(current,p,p_aux,charFound):
    if current==None:
        return None
    if len(p)==0:
        if p_aux==charFound:
            return current #ultimo caracter del prefijo
        return None
    next=None
    if current.children!=None:
        for child in current.children:
            if child.key==p[0]:
                next=child #nodo con key del prefijo
                charFound=charFound+child.key
        if next!=None:
            return findCommonPrefixR(next,p[1:],p_aux,charFound)
        return None
    return None
def findwordsPrefix(current,words,n,foundWord,p):
    if current==None:
        return words
    if current.isEndOfWord==True:
        if len(foundWord)==n:
            words.append(foundWord)
    if current.children!=None:
        for child in current.children:
            findwordsPrefix(child,words,n,foundWord+child.key,p)
    return words
#Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos 
#pertenecen al mismo documento y False en caso contrario.
#Se considera que un  Trie pertenece al mismo documento cuando:
#Ambos Trie sean iguales (esto se debe cumplir)
#Si la implementación está basada en LinkedList, considerar el caso donde las palabras 
#hayan sido insertadas en un orden diferente.
#En otras palabras, analizar si todas las palabras de T1 se encuentran en T2. 
def belongToSameDocument(T1,T2):
    if T1==None or T2==None:
        return False
    return areEqual(T1.root,T2.root,True)
    
def areEqual(T1node,T2node,flag):
    if T1node==None or T2node==None:
        flag=False
        return flag
    if T1node.key==T2node.key:
        if T1node.children==None and T2node.children==None:
            flag=True
            return flag
        elif T1node.children!=None and T2node.children!=None:
            if len(T1node.children)!=len(T2node.children):
                flag=False
                return flag
            for i in range(0,len(T1node.children)):
                areEqual(T1node.children[i],T2node.children[i],flag)
                if flag==False:
                    break
    else:
        flag=False
    return flag
            
#Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. 
#Dos cadenas son invertidas si se leen de izquierda a derecha y contiene los mismos caracteres que si se 
#lee de derecha a izquierda, ej: abcd y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, 
#sin embargo abcd y dcka no son invertidas ya que difieren en un carácter.

#inverse=word[::-1]


def invertedChains(T):
    if T==None:
        return
    words=get_words(T.root)
    for i in range(0,len(words)):
        word=words[i]
        if search(T,word[::-1]):
            return True
    return False
#Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol Trie T y 
#la cadena  devuelve la forma de auto-completar la palabra. Por ejemplo, para la 
#llamada autoCompletar(T, ‘groen’) devolvería “land”, y a que podemos tener “groenlandia” o “groenlandés” 
#(en este ejemplo la palabra groenlandia y groenlandés pertenecen al documento que representa el Trie). 
#Si hay varias formas o ninguna, devolvería la cadena vacía. 
#Por ejemplo, autoCompletar(T, ma’) devolvería “” (cadena vacia) si T presenta las cadenas “madera” y “mama”. 
def autoCompletar(T,cadena):
    if T==None or cadena=="":
        return
    lastChar=findCommonPrefixR(T.root,cadena,cadena,"")
    #print(lastChar.key)
    words=get_words(lastChar)
    #print(words)
    suggestions=[]
    chars_s=""
    for j in range(0,len(words)):
        word=words[j][1:]
        #print(word, "word")
        index=0
        #print(word[index])
        for n in range(j+1,len(words)):
            word_aux=words[n][1:]
            #print(word_aux,"word aux")
            for i in range(0,len(word)):
                if word[index]==word_aux[index]:
                    #print("match")
                    chars_s+=word[index]
                    index=index+1
                    #print(chars_s,"chars s")
                elif chars_s!="":
                    if suggestions!=[]:
                        if len(chars_s)>len(suggestions[0]):
                            suggestions[0]=chars_s
                            chars_s=""
                            index=0
                    else:
                        suggestions.append(chars_s)
                    break
    if suggestions==[]:
        return ""
    else:
        return suggestions[0]
