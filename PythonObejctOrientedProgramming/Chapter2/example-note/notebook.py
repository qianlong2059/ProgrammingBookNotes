from note import Note

class NoteBook:
    def __init__(self):
        self.notes = []

    def new_notes(self,content,tag):
        self.notes.append(Note(content,tag=tag))

    def _find_note(self,id):
        for note in self.notes:
            if id == note.id:
                return note

    def modify(self,id,content=None,tag=None):
        if content != None:
            self._find_note(id).content = content
            print(f"note id:{id}, content has been modified.")
        
        if tag != None:
            self._find_note(id).tag = tag
            print(f"note id:{id}, tag has been modified.")


    def search(self,filter):
        return [note for note in self.notes if note.match(filter)]
    
if __name__=="__main__":
    notebook = NoteBook()
    notebook.new_notes(content="hello world", tag="1")

    notes = notebook.search("world")
    print(notes[0].id,notes[0].content)
    
    notebook.modify(id=1,content="hello again")
    print(notes[0].id,notes[0].content)