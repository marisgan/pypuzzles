def make_sublists(string: str):
    lst = string.split()
    result = list([])
    for j in range(len(lst)+1):
        for i in range(len(lst)):
            if lst[i:i+j] not in result:
                result.append(lst[i:i+j])
    return result


print(make_sublists('a f z'))
