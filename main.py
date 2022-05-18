#Guess The Number (Python)

from os import name as os_name, system as os_system
from random import randint as ran_randint

if os_name == "nt":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Guess The Number")

def clearconsole():
    if os_name == "nt": os_system("cls")
    else: os_system("clear")

class Main():
    def __init__(self):
        clearconsole()
        self.max_number = 100
        self.number_generated = ran_randint(0, self.max_number)
        self.number_of_wrong_guess = 0

        while True:
            print(f"Guess the number between 0 and {self.max_number}")
            self.guessed_number = int(input(">"))

            while type(self.guessed_number) != int:
                clearconsole()
                print(f"This is not a number, Please enter a number between 0 and {self.max_number}")
                self.guessed_number = int(input(">"))

            if guessed_right := self.compare():
                print("Do you want to exit? Type 'yes' or 'y' to exit, Press Enter to continue.")
                menu = input(">")
                if menu in ["yes", "y"]:
                    clearconsole()
                    break
                else:
                    clearconsole()
                    self.number_generated = ran_randint(0, self.max_number)
                    self.number_of_wrong_guess = 0
            
    def compare(self):
        clearconsole()
           
        if self.guessed_number == self.number_generated:
            print(f"Congratulations, You guessed the number! it was {self.number_generated}")
            if self.number_of_wrong_guess == 0:
                print("How did you guess it on first try?")
            print(f"Number of Wrong guess: {self.number_of_wrong_guess}")
            return True

        elif self.guessed_number > self.max_number:
            self.number_of_wrong_guess += 1
            print(f"That's way higher than the max number! You guessed {self.guessed_number}\n")

        elif self.guessed_number > self.number_generated:
            self.number_of_wrong_guess += 1
            print(f"Try lower, You guessed {self.guessed_number}\n")
                        
        elif self.guessed_number < self.number_generated:
            self.number_of_wrong_guess += 1
            print(f"Try higher, You guessed {self.guessed_number}\n")
      
if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        clearconsole()    