def remove_adjacent_duplicates(s: str) -> str:
    stack=[]

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

print(remove_adjacent_duplicates("abcd"))
print(remove_adjacent_duplicates("aab"))
print(remove_adjacent_duplicates("abba"))
print(remove_adjacent_duplicates("aba"))