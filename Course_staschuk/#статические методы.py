#статические методы
class Comment:
    def __init__(self, text):#создание собственных атрибутов
        self.text = text
        self.votes_qty = 0

    def upvote(self, qty):
        self.votes_qty += qty

    @staticmethod#декоратор
    def merge_comments(first, second):#статический метод
        return f"{first} {second}"

my_comment = Comment("My comment")
m_1 = Comment.merge_comments("Thanks!", "Excellent.")
print(m_1)

m_2 = my_comment.merge_comments("Great", "OK")
print(m_2)