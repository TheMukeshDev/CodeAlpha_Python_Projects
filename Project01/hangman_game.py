import random

# ● Use a small list of 5 predefined words (no need to use a file or API).
# ● Limit incorrect guesses to 6.
# ● Basic console input/output — no graphics or audio.
# Key Concepts Used: random, while loop, if-else, strings, lists.
guess_word=["dog","cat","rat","cow","goat","ox"]
HANGMANPICS = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def hangman_game():
    
    print("Welcome to Hangman Game : ")
    # print
    print("You have 6 chance to guess the correct word")
    print("Hint 💡 (Animals name) and no same input")
    chance=0

    secret=list(random.choice(guess_word))
    
    print(f"Enter letter to guess : ") 
    print(HANGMANPICS[chance])
    guess_letter=[]
    while(chance<6):
        
        # display
    
        blank_letter=""
        for s in secret:
            if s in guess_letter:
                blank_letter+=s
            else:
                blank_letter+="_"
                
        print(f"Guess {blank_letter}")
        print(f" Guess letter : {",".join(guess_letter)}")
        print(f"Live reaminaing {6-chance}")
        
        if "_" not in blank_letter:
            print("\n----------------------------------")
            print(f"🎉 You win! The word was '{",".join(secret)}'.")
            print("----------------------------------")
            return
        
        # input
        try:
            word=input("Guess a letter : ").lower()
        except:
            print("Invalid input")
            if len(word)>1 or word.isalpha():
                print("Invalid input. Please enter a single letter.")
            continue
        
        guess_letter.append(word)
            
        if word  in secret:
            
                print(f"Good guess! '{word}' is in the word.")
            
        else:
            chance+=1
            
            print(f"Sorry, {word} is not in the word\nLive remaining: {chance}")
            print(HANGMANPICS[chance])
        if(chance==0):
            print(f"\n😓game is over \n The correct word is {secret}")
        
        
hangman_game()