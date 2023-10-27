s = "room"
i=0
while(i<len(s)):
    temp =1
    print(s[i],end="") 
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            temp+=1
    print(temp) 
    
    
