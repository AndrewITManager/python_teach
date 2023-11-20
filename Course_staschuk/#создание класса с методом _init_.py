#создание класса с методом _init_
class Comment:
    def __init__(self, text):#создание собственных атрибутов
        self.text = text
        self.votes_qty = 0

    def upvote(self, qty):
        self.votes_qty += qty

    @staticmethod#статический метод
    def merge_comments(first, second):
        return f"{first} {second}"

 

first_comment = Comment("First comment")
print(first_comment.text)
print(first_comment.votes_qty)

print(first_comment.__dict__)

print(dir(first_comment)) #все атрибуты экземпляра

my_comment = Comment("My comment")
# print(dir(my_comment))
# print(my_comment)
# print(my_comment.text)
# print(my_comment.votes_qty)
my_comment.upvote = 10
print(my_comment.votes_qty)

# second_comment = Comment("Second comment")
# second_comment.upvote(2)
# print(second_comment.votes_qty)



