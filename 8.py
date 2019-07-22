word = 0
ye = 0
while word != "stop":
    word = input("type a word")
    length = len(word)
    while ye < length:
        print(word[ye])
        ye += 1