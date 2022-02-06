import maze as mz
#Declared variables to count red and green cells
countR=0
countG=0

#User enter the size of the maze
size=int(input('Enter the value of n to create a n X n maze: '))

#Conditions
if size>9 or size<=0:
    print('Invalid value')
elif size==1:
    print('Source and destination cells are the same')
elif size==2:
    print('Destination is reachable from the source')
elif size>=3 or size<10:
    maze=mz.create_maze(size)
    mz.print_maze(maze)
    for i in maze:
        if i=='R':
            countR=countR+1
        elif i=='G':
            countG=countG+1

    print('There are',countG,'green cells and',countR,'red cells.')

#Getting the string result of the get_source function
source=mz.get_source()
#Getting the string result of the get_destination function
destination=mz.get_destination()

sx=0#for x coordinate of the source cell
sy=0#for y coordinate of the source cell
sc=0#for counting the repetitions
for i in source:
    sc=sc+1
    if sc==9:
        sx=source[sc]
    if sc==20:
        sy=source[sc]

dx=0#for x coordinate of the destination cell
dy=0#for y coordinate of the destination cell
dc=0#for counting the repetitions
for j in destination:
    dc=dc+1
    if dc==9:
        dx=destination[dc]
    if dc==20:
        dy=destination[dc]
#Part a and Part b solution
print('The coordinates of the source cell are ('+str(sx)+','+str(sy)+').')
print('The coordinates of the destination cell are ('+str(dx)+','+str(dy)+').')

#Explicit type casting
num1=int(sx)
num2=int(dy)

#Initializing count for green cell
green=0
#Logic Building
for i in range(num1,size,1):#Interval of 1 because there is a gap of 1 in each element in a row
    if maze[i]=='G':
        green=green+1
        if i==5:
            break

#Initializing count for red cell
red=0
#Logic Building
for j in range(num2,len(maze),size):#Interval of size because in a  particular column the next element occurs after the gap of size
    if maze[j]=='R':
        red=red+1
        if j==24:
            break

#Part c solution
print('Number of green cells in the source row:',green)
print('Number of red cells in the destination col:',red)

