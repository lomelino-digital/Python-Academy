print('Write a message to count the characters:')
message = input()
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1


print(count)
