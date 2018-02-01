def merge(L1,L2):
    '''
    Merge the contents of two lists, each of which is already sorted
    into a single sorted list.
    '''
    i1 = 0
    i2 = 0
    L = [0]

    '''
    Repeated choose the smallest remaining item from the lists until one
    list has no more items that have not been merged.
    '''
    merge_flag = True
    while merge_flag:

        if L1[i1] < L2[i2]:
            if L1[i1] != L[-1]:
                L.append( L1[i1] )
            i1 += 1
        else:
            if L2[i2] != L[-1]:
                L.append( L2[i2] )
            i2 += 1
        if i1 == len(L1)-1 and i2 == len(L2)-1:
            merge_flag = False
        elif i1 == len(L1):
            i1 = len(L1)-1 #edge cases where the two lists dont merge simultaneously
        elif i2 == len(L2):
            i2 = len(L2)-1
    return L

if __name__ == "__main__":
    L1 = [ 2, 7, 9, 12, 17, 18, 22]
    L2 = [ 1, 5, 6, 8, 13, 14, 15, 18, 19, 23, 25 ] 

    merged_L = merge(L1, L2)
    print(merged_L)
'''
1,2,5,67,8,912,13,14,15,17
'''