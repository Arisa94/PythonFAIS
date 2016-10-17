number = 100098003
word = str(number)
wordlist = list(word)
counter = 0
for x in wordlist:
    if x == '0':
        counter = counter + 1

print counter
