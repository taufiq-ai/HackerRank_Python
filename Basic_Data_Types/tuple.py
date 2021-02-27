        #Test#
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
    
#     t = tuple(integer_list)
#     print(t)
#     print(hash(t))

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    hash_value = hash(t)
    print(hash_value)