book1 = open('book1.txt', 'r', encoding="utf-8").read().lower()
book2 = open('book2.txt', 'r', encoding="utf-8").read().lower()

#remove empty lines
book1 = book1.replace("\n", "")
book2 = book2.replace("\n", "")

#remove any punctuation
puctuation = ["-", ".", "?", ",", ":", ";", "“", "—", "”"]
for i in puctuation:
    book1 = book1.replace(i,"")
    book2 = book2.replace(i, "")

#remove stopwards
stopwords=['what', 'who', 'is', 'a', 'at', 'is', 'he']
for s in stopwords:
    book1 = book1.replace(s, "")
    book2 = book2.replace(s, "")

#remove numbers
for n1 in book1:
    if n1.isnumeric():
        book1 = book1.replace(n1, "")
for n2 in book2:
    if n2.isnumeric():
        book2 = book2.replace(n2, "")

#splitting and making intersection
book1 = set(book1.split())
book2 = set(book2.split())
intrsect = book2.intersection(book1)

#print numbers of common words
print("numbers of common words: ", len(intrsect), "\nwords: ",intrsect)
# print(book1)
# print(book2)





