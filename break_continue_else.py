#break
for i in range(1,11):
    if i==5:
        break
    else:
        print(i)

#continue
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i)

#else
for i in range(1,11):
    if i==15:
        break
    else:
        print(i)
else:
    print("All numbers are printed wthin the given range.")
