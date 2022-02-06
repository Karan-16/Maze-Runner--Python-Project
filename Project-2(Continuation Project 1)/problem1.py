import maze as mz
#Initializing count
count_red=0
count_green=0

#User Enters The Size Of Maze
size=int(input('Enter the value of n to create a n X n maze: '))

#Conditions on maze
if size>9 or size<=0:
    print('Invalid value')
elif size==1:
    print('Source and destination cells are the same')
elif size==2:
    print('Destination is reachable from the source')
elif size>=3 or size<10:
    #Creating maze using the create function defined in maze module
    maze=mz.create_maze(size)
    #Printing maze using the print function defined in maze module
    mz.print_maze(maze)
    for i in maze:
        #Fulfilling the conditions
        if i=='R':
            count_red=count_red+1
        elif i=='G':
            count_green=count_green+1

    print('There are',count_green,'green cells and',count_red,'red cells.')
