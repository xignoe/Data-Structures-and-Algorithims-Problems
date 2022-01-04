if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
for name,scores in student_marks.items():
    average = float(sum(student_marks[name])/len(student_marks[name]))
    nuAverage = format(average, '.2f')
    if name == query_name:
        print(nuAverage)