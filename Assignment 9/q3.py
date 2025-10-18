#Author:Arthur drummond
#Date:17/10/2025
#A program takes word and organises it diffently

word=input("Enter your word:")
without=""
if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
    print(word+"way")
else:
    
    for i in range(1,len(word)):
        without=without+word[i]
        
    
    print(without+word[0]+"ay")