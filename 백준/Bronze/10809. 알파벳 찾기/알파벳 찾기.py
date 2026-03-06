s = input()
alphabet = [-1] * 26 

for i in range(len(s)):
    char = s[i]  
    if alphabet[ord(char) - ord("a")]  == -1 :  
        alphabet[ord(char) - ord("a")] = i 

for i in range(26) :
    print(alphabet[i], end = " ") 