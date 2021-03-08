OUT_FILE_NAME = 'output_question_1.py'

def findPath(arr, x, y, Sum, path, operations):
    global n_row,n_col,num
    if x == n_row-1 and y == n_col-1:
        if Sum+arr[x][y] == num:
            if path not in operations:
                return path
            else:
                return 0
        else:
            return 0
    if Sum>num:
        return 0
    if x<n_row-1:
        ans = findPath(arr, x+1, y, Sum+arr[x][y], path+"D", operations)
        if ans != 0:
            if ans not in operations:
                return ans
            else:
                return 0
    if y<n_col-1:
        ans = findPath(arr, x, y+1, Sum+arr[x][y], path+"R", operations)
        if ans != 0:
            if ans not in operations:
                return ans
            else:
                return 0
    return 0

            
def write_to_file(ans, file_name):
    file = open(file_name, 'a')
    file.write(str(num) + ' '+ans)
    file.write('\n')
    file.close()

if __name__ == "__main__":
    #(a)
    n_row,n_col=9,9
    arr = []
    for i in range(1, n_row+1):
        arr.append([i]*n_col)
    Sum = 0
    x,y=0,0
    path=""
    operations=[]
    required_sum = (65,72,90,110)
    for num in required_sum:
        ans=findPath(arr,x,y,Sum,path, operations)
        if ans!=0:
            write_to_file(ans, OUT_FILE_NAME)
    #(b)
    n_row,n_col=90000,100000
    arr = []
    for i in range(1, n_row+1):
        arr.append([i]*n_col)
    Sum = 0
    x,y=0,0
    path=""
    operations=[]
    required_sum = (87127231192,5994891682)
    for num in required_sum:
        ans=findPath(arr,x,y,Sum,path, operations)
        if ans!=0:
            write_to_file(ans, OUT_FILE_NAME)
            



