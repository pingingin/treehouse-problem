import sys

def find_inline(x, y, arr_tree):
    # find horizontal line left to right
    max_tree = 0
    for i in range(0, len(arr_tree[x])):
        if i == y and arr_tree[x][i] > max_tree:
            return True
        else:
            pass
        if arr_tree[x][i] > max_tree:
            max_tree = arr_tree[x][i]
            
    # find horizontal line right to left
    max_tree = 0
    for i in range(len(arr_tree[x])-1, 0, -1):
        if i == y and arr_tree[x][i] > max_tree:
            return True
        else:
            pass
        if arr_tree[x][i] > max_tree:
            max_tree = arr_tree[x][i]
            
    # find vertical line top to down
    max_tree = 0
    for i in range(0, len(arr_tree)):
        if i == x and arr_tree[i][y] > max_tree:
            return True
        else:
            pass
        if arr_tree[i][y] > max_tree:
            max_tree = arr_tree[i][y]
            
    # find vertical line down to top
    max_tree = 0
    for i in range(len(arr_tree) - 1, 0, -1):
        if i == x and arr_tree[i][y] > max_tree:
            return True
        else:
            pass
        if arr_tree[i][y] > max_tree:
            max_tree = arr_tree[i][y]
    
    return False

def main():
    file_data = sys.argv[1]
    f = open(file_data, "r")
    arr_tree = []
    for line in f:
        arr_tree.append([int(x) for x in line[:-1]])
    
    resut_tree = len(arr_tree) * 2 + len(arr_tree[0]) * 2 - 4    

    for i in range(1, len(arr_tree) - 1):
        for j in range(1, len(arr_tree[i]) - 1):
            if find_inline(i, j, arr_tree):
                resut_tree += 1
    
    print(resut_tree)
    
main()