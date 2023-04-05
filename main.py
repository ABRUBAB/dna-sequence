sqns1 = input()
sqns2 = input()
match = 0
for i in range(0, len(sqns1)):
    if sqns1[i] == sqns2[i]:
        match += 1
print((match/len(sqns1)) * 100,"%")
