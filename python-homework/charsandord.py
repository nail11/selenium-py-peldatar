kisbetuk = []

for i in range(26):
    kisbetuk.append(chr(i+97))

k = len(kisbetuk) % 10

for i in range(k):
    print(kisbetuk[i], ord(kisbetuk[i]), kisbetuk[i+10], ord(kisbetuk[i+10]), kisbetuk[i+20], ord(kisbetuk[i+20]))
for i in range(10-k):
    print(kisbetuk[i+k], ord(kisbetuk[i+k]), kisbetuk[i+k+10], ord(kisbetuk[i+k+10]))

