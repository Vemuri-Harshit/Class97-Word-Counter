count = 0
word = 1


sentence = input("")
print(sentence)



for ltr in sentence:
    count += 1
    print(ltr)
    if(ltr == " "):
        word += 1

print(word)