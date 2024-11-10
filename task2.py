#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''

def find_factors(x):
    y = x + 1
    factor_list = []
    
    for n in range(y):
        if n != 0:
           if  x%n == 0:
               factor_list.append(n)
    return factor_list        


def main():
    factors = []
    myNumber = 24
    factors = find_factors(myNumber)
    print (factors)

if __name__ == "__main__":
    main()