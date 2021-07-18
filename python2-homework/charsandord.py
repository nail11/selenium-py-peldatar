# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
#
# Szavak előfordulási gyakorisága
# Állapítsuk meg, hogy az alábbi szövegben (TEXT) melyik szó hányszor fordul elő s írassuk ki az eredményt a következő formában: szó_1 előfordulások_száma_1 szó_2 előfordulások_száma_2 ...
#
# Az eredményt úgy írassuk ki, hogy a lista szavak szerint rendezve legyen. Minden szó kisbetűsen szerepeljen, vagyis pl. a 'The' és 'the' szavak azonos szónak számítanak.
#
# Használjuk az str.split() függvényt (paraméter nélkül) a whitespace karakterek eltávolítására.
#
# Az egyes szavakhoz kapcsolódó írásjelekkel (pont, vessző, idézőjel, stb.) nem kell most foglalkozni.
#
# Ezt a szöveget használd a ruttatáshoz: The Old Sea-dog at the Admiral Benbow


with open('old_see_dog.txt') as text:
    content = text.read()

    word_list = content.lower().replace('\n', '').replace('\r', '').replace('"', '').replace('.', '').replace(',', '') \
 \
        .replace(';', '').replace('?', '').replace('--', '').replace('17__', '').replace(':', '').split()

word = ''
word_dic = dict()

for i, word in enumerate(word_list):

    if word not in word_dic:
        word_dic.update({word: word_list.count(word)})
        sorted_word_dic = dict(sorted(word_dic.items()))

print(sorted_word_dic)
