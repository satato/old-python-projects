__author__ = 'Amber Melton'


Data = open("data.txt", "r")


parsum = 0
scoresum = 0

for line in Data:

    par = int(line[0])
    score = int(line[2])

    if par - score == 0:
        print("Par")
    elif par - score < 0:
        distance = score - par
        if distance == 1:
            print("Bogey")
        else:
            print("Double Bogey")
    else:
        distance = par - score
        if distance == 1:
            print("Birdie")
        else:
            print("Eagle")

    parsum = parsum + par
    scoresum = scoresum + score


if parsum - scoresum == 0:
    print("Par")
elif parsum - scoresum < 0:
    distance = scoresum - parsum
    if distance == 1:
        print("Overall: Bogey")
    else:
        print("Overall: Double Bogey")
else:
    distance = parsum - scoresum
    if distance == 1:
        print("Overall: Birdie")
    else:
        print("Overall: Eagle")


input("Program Complete. Press Enter to Exit...")