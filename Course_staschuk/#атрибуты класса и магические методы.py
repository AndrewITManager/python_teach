#атрибуты класса
class Comment:
    total_comments = 0
    def upvote(self):
        self.votes_qty += 1

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1

    def __add__(self, other):#магический метод
        return {'text': f"{self.text} {other.text}", 
                'total_votes_qty': self.votes_qty + other.votes_qty}



first_comment = Comment("First comment")
print(Comment.total_comments)
second_comment = Comment("Second comment")
print(Comment.total_comments)
third_comment = Comment("Third comment")
print(Comment.total_comments)

#магические методы классов
first_comment.upvote()
second_comment.upvote()

print(first_comment + second_comment)#при использовании + найдет метод __add__
