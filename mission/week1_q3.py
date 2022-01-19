score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]
student_number = len(score)

def get_avg(score):
    for idx in range(student_number):
        print(f'{idx+1} 번, 평균 : {sum(score[idx])/2}')

get_avg(score)