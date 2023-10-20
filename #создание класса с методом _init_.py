#создание класса с методом _init_
class Comment:
    def __init__(self, text):#создание атрибутов
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1