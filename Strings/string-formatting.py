def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    print(width)
    for i in range(1,number+1):
        print (f"{str(i).rjust(width)} {str(oct(i)[2:]).rjust(width)} {str(hex(i).upper()[2:]).rjust(width)} {str(bin(i)[2:]).rjust(width)}")

if __name__ == '__main__':
    #n = int(input())
    n = 15
    print_formatted(n)