def vector_module(text):
    mod=0
    for word in text:
        mod+=text[word]*text[word]
    mod=np.sqrt(mod)
    return mod

def cosine_similarity(text1,text2):
  if text1 == text2:
    return 1.0
  mod1=vector_module(text1)
  mod2=vector_module(text2)
  if mod1==0 or mod2==0:
      return 0
  sumxy = 0
  for i in text1:
        sumxy += text1[i]*text2[i]
  return sumxy/(mod1*mod2)
