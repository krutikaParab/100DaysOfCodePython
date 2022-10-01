#finding year is leap year or not

year = int(input("enter a year to check leap year: "))

if year%4 == 0:
    if year%100 == 0:
        print(f'{year} year is leap year')
        if year%400 == 0:
            #print("leap")
            print(f'{year} year is a leap year')
        else:
            print(f'{year}year not a leap year')
    else:
        print(f'{year}year not a leap year')
else:
    print(f'{year}year not a leap year')
