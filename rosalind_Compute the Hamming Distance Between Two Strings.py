file = open("rosalind_ba1g.txt", "r")
seqs = file.read().splitlines()
file.close

print(seqs)
print(len(seqs))

String1 = seqs[0]
String2 = seqs[1]



#x = list(String1)
#y = list(String2)



counter = 0


#for i in String1:
#    if String1[i] != String2[i]:
#        counter += 1


for i in range(len(String1)):
    if String1[i] != String2[i]:
        counter += 1

print(counter)     