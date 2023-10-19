#while задача
while True:
    num1 = int(input("input first num: "))
    num2 = int(input("input two num: "))
    result = num1 / num2
    print(f"result : {result}")
    continue_request = input("want continue? (yes/no): ")
    if continue_request == "no":
        break
print("end work")

# while True:
#     try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     if num2 == 0:
#         raise ValueError(“Second number can’t be zero”)
#         result = num1 / num2
#         print(f’Result: {result}')
#         continue_request = input("Continue? (y/n): ").lower()
# if continue_request in [‘y’, ‘yes’]:
# continue
# else:
# break
# except ValueError:
# print(“Invalid input, try again”)
# print(“Exited loop”)