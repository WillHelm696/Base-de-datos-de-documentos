import numpy as np

def cosine_similarity(text1,text2):
  if text1 == text2:
            return 1.0

        sumxx = 0
        sumyy = 0
        sumxy = 0
  
        for i in text1:
            sumxx += int(text1[i][1])**2 #acceder al tf de la palabra
            if i in text2: #si la palabra se encuentra en el segundo texto
                sumyy += int(text2[i][1])**2
                sumxy += int(text1[i][1])*int(text2[i][1])
        return sumxy/np.sqrt(sumxx*sumyy)
