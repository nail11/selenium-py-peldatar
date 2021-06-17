kisbetuk = ['a','á','b','c','d','e','f','g','h','i','í','j','k','l','m','n','o','ó','ö','ő','p','q','r','s','t','u','ú','ü','ű','x','y','v','w','z']

k = len(kisbetuk) // 10

for i in range(k):
    print(kisbetuk[i], ord(kisbetuk[i]), kisbetuk[i+10], ord(kisbetuk[i+10]), kisbetuk[i+20], ord(kisbetuk[i+20]), kisbetuk[i+30], ord(kisbetuk[i+30]))

for i in range(10-k):
    print(kisbetuk[i+k], ord(kisbetuk[i+k]), kisbetuk[i+k+10], ord(kisbetuk[i+k+10]), kisbetuk[i+k+20], ord(kisbetuk[i+k+20]))