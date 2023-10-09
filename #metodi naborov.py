#metodi naborov
photo_size = {'1920*1080', '800*600'}
photo_size.add('1024*768')
print(photo_size)
other_size = {'300*400', '500*600', '800*600'}
print(other_size)
all_sizes = photo_size.union(other_size)#объеденение элементов, можно сипользовать |
print(all_sizes)
common_s = photo_size.intersection(other_size)#пересечение элементов
#можно использовать знак &
print(common_s)
nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}
res = nums.issubset(other_nums)#один набора включен в другой
print(res)
