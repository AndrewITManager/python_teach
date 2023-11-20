#практика тернанрный опертатор
my_img = ('1920', '1080')

# print(f"{my_img[0]}x{my_img[1]}") if len(
#     my_img) == 2 else print("Incorrect image formatting")

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else "Incorrect image formatting"

print(info)