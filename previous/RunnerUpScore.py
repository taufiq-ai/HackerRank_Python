if __name__ == '__main__':
    arr = [] 
    n = int(input("Enter number of elements : ")) 
    for i in range(0, n): 
        ele = int(input()) 
        arr.append(ele) # adding the element 
        
    print(arr) 
    WinnerScore = arr[0]
    RunnerUp = arr[1]
    for element in range(len(arr)):      
        if arr[element]>WinnerScore:
            WinnerScore = arr[element]
    for element in range(len(arr)):
        if WinnerScore == RunnerUp or (arr[element] > RunnerUp and arr[element] != WinnerScore):
            RunnerUp= arr[element]
    print(RunnerUp)
   