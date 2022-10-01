#trying to find out highest scores among the class

def findHighScore(scorelist):
    high_score = 0
    for score in scorelist:
        if int(score) > high_score:
            high_score = int(score)
    max_score = high_score
    return max_score

if __name__ == '__main__':
    print("Let's find out highest score in class")
    score_list = input("Scores\n").split()

    high_score = findHighScore(score_list)

    print(f'So the highest score is {high_score}')
