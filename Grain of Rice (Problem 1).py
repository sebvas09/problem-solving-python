# Rice Grain Problem: Exponential Growth & Square Counting (Problem 1)

# Plan:
# - Start from the first square
# - Keep adding grains (doubling each time)
# - Stop when adding the next square would exceed the total grains 
# - Return how many squares were filled


grains = int(input("Grains of rice:")) #will be used as the condition in the while loop 

total_grains = 0 #initialize total grains
squares = 0 #initialize square (which square we're on)

while total_grains + (2**squares) <= grains: #check if adding the next square stays within the grain limit
  total_grains = total_grains + (2**squares) #adds new grain value to total_grains after adding a new square 
  squares +=1 #count number of squares 
print(squares) #output number of squares 
