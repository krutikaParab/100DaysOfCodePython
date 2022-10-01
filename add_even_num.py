#Adding an even num:
def addEvenNum(num):
    add = 0
    for i in range(num):
        if i%2 == 0:
            add += i
    sum_even = add
    return sum_even

if __name__ == '__main__':
    range_num = int(input("Please specify the range...within a range we will add even numbers\n"))

    even_sum = addEvenNum(range_num)

    print(f'The sum of even numbers within range 1 to {range_num} is {even_sum}')
