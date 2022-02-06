1#User input source cell coordinates
x1=int(input('Enter the x coordinate of the source cell:'))
y1=int(input('Enter the y coordinate of the source cell:'))
#User input destination cell coordinates
x2=int(input('Enter the x coordinate of the destination cell:'))
y2=int(input('Enter the y coordinate of the destination cell:'))

#Logic
final_source=abs(x1-y1)
final_destination=abs(x2-y2)
a=(final_destination-final_source)%2

#Print Soltion
print(a)




