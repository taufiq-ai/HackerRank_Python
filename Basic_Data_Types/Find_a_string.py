def count_substring(string, sub_string):
    lenght_of_sub_string =len(sub_string)
    count = 0
    
    for index in range(len(string)):
        if sub_string == string[index:(index+(lenght_of_sub_string))]:
            count +=1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)