with open('gyak.txt','w') as f:
    f.write('három\n'+'négy,öt,hat')

with open('gyak.txt','r')  as f:
    print(type(f))
    print('---')
    result = f.read()
    print(type(result))
print(result)
print('---')

with open('gyak.txt','r')  as f:
    result = f.readlines()
    print(type(result))
print(result)
print('---')

with open('gyak.txt','r')  as f:
    result1 = f.readline()
    result2 = f.readline()
    print(type(result1))
print(result1)
print(result2)
print('---')

with open('gyak.txt','r')  as f:
    for line in f:
        print(line)