#модуль time
import time

# print(time.ctime(1698950785))

start_time = time.time()
print(start_time)

my_list = list(range(100000000))
print(my_list[1000])

# time.sleep(2.5)#остановка на некоторое время выполнение программы

end_time = time.time()
print(end_time)

print("Total duration of the operation: ", end_time - start_time)
