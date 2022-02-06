#importing mazeasn4 module in this module
import mazeAsn4 as mz
import math

#Calling create_maze function
maze=mz.create_maze(0)
#Printing maze using print_maze function
mz.print_maze(maze)
#Getting source from get_source function
source=mz.get_source()
#Getting destination from get_destination function
destination=mz.get_destination()
#Getting x coordinate of source
sx=source[0][1]
#Getting y coordinate of source
sy=source[1][1]
#Getting x coordinate of destination
dx=destination[0][1]
#Getting y coordinate of destination
dy=destination[1][1]

print("Source coordinates: X: "+str(sx)+" Y: "+str(sy))
print("Destination coordinates: X: "+str(dx)+" Y: "+str(dy))

def compute_path(maze,source,destination):
    #Getting x coordinate of source
    src_x=source[0][1]
    #Getting y coordinate of source
    src_y=source[1][1]
    #Getting x coordinate of destination
    des_x=destination[0][1]
    #Getting y coordinate of destination
    des_y=destination[1][1]

    # Initializing T with the source coordinates
    T = [[(src_x, src_y)]]

    # Initializing lists sub_list and l
    sublist=[]
    l=[]
    count=1
    #Getting the size of the maze
    n=math.sqrt(len(maze))
    for i in maze:
        #appending all items in maze as a list to a new list
        l.append(i)
        #To create a sublist in a list for each row as a list of tuples
        if count % n == 0:
            sublist.append(tuple(l))
            #So that the row does not get added twice, clear the list to append another row from starting
            l.clear()
        count =count+1


    #Loop to iterate until T is empty
    while len(T)>0:
        # i,j contains the last element coordinates of the sublist T[0]
        i = T[0][len(T[0]) - 1][0]
        j = T[0][len(T[0]) - 1][1]

        #if i and j are same as destination coordinates break the loop
        if i == des_x and j == des_y:
            return T[0]
            break
        #Temp contains a temporary sublist od T[0]
        temp = T[0]
       #Emptying the sublist to append the new sublist
        del T[0]
        #Checking first condition for green cell
        if (i + 1) < n and (j - 1) < n:
            if (j - 1) > 0 and sublist[i + 1][j - 1] == 'G':
               #Create a new temporary list copy as changing the list would alter the list and we are required to check the other conditions as well
                copy_1 = temp.copy()
                copy_1.append((i + 1, j - 1))
                T.append(copy_1)
        #Checking second condition for green cell
        if (i + 1) < n and j < n:
            if sublist[i + 1][j] == 'G':
                #Create a new temporary list copy as changing the list would alter the list and we are required to check the other conditions as well
                copy_2 = temp.copy()
                copy_2.append((i + 1, j))
                T.append(copy_2)
        #Checking third condition for green cell
        if (i + 1) < n and (j + 1) < n:
            if sublist[i + 1][j + 1] == 'G':
                #Create a new temporary list copy as changing the list would alter the list and we are required to check the other conditions as well
                copy_3 = temp.copy()
                copy_3.append((i + 1, j + 1))
                T.append(copy_3)

        temp = []
    return T


# Calling the function compute path
ans = compute_path(maze,source,destination)
# If result not empty
if len(ans)>0:
    print("Valid path found:",ans)
# If list is empty
else:
    print("A valid path does not exist!")



