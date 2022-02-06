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
