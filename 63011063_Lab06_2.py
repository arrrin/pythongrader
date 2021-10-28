def sorted_list(num_list, list_sort, str_len):
    if str_len < 1:
        return
    else:
        list_sort.append(max(num_list))
        num_list.pop(num_list.index(max(num_list)))
        sorted_list(num_list, list_sort, str_len - 1)


str_inp = input("Enter your List : ").split(",")
str_temp = list(map(int, str_inp))
lst_s = []
sorted_list(str_temp, lst_s, len(str_temp))
print("List after Sorted : ", lst_s, sep="")
