import random
#Each entry in the inner brackets is a row
road = []  #Contains numerical representation of the road
numrows = 20    #Number of rows in road
numcols = 4     #Number of columns in road (must be at least 3: 2 for the barriers,
                #1 for the road)
                #Rows increase downward

#Populate road matrix:
for i in range(0,numrows):     #Fills matrix with rows
    road.append([])

for i in road:
    for j in range(0, numcols):      #Fills matrix with columns
        if (j == 0 or j == numcols - 1):
            i.append(-1)
        else:
            i.append(0)

#Sanity check:
#print(road)


class Car:
    laneSwitchProb = 21  #Probability of switching lanes = laneSwitchProb - 1
    
    def __init__(self, position):  #Position is a list of length 2
        self.position = position
        self.x = self.position[0]     #x represents COLUMNS
        self.y = self.position[1]     #y represents ROWS
        
    
    #drive currently assumes that road has two lanes (two columns that the cars can actually occupy)
    def drive(self):
        if(road[self.y][self.x-1] > -1 and self.y < (len(road) - 1)):  #If the car is NOT adjacent to the left barrier and still has room to drive downard...
            if(random.randint(1,101) < self.laneSwitchProb):   #If the random number is less than 21, switch lanes
                road[self.y][self.x] = 0  #The car is leaving this tile
                self.x = self.x - 1
                self.y = self.y + 1     #The car will always drive down
                road[self.y][self.x] = 1   #Update the car's position
            else:                            #...else, stay in lane
                road[self.y][self.x] = 0  #The car is leaving this tile
                self.y = self.y + 1
                road[self.y][self.x] = 1   #Update the car's position
        elif(road[self.y][self.x-1] == -1 and self.y < (len(road) - 1)):   #If the car IS adjacent to the left barrier and has room to drive downward...
            if(random.randint(1,101) < self.laneSwitchProb):   #If the random number is less than 21, switch lanes
                road[self.y][self.x] = 0  #The car is leaving this tile
                self.x = self.x + 1
                self.y = self.y + 1     #The car will always drive down
                road[self.y][self.x] = 1   #Update the car's position
            else:                            #...else, stay in lane
                road[self.y][self.x] = 0  #The car is leaving this tile
                self.y = self.y + 1
                road[self.y][self.x] = 1   #Update the car's position
        
        

firstCar = Car([1,0])   #Position = [column, row] = [x,y]
for i in range(0,10):    #Second argument is the number of time steps
    firstCar.drive()
    #Prints the road as a road:
    print()    #Print new line
    #Printing for each time step shows progress of car along road
    for a in road:
        print(a)



                
                
            
            