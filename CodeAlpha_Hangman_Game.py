import random

Words_list = ["algorithm", "database", "debug", "bandwidth", "encryption"]
incorrect_guess_count = 0

print("----------------HANGMAN GAME-----------------\n")
print("You have 6 incorrect guesses to find the word")

word_index = random.randint(0, 4)
game_display = ["_"] * len(Words_list[word_index])

def get_guess():
    while True:
        ch = input("Enter your guess: ").lower()
        if len(ch) == 1 and ch.isalpha():
            return ch
        print("Please enter a single alphabet letter")

while incorrect_guess_count < 6:
    print("\nWord:", "".join(game_display))
    ch = get_guess()
    indices = [i for i, char in enumerate(Words_list[word_index])
               if char == ch]
    if not indices:
        incorrect_guess_count += 1
        print("Wrong Guess. Try Again")
        print(f"You have {6 - incorrect_guess_count} incorrect guesses left")
    else:
        for idx in indices:
            game_display[idx] = ch
        print("Correct Guess")
        print("Word:", "".join(game_display))
    if "".join(game_display) == Words_list[word_index]:
        print("You won the game")
        break

if "".join(game_display) != Words_list[word_index]:
    print("You lost the game")
    print("The word was:", Words_list[word_index])