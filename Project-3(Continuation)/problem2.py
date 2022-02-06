#importing maze file from mazeSmart
import mazeSmart as ms
#Taking input for the size of the maze
n=int(input("Enter the value of n to create a n x n maze: "))
#Cheching conditions for a valid maze based on the question statement
while True:
    if n <=2:
        n=int(input("Please enter another value that is greater than 2: "))
        continue
    else:
        break
#Calling create_maze function
maze=ms.create_maze(n)
#Printing maze using print_maze function
ms.print_maze(maze)

#Getting source from get_source function
source=ms.get_source()
#Getting destination from get_destination function
destination=ms.get_destination()

#Creating functon to extract coordinates from the string
def process_strings(string1,string2):
    result="Extracted coordinates: "
    string3=""
    str1=""
    str2=""
    #Using is.digit function to access digits in string
    for i in range(0,len(string1)):
        if string1[i].isdigit():
            str1=str1+string1[i]
        if string1[i]=="y":
            str1=str1+","

    for i in range(0,len(string2)):
        if string2[i].isdigit():
            str2=str2+string2[i]
        if string2[i]=="y":
            str2=str2+","
    #Concatenation of strings to print desired output
    string3="("+str1+")and("+str2+")"
    result=result+string3
    #To print the result
    print(result)
    #To return the result
    return string3
coordinates=process_strings(source,destination)

def print_path(c):
    print(c)

def compute_path(maze, n, c):
    current_x = int(c[(c.find("(")) + 1:c.find(",")])  # Finding x coordinate of source
    current_y = int(c[(c.find(",")) + 1:c.find(")")])  # Finding y coordinate of source
    future_x = int(c[(c.rfind("(")) + 1:c.rfind(",")])  #Finding x coordinate of destination
    future_y = int(c[(c.rfind(",")) + 1:c.rfind(")")])  #Finding y coordinate of destination

    # Creating a path variable to print in the desired format
    path = "("+str(current_x)+","+str(current_y)+")"
    # To store the index of current source in maze
    current = 0
    # if x coordinate of source is 0 then current will be source's y coordinate
    # if x not equal to zero then x coordinate will be size of the maze time the x coordinate coz repetitions occur after every gap of size of the maze
    if current_x == 0:
        current = current_y
    if current_x > 0:
        current = current_x * n

    #Checking conditions for cell below the current is green or red
    if maze[current+n] == 'G':
        go_down = 1
        go_right = 0
        # current_x and current_y are the coordinates of the current block
        current_x += 1
        current_y = current_y
        # path will keep on adding all the coordinates of the path
        path += ";"+"("+str(current_x)+","+str(current_y)+")"
        current += n

        #Initiallizing a variable to check the cell and to break
        check = True

        for i in range(current, len(maze)-n-1):
            #Check the cell below
            if current < n*n-n:
                if maze[current+n] == 'G':
                    check = True
                    # If go_down is zero then previous step was go_right
                    # If previous step was go_down then next step has to be go_right
                    if go_down == 0:
                        current += n
                        current_x += 1
                        current_y = current_y
                        path += ";" + "(" + str(current_x) + "," + str(current_y) + ")"
                        #Invert the condition for the next step
                        go_right = 0
                        go_down = 1
                else:
                    check = False
            if current <= n*n-n-1:
                # Checking the block to the right
                if maze[current+n+1] == 'G':
                    check = True
                    #If go_right is zero means previous step was go_down
                    #If previous step was go right then we have to take next step go_down
                    if go_right == 0:
                        current += n+1
                        current_x += 1
                        current_y += 1
                        path += ";" + "(" + str(current_x) + "," + str(current_y) + ")"
                        go_down = 0
                        go_right = 1
                else:
                    check = False
                # Break the loop if destination reached
                if current_x == future_x and current_y == future_y:
                    print_path(path)
                    break
                # If current is red then also break the loop
                if maze[current] == 'R':
                    print_path("Valid zigzag path not found!")
                    break
                # if the current is in the last row and still not reached the destination break the loop
                if current_x == future_x and current_y != future_y:
                    print_path("Valid zigzag path not found!")
                    break
                # if check is false means current is red so break the loop
                if check == False:
                    print_path("Valid zigzag path not found!")
                    break
    # Checking for below cell
    elif maze[current+n+1] == 'G':
        go_down = 0
        go_right = 1

        current_x += 1
        current_y += 1
        #Storing the path as a string in path variable
        path += ";"+"("+str(current_x)+","+str(current_y)+")"
        current += n
        # Check will keep the track that the block is green if not break the loop
        check = True

        for i in range(current, len(maze)-n-1):
            if current <= n*n-n:

                if maze[current+n] == 'G':
                    check = True
                    #If down is zero then previous step was for right
                    #If previous was down we can't go down and we have to go right
                    if go_down == 0:
                        current += n
                        current_x += 1
                        current_y = current_y
                        path += ";" + "(" + str(current_x) + "," + str(current_y) + ")"
                        go_right = 0
                        go_down = 1
                else:
                    check = False
                # Check diagonal
            if current <= n*n-n-1:
                if maze[current+n+1] == 'G':
                    check = True
                    # If right is zero then previous step was go_down and if not vice varsa

                    if go_right == 0:
                        current += n+1
                        current_x += 1
                        current_y += 1
                        path += ";" + "(" + str(current_x) + "," + str(current_y) + ")"
                        go_down = 0
                        go_right = 1
                else:
                    check = False
                #If destination reached break the loop and print the path using print_path function
                if current_x == future_x and current_y == future_y:
                    print_path(path)
                    break
                #If current path is red break the loop
                if maze[current] == 'R':
                    print_path("Valid zigzag path not found!")
                    break
                #If reached last row and destination not rached then break the loop
                if current_x == future_x and current_y != future_y:
                    print_path("Valid zigzag path not found!")
                    break
                if future_y == current_y and current_x != future_x:
                    print_path("Valid zigzag path not found!")
                    break
                # Break the loop if check is false as false checks for the cell being red or green
                if check == False:
                    print_path("Valid zigzag path not found!")
                    break
    else:
        print_path("Valid zigzag path not found!")

# Calling the compute_path function
compute_path(maze, n, coordinates)
