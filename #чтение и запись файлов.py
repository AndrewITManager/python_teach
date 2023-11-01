# test_file = open('test.txt', 'w')
# # print(test_file)
# # print(type(test_file))
# test_file.write("First string\n")
# test_file.close()

with open('test.txt', 'w') as test_file:
    test_file.write("Первая строка\n")
    test_file.write("Вторая строка\n")
    test_file.write("Третья строка\n")

# test_file = open('test.txt')
# print(test_file.read())
# test_file.close()

with open('test.txt') as test_file:
    print(test_file.read())

with open('test.txt') as test_file:
    lines = test_file.readlines()
    for line in lines:
        print(line)

with open('test.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break
        
