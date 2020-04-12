__author__ = 'Amber Melton'


data = open("data.txt", "r")

AWins = 0
BWins = 0

HighestHole = [0, 0]

index = 1

parsum = 0
scoreAsum = 0
scoreBsum = 0


for line in data:

    par = int(line[0])
    scoreA = int(line[2])
    scoreB = int(line[4])

    if scoreA + scoreB > HighestHole[1]:
        HighestHole = [index, scoreA+scoreB]

    if scoreA > scoreB:
        BWins += 1
    elif scoreB > scoreA:
        AWins += 1

    parsum = parsum + par
    scoreAsum = scoreAsum + scoreA
    scoreBsum = scoreBsum + scoreB

    index += 1


def parcompare(score):
    if parsum == score:
        print("Par")
    elif parsum > score:
        print(parsum-score, "under par")
    else:
        print(score-parsum, "over par")


global betterscore
global worsescore

if scoreAsum > scoreBsum:
    betterscore = scoreBsum
    worsescore = scoreAsum
else:
    betterscore = scoreAsum
    worsescore = scoreBsum

print(betterscore, worsescore)

parcompare(betterscore)
parcompare(worsescore)


if betterscore == scoreBsum:
    print(BWins)
else:
    print(AWins)


print(HighestHole[0], HighestHole[1])

input("Program Complete. Press Enter to Exit...")