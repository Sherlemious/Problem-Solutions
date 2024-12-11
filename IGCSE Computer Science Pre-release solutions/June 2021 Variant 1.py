# Variables

Names = {}
Abstentions = 0
VoterIDs = []
winners = []
high = 0
winner = ""

# Inputs (with validation)

Tutor_Group = input("Please enter Tutor group name:\n")
Num_of_students = int(input("Please enter number of students:\n"))

while Num_of_students < 28 or Num_of_students > 35:
    Num_of_candidates = input(
        "Please enter number a valid number of students (between 28 and 35):\n")

Num_of_candidates = int(input("Please enter number of candidates:\n"))

while Num_of_candidates > 4:
    Num_of_candidates = input(
        "Please enter number a valid number of candidates (less than or equal 4):\n")

for i in range(Num_of_candidates):
    print(f"Please enter name of candidate number {i+1}:")
    Names[input()] = 0

# Voting


for i in range(Num_of_students):
    voterID = input("Please enter your Voter ID:\n")
    if voterID not in VoterIDs:
        VoterIDs.append(voterID)
        vote = input("Please enter the vote:\n")
        while vote not in Names and vote.lower() != "abstain":
            vote = input("Please input a valid candidate name or abstain:\n")
        if vote in Names:
            Names[vote] += 1
        else:
            Abstentions += 1
    else:
        print("you already voted:\n")


for name in Names:
    if Names[name] > high:
        high = Names[name]

for name in Names:
    if Names[name] == high:
        winners.append(name)

print(f"Number of Abstentions is equal to {Abstentions}")

if len(winners) > 1:
    print(f"There is a tie between {winners} with votes of {high}")
    Names = {}
    VoterIDs = []
    for winner in winners:
        Names[winner] = 0
    for i in range(Num_of_students):
        voterID = input("Please enter your Voter ID:\n")
    if voterID not in VoterIDs:
        VoterIDs.append(voterID)
        vote = input("Please enter your vote:\n")
        while vote not in Names and vote.lower() != "abstain":
            vote = input("Please input a valid candidate name or abstain:\n")
        if vote in Names:
            Names[vote] += 1
        else:
            Abstentions += 1
    else:
        print("you already voted:\n")

    for name in Names:
        if Names[name] > high:
            high = Names[name]
            winner = name

print(f"The winner for tutorgroup {Tutor_Group} is: {winner} by {Names[winner]} votes \nThe number of Abstentions was {Abstentions}")
