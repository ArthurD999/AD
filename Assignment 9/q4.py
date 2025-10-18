#Author:Arthur drummond
#Date:17/10/2025
#A program takes a word and a character and counts how many times that character is in the word
counter=0
word=input("Enter your word:").lower()
character=input("Enter your character:").lower()

for i in word:
    if i==character:
        counter+=1
print(character,"is in that word",counter,"times")