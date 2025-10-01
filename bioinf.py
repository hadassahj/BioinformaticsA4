#problem 1
seq = input("Scrie secventa: ")
alfabet = set(seq)
print("Alfabetul:", alfabet)


#problem 2
seq2= "ACGGGCATATGCGC"
alfabet2 = set(seq2)
for litera in alfabet2:
    count = seq2.count(litera)
    print("the percentage of", litera, "is", count/len(seq2)*100)





