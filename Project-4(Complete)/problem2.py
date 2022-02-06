#importing mazeasn4 module in this module
import mazeAsn4 as mz
import math

# Initializing count variable to count the number of times we get the valid path
count = 1
# Create a dictionary of valid maze according to the question statement
D = dict(Maze1=[], Maze2=[], Maze3=[], Maze4=[], Maze5=[], Maze6=[], Maze7=[], Maze8=[], Maze9=[], Maze10=[])
#Iterating 10 times to compute valid 10 mazes
while count <= 10:
    # Creating a maze using create_maze() function
    maze = mz.create_maze(1)
    # Getting the source using get_source() function
    source = mz.get_source()
    # Getting the destination using get_destination() function
    destination = mz.get_destination()

    def compute_path(maze, source, destination):

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
        sublist = []
        l = []
        count = 1
        # To get the size of the maze we can take the square root of the total length of the maze string.
        n = int(math.sqrt(len(maze)))

        for i in maze:
            #appending all items in maze as a list to a new list
            l.append(i)
            #To create a sublist in a list for each row as a list of tuples
            if count % n == 0:
                sublist.append(tuple(l))
                #So that the row does not get added twice, clear the list to append another row from starting
                l.clear()
            count += 1

        # looping till the list T is empty
        while T:
            # i,j contains the last element coordinates of the sublist T[0]
            #There is a tuple inside a list which is inside a list so we need 3 indexes
            #i is at 0 position of the tuple
            i = T[0][len(T[0]) - 1][0]
            #j is at 1 position of ftuple
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
                if sublist[i + 1][j - 1] == 'G' and (j - 1) > 0:
                   #Create a new temporary list copy as changing the list would alter the list and we are required to check the other conditions as well
                    #Adding the  source index first
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

    # Calling the function compute_path
    ans = compute_path(maze, source, destination)
    #If list not empty
    if len(ans)>0:
        #Initiallizing dictionary
        if count == 1:
            D["Maze1"] = [maze, ans]
        if count == 2:
            D["Maze2"] = [maze, ans]
        if count == 3:
            D["Maze3"] = [maze, ans]
        if count == 4:
            D["Maze4"] = [maze, ans]
        if count == 5:
            D["Maze5"] = [maze, ans]
        if count == 6:
            D["Maze6"] = [maze, ans]
        if count == 7:
            D["Maze7"] = [maze, ans]
        if count == 8:
            D["Maze8"] = [maze, ans]
        if count == 9:
            D["Maze9"] = [maze, ans]
        if count == 10:
            D["Maze10"] = [maze, ans]
        count =count+ 1
    # If list is empty contiune until we find all 10 valid maze
    else:
        continue
print("Successfully created maze.txt with dictionary keys and values!")

# Creating a text file maze.txt with write method
with open("maze.txt", "w") as f:
    #Initilize a string to store the key value pairs as string by concatenation
    string = ""
    # converting the dictionary into a string as items in dictionary can be added in string format only
    for key in D.keys():
        for value in D.values():
            if D[key]==value:
                string += str(key) + ":" + str(value) + "\n"
    # Writing string into the file maze.txt
    f.write(string)
    # closing the file maze.txt
    f.close()
