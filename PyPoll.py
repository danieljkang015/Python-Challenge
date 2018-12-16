import os
import csv

election_data_csv = os.path.join('..', 'PyPoll', 'election_data.csv')
 
total_votes = 0
candidate = {}
candidate_percent = {}
vote_count = 0
winner = ""

with open(election_data_csv, newline = "") as election_data:
    reader = csv.reader(election_data, delimiter = ",")
    header = next(reader)
    for row in reader:

        total_votes += 1

        if row[2] in candidate.keys():
            candidate[row[2]] += 1
        else:
            candidate[row[2]] = 1
        for name, value in candidate.items():
            candidate_percent[name] = round((value/total_votes) * 100, 2)
        for name in candidate.keys():
            if candidate[name] > vote_count:
                winner = name
                vote_count = candidate[name]

print(f'Election Results')
print(f'-------------------------------------')
print(f'Total Votes: {str(total_votes)}')
print(f'-------------------------------------')
for name, value in candidate.items():
    print(f'{str(name)}: {str(candidate_percent[name])}% ({str(value)})')
print(f'-------------------------------------')
print(f'Winner: {winner}')
print(f'-------------------------------------')