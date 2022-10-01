#program to find average height of students
def calculateAvgHeight(height_list):
    length_of_list = len(height_list)
    sum_of_height = 0
    
    for i in range(0, length_of_list-1):
        sum_of_height += int(i)

    average = float(sum_of_height//length_of_list)
    return average

if __name__ == '__main__':
    height_list = input("Please specify students height to find an average\n").split()

    average = calculateAvgHeight(height_list)

    print(f'An average height of the class is {average}')
    


