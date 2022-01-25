# test score, mid : 50, fianl : 75

class Student_Score():
    def __init__(self):
        self.__mid = 0
        self.__final = 0
            
    @property
    def Score_mid(self):
        return self.__mid

    @Score_mid.setter
    def Score_mid(self, mid):
        self.__mid = mid

    @property
    def Score_final(self):
        return self.__final

    @Score_final.setter
    def Score_final(self, final):
        self.__final = final

    def Score_average(self):
        score_average = (self.__mid + self.__final) / 2
        print (score_average)
        
score = Student_Score()
score.Score_mid = 50
print(score.Score_mid)
score.Score_final = 75
print(score.Score_final)
score.Score_average()
