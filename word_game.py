#Practicing class inheritance
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            pass
    
class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    
    def round_winner(self, player1_word:str, player2_word: str):
        vowels = "aeiou"
        player1_count = 0
        player2_count = 0
        for letter in player1_word:
            if letter in vowels:
                player1_count += 1
        for letter in player2_word:
            if letter in vowels:
                player2_count += 1
        if player1_count > player2_count:
            return 1
        elif player1_count < player2_count:
            return 2
        else:
            return "tie"

class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    
    def round_winner(self, player1_word:str, player2_word: str):
        word_bank = ["rock","paper","scissors"]
        if player1_word not in word_bank and player2_word not in word_bank:
            pass
        elif player2_word not in word_bank and player1_word in word_bank:
            return 1
        elif player1_word not in word_bank and player2_word in word_bank:
            return 2
        elif player1_word == player2_word:
            pass
        elif player1_word == "rock" and player2_word == "scissors":
            return 1
        elif player1_word == "paper" and player2_word == "rock":
            return 1
        elif player1_word == "scissors" and player2_word == "paper":
            return 1
        else:
            return 2
        
    
        




if __name__=="__main__":
    p = RockPaperScissors(4)
    p.play()
