
if __name__ == '__main__':
    students=[]
    scores = []
    for i in range(int(input())):
        name = input()
        score = float(input())        
        student = [name,score]

        students.append(student)
        scores.append(score)

    scores = sorted(set(scores))        
    Second_lowest = scores[1]

    # print("\n Output \n")
    # print(sorted(set(scores)))
    # print(Second_lowest)
    
    name = []
    for i in students:
        if i[1]==Second_lowest:
            name.append(i[0])

    #print(str(sorted(name)))
    for i in sorted(name):
        print(i)
        
    
        
        
