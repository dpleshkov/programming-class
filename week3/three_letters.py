words = []
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(26):
    for y in range(26):
        for z in range(26):
            words.append('{}{}{}'.format(alph[x],alph[y],alph[z]))

for x in range(20):
    print(words)
