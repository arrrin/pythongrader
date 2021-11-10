def find_max(num_list,str_len):
    if str_len == 1:
        return num_list[0]
    return max(num_list[str_len-1],find_max(num_list,str_len-1))


inp = [int(i) for i in input('Enter Input : ').split()]

print("Max : "+str(find_max(inp,len(inp))))