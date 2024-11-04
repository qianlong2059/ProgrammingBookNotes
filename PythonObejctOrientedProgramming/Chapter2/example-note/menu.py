import sys
from notebook import NoteBook
from note import Note

class Menu:
    def __init__(self):
        self.notebook = NoteBook
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify,
            "5": self.quit
        }
    
    def display_menu(self):
        print("""
Notebook Menu
    1. Shwo All Notes

        """)

    def show_notes(self):
        pass

    def search_notes(self):
        pass

    def add_note(self):
        pass

    def modify(self):
        pass

    def quit(self):
        pass
        
if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()