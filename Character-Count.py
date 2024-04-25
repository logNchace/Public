string = input("Character Count: ")
count = 0
for char in string:
    if char != ' ':
        count += 1
print("Total character count:", count)
