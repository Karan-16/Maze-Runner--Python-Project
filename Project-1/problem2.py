#User input source cell coordinates
x1=int(input('Enter the x coordinate of the source cell:'))
y1=int(input('Enter the y coordinate of the source cell:'))
#User input destination cell coordinates
x2=int(input('Enter the x coordinate of the destination cell:'))
y2=int(input('Enter the y coordinate of the destination cell:'))

#Logic
final_source=abs(x1-x2)
final_destination=abs(y1-y2)
a=(((final_destination^final_source)^1)*final_destination)

#Print Solution
print(a)
