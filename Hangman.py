import random

def make_guess():
    guess = input("Enter a letter: ").lower()
    return guess

def _get_stickman_stages():
    return [
        """
           +---+
               |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
           |   |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
          /|   |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
          /|\\  |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
          /|\\  |
          /    |
               |
               |
        =========
        """,
        """
           +---+
           O   |
          /|\\  |
          / \\  |
               |
               |
        =========
        """
    ]

def ask_to_play_again():
    return input("Do you want to play again? (y/n) ").lower() == 'y'

class Hangman:
    def __init__(self):
        self.words = ['python', 'coding', 'programming', 'developer']
        self.word = random.choice(self.words)
        self.guessed_word = ['_'] * len(self.word)
        self.ATTEMPTS = 6
        self.stickman_stages = _get_stickman_stages()

    def display_game_status(self):
        print(self.stickman_stages[6 - self.ATTEMPTS])
        print(f"\n{' '.join(self.guessed_word)}")

    def update_word(self, guess):
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.guessed_word[i] = guess
        print("Great Job")

    def reduce_attemps(self):
        self.ATTEMPTS -= 1
        print(f"Wrong guess! \nYou have {self.ATTEMPTS} attempts left.")

    def check_win(self):
        return '_' not in self.guessed_word

    def check_loss(self):
        return self.ATTEMPTS == 0

    def play(self):
        while self.ATTEMPTS > 0:
            self.display_game_status()
            guess = make_guess()
            if guess in self.word:
                self.update_word(guess)
            else:
                self.reduce_attemps()


            if self.check_win():
                print("Congratulations! You won!")
                break
            elif self.check_loss():
                print(self.stickman_stages[6])
                print("You lost! The word was", self.word)
                break

if __name__ == "__main__":
    while True:
        game = Hangman()
        game.play()

        if not ask_to_play_again():
            break