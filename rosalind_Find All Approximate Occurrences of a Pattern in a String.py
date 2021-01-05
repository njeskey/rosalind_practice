file = open("rosalind_ba1h.txt", "r")
fileread = file.read().splitlines()
file.close

Pattern = fileread[0]
Text = fileread[1]
d = fileread[2]
t = int(d)



#Pattern = "ATTCTGGA"
#Text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
#d = 3

length_pattern = len(Pattern)

l = len(Text) - (length_pattern - 1)

print(l)

frag = []

for start in range(0,l):
    
    fragment = Text[start : start + length_pattern]
    frag.append(fragment)

print(frag)

start_locs = []

counter_list = 0
for n in frag:
    counter = 0
    for i in range(len(n)):
        if n[i] != Pattern[i]:
            counter += 1
    if counter < t + 1:
        start_locs.append(counter_list)
    counter_list += 1
    
#print(start_locs)

string_ints = [str(int) for int in start_locs]
printstring = " ".join(string_ints)
    
print(printstring)