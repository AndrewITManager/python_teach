#задача class
class Image:
    def __init__(self, resolution, title, extension):#собственные методы создаются при создании экземляра класса
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):#метод
        self.resolution = new_resolution #новое разрешение

    def __str__(self):
        return f"{self.title}.{self.extension}"

first_img = Image('1920x1080', "My Dog", 'jpg')

print(first_img.resolution)
print(first_img.title)
print(first_img.extension)

first_img.resize('4000x3000')
print(first_img.resolution)

print(first_img)

second_img = Image('8000x5000', "My cat", 'png')
print(second_img)
