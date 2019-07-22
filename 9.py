word = 0
list = []
sum = 0
while word != "stop":
    word = input("type a number")
    if word != "stop":
        word = int(word)
        list.append(word)
length = len(list)
while length > 0:
    length -= 1
    sum += list[length]
numbers = len(list)
sum = sum / numbers
print(sum)