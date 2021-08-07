x = int(input("input: "))

def count_sheep(sheep):
    for i in range(1, sheep + 1):
        print(str(i) + " sheep...", end='')
    print()

count_sheep(x)
