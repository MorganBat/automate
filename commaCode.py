def commaCode(lst):
    ans = []
    i = 0

    while i < (len(lst) - 2) :
        ans.append(lst[i])
        ans.append(', ')
        i += 1

    ans.append(lst[-2])
    ans.append(", and ")
    ans.append(lst[-1])
    
    return ''.join(ans)

print(commaCode(['apples', 'banana','tofu', 'cats']))