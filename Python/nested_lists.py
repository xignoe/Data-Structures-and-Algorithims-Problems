lis = []
second_low = []
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    lis.append([name,score])
    scores.add(score)
    
second_low_score = sorted(scores)[1]

for name, score in lis:
    if score == second_low_score:
        second_low.append(name)
        
for name in sorted(second_low):
    print(name, end='\n')