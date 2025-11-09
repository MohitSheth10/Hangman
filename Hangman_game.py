
import random
#add hints improve #add impossible mode
mode=""
file_path=r"D:\Coding\Projects\Hangman"
while mode!="easy" and mode!="medium" and mode!="hard":
    mode=input("Which mode do you choose:\nEasy\nMedium\nHard: ").lower().strip()
    if mode=="easy":
        file=open((file_path + r"\easy.txt"),"r")
    elif mode=="medium":
        file=open((file_path + r"\medium.txt"),"r")
    elif mode=="hard":
        file=open((file_path + r"\hard.txt"),"r")
    else:
        print("Invalid")
    

data=file.readline()
list=data.split() 
word=random.choice(list)
word=word.upper()
total_chances=7
guessed_word="_"*len(word)
while total_chances!=0:
    print(guessed_word)
    letter=input("Enter the letter: ").upper()
    if letter in word:
        for i in range(0,len(word)):
            if letter==word[i]:
                guessed_word = guessed_word[:i] + letter + guessed_word[i+1:] #?
        if guessed_word==word:
            print("Congratulations!!")
            break
    else:
       total_chances-=1
       print("Incorrect guess")
       print(f"The number of chances remaining is:  {total_chances}")
else:
    print(f"You have{total_chances}guesses remaining")
    print("Fail")
print("You had",total_chances,"guesses remaining")
print("The correct word was",word)
