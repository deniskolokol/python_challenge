#https://www.hackerrank.com/challenges/zipped/


students_N, subjects_X = map(int, input().split())
student_scores = []
for subj in range(subjects_X):
    student_scores.append(list(map(float, input().split())))

zipped_scores = zip(*student_scores)
for score in zipped_scores:
    print(sum(score)/subjects_X)