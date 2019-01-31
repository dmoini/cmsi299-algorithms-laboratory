import fileinput

initial_line = True
for line in fileinput.input():
    line = line.rstrip()
    arr = line.split(' ')
    participants, budget, hotels, weeks = arr[0], arr[1], arr[2], arr[3]
    if not initial_line:
        
    initial_line = False
    # print(arr)