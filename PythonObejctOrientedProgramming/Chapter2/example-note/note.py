import datetime

lastest_id = 0

class Note:
    def __init__(self, content, tag=''):
        global lastest_id
        lastest_id += 1
        self.id = lastest_id
        self.creation_time = datetime.datetime.today()
        self.tags = tag
        self.content = content

    def match(self, filter):
        return filter in self.content or filter in self.tags


if __name__=="__main__":
    note1 = Note("hello first")
    note2 = Note("hello again")

    print(note1.content)
    print(note2.content)

    print(note1.match("first"))