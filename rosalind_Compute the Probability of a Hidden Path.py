Markov_scores = {
        "A_to_A" : 0.194,
        "A_to_B" : 0.273,
        "B_to_A" : 0.806,
        "B_to_B" : 0.727
        }

sample_string = "AABAABBAABBBBBAAABBAAABAAAAABABABBABAABBAABAAAAABA"

x = list(sample_string)

track = None

A_to_A_count = 0
A_to_B_count = 0
B_to_A_count = 0
B_to_B_count = 0


for i in x:
    if i == "A":     
        if track == 0:
            A_to_A_count += 1
        if track == 1:
            A_to_B_count += 1
        track = 0
#       print("A here")
    if i == "B":
        if track == 0:
            B_to_A_count += 1
        if track == 1:
            B_to_B_count += 1
        track = 1
#       print("B here")
    print(track)
    
print(A_to_A_count)
print(A_to_B_count)
print(B_to_A_count)
print(B_to_B_count)


prob = (0.527**A_to_A_count)*(0.5**A_to_B_count)*(0.473**B_to_A_count)*(0.5**B_to_B_count)

prob_attuned = prob*0.5 # "You may assume the initial probabilites are equal"

print(prob_attuned)  

    