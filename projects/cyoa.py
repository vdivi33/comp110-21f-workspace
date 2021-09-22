"""Hang-Py, A typical hangman game!"""
import random 

player: str = ""
hang_word: str = ""
hang_line: str = ""
points: int = 0
guesses: int = 0
replayed: bool = False
NAMED_CONSTANT = "\U00000000"
SMILE = "\U0001F604"
SAD = "\U0001F615"
SNAKE = "\U0001F40D"
CROSS = "\U0000274C"
print(SMILE)


def main() -> None:
    """The main function that makes calls to other functions. Compiles and prints the final points."""
    global points
    global guesses
    global hang_line
    global player
    global replayed
    if(replayed is False):
        greet()
    else:
        print(f"Welcome back {player} {SMILE}!")
    if(replayed is False):
        play_option: str = input("Would you like to play? Enter y or n :: ")
    play_option = "y"
    if(play_option == "y" or play_option == "Y"):
        bonus_option: str = input("Would you like to turn on Snake Eyes mode? Enter y or n :: ")
        difficulty: str = input("Would you like the words to be easy or hard? ")
        if(difficulty == "easy" or difficulty == "e"):
            hang_word = choose_easy()
        else:
            hang_word = choose_hard()
        print("Alright! Enjoy the game!")
        check(hang_word)
        print("")
        print(f"The hidden word is {len(hang_word)} characters long!")
        i: int = 0
        while i < len(hang_word):
            hang_line = hang_line + "-"
            i = i + 1  
        print(hang_line)
        guess(hang_word)
        if(bonus_option == "y" or bonus_option == "Y"):
            points = snake_eyes(points)
        print(f"The word was {hang_word}")
        print(f"Total {points} points! with a total of {guesses} guesses")
        replay: str = input("Would you like to play again y or n?: ")
        if(replay == "y" or replay == "Y"):
            replayed = True
            hang_word = ""
            hang_line = ""
            points = 0
            guesses = 0
            main()
        else:
            print("Thanks for playing!")
    else:
        print("Okay, thanks for stopping by!")


def greet() -> None:
    """Greets the player and assigns their name to the global player variable."""
    global player
    player = input("What is your name? ")
    print(f"Hello There {player}! Welcome to hang py {SNAKE}, a typical hang man game but python themed!")
    print("-You have double as many guesses as the words number of characters. Ex: cobra would have 10 guesses.")
    print("- Snake eyes is an optional mode that can either double your points or lose the game!")
    print("-The snake eye function returns true is two random integers are equal.")
    print("-Guess the word at anytime by typing in 'guess'!")
    print("-You earn a point for ever correct letter!")
    print(f"Goodluck {player}")


def choose_easy() -> str:
    """Uses a random function to randomly pick 1 of 6 'easy' words for the hangman game."""
    i: int = random.randint(1, 5)
    if(i == 1):
        return "slither"
    elif(i == 2):
        return "snake"
    elif(i == 3):
        return "viper"
    elif(i == 4):
        return "python"
    elif(i == 5):
        return "cobra"
    return "fangs"


def choose_hard() -> str:
    """Uses a random function to randomly pick 1 of 6 'hard' words for the hangman game."""
    i: int = random.randint(1, 5)
    if(i == 1):
        return "serpentine"
    elif(i == 2):
        return "boa constrictor"
    elif(i == 3):
        return "anaconda"
    elif(i == 4):
        return "black mamba"
    elif(i == 5):
        return "vertebrae"
    return "titanoboa"


def check(word: str) -> str:
    """This function checks whether the random word contains a space."""
    if(word.find(" ") < 0):
        return "Note: This word has a space in it! "
    return ""


def guess(x: str) -> None:
    """The primary function that prompts the player to choose a letter. The player can initiate 'guess mode' where they can earn full points for guessing correctly!"""
    print("Type in 'guess' if you think you got the word")
    global points
    global guesses
    global hang_line
    c: bool = True
    letter: str = ""
    i: int = 0
    current: int = 0
    while(guesses < 2 * len(x)):
        g: str = input("Enter a single Letter ")
        if(g == "guess"):
            print("Entered Guess Mode")
            full: str = input("Enter the full word: ")
            if(full == x):
                print(f"Correct! {SMILE}")
                points = len(x)
                break
            else:
                print(f"That is Incorrect {player} {CROSS}")
                break
        else:
            if(len(g) == 1 and letter.find(g) < 0):
                while(i < len(x)):
                    if(x[i] == g):
                        letter = letter + g
                        c = False
                        points = points + 1
                        current = i
                        print(f"Nice job {player}, Correct: {points}")
                        hang_line = (fill(g, current))

                    i = i + 1
                if(c is True):
                    print(f"That is incorrect {CROSS}")
                i = 0
                c = False
            else:
                print("That is not a valid character or you have already used this character")
            guesses = guesses + 1
       

def fill(word: str, pos: int) -> str:
    """A function to fill in the correctly guessed letters on the empty dashed line string."""
    global hang_line
    ln = list(hang_line) 
    ln[pos] = word
    hang_line = "".join(ln)
    print(hang_line)
    return hang_line


def snake_eyes(p: int) -> int:
    """An addiitonal mode that the player choose that can either reduce their points by half or double it."""
    r1: int = random.randint(0, 2)
    r2: int = random.randint(0, 2) 
    if(r1 == r2):
        print(f"The {SNAKE} saw {player}, points halved {SAD}")
        p = p // 2
    else:   
        p = p * 2
        print(f"The {SNAKE} did not see {player}! Points multiplied by 2! {SMILE}")
    return p


if __name__ == "__main__":
    main()