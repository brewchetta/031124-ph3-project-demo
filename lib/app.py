# able to log and track dad jokes
from lib.models import DadJoke

class App:

    def __init__(self):
        self.user_input = ''
        DadJoke.create_table()


    def run(self):
        print("Hello and welcome to dad jokes 3000")
        self.main_menu()

    def main_menu(self):
        print("Main Menu")
        print("1. See dad jokes")
        print("2. Add new joke")
        print("3. Delete joke")
        print("4. Exit program")

        while self.user_input not in ["1", "2", "3", "4"]:
            self.user_input = input(">>> ")
            if self.user_input not in ["1", "2", "3", "4"]:
                print("Invalid option please choose a better one")

            if self.user_input == "1":
                self.see_dad_jokes()

            if self.user_input == "2":
                self.add_dad_joke()

            if self.user_input == "3":
                self.delete_dad_joke()

            if self.user_input == "4":
                self.exit_program()


    def see_dad_jokes(self):
        all_jokes = DadJoke.read_all()
        for joke in all_jokes:
            print(f"\n{joke[0]}. {joke[1]}")
        self.user_input = ''

    def add_dad_joke(self):
        print("Add a new dad joke here!")
        self.user_input = input(">>> ")
        new_joke = DadJoke(content=self.user_input)
        new_joke.create()
        print("Your joke has been added! Returning you to the main menu...")

    def delete_dad_joke(self):
        all_jokes = DadJoke.read_all()
        print("Choose the joke to delete by its id and input that here:")
        self.user_input = input(">>> ")
        while self.user_input not in [str(j[0]) for j in all_jokes]:
            print("Invalid id!")
            self.user_input = input(">>> ")
        DadJoke.delete_by_id(self.user_input)
        print("Dad joke deleted!")
        self.user_input = ''

    def exit_program(self):
        print("See ya later!")