numbers = [1,2,5,8,3,7,9]

res = 1

for num in numbers:
    #  összeszorozzuk a számokat
    res = res * num

# kiírás a kért formában a join és list comprehension használatával
print(f"{numbers} => {' * '.join(str(e) for e in numbers)} = {res}")
