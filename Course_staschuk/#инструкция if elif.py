#инструкция if in def
# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "not integer"
    
#     if a >= b:
#         return f"{a} > or = {b}" 
#     return f"{a} < {b}"

# print(nums_info(True, 10))
# print(nums_info(10, 2))
# print(nums_info(4, 15))

def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "not integer"
    elif a >= b:
        info = f"{a} > or = {b}" 
    else:
        info = f"{a} < {b}"
    return info

print(nums_info(True, 10))
print(nums_info(10, 2))
print(nums_info(4, 15))