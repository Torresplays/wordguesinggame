"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random

global e
LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add yur code (remember to delete the "pass" below)
    """
    
    t=len(secret_word)
    
    
    print("The word now looks like this: ")
    str1=""
    for i in range(t):
        str1="-"+str1
    print(str1)
    e=8
    k=8
    s=3
    while k!=0:
        if str1==secret_word:
            print("Congratulations, the word is:" +str(secret_word))
            k=0
            e=0
            s=1
            
            
        else:
            n=input(("Type a single letter here, then press enter: "))
            n=str(n.upper())
            if len(n)==1:
                h=secret_word.find(n)
                l=secret_word.count(n)
                if l<=1:
                    if h>-1:
                        print("That guess is correct.")
                        
                        
            
                        v=0
                        str2=""
                    
                        for ch in str1:
                                if v==h:
                                    str2+=n
                                else:
                                    str2+=ch
                                v+=1
                        str1=str2
                        
                        
                        

                    else:
                        print("There are no "+str(n)+"'s in the word")
                        k=k-1
                        e=e-1
                        
                        
                        
                            
                            
                    if str1!=secret_word and k!=0 :
                        print("The word now looks like this: "+str(str1))
                        print("You have "+str(k)+" guesses left")
                    
                elif l>1:
                    y=list(str1)
                    for i in range(len(str1)):
                        ch=secret_word[i]
                        if ch==n:
                            y[i]=n
                    str1="".join(y)
                    print("The word now looks like this: "+str(str1))
                    print("You have "+str(k)+" guesses left")

                
            else:
                print("Guess should only be a single character.")      
                print(str1)
    
    if k==0 and s!=1:
        print("Sorry, you lost. The secret word was: "+str(secret_word))
    

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    s=0
    list1=[]
    with open(LEXICON_FILE) as f:
        for line in f:
            line=line.strip()
            list1.append(line)
            s=s+1
        f.close()
    p=random.randint(0,s)
    return list1[p]
    
        
    

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)
    input()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
