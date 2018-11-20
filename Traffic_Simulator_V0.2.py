#Multiple-car support added
import random
#Each entry in the inner brackets is a row
road = []  #Contains numerical representation of the road
numrows = 20    #Number of rows in road
numcols = 4     #Number of columns in road (must be at least 3: 2 for the barriers,
                #1 for the road)
                #Rows increase downward
numCars = 4     #Number of cars you want in the simulation
numTimeSteps = 10

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
    
    def __init__(self, position,idNum):  #Position is a list of length 2
        self.position = position
        self.x = self.position[0]     #x represents COLUMNS
        self.y = self.position[1]     #y represents ROWS
        self.idNum = idNum
        
    
    #drive currently assumes that road has two lanes (two columns that the cars can actually occupy)
    def drive(self):
        if(road[self.y][self.x-1] > -1 and self.y < (len(road) - 1)):  #If the car is NOT adjacent to the left barrier and still has room to drive downard...
            if(random.randint(1,100) < self.laneSwitchProb):   #If the random number is less than 21, switch lanes
                #########NOTE: PYTHON ACCESSES MATRICES BY ROW--y--FIRST THEN COLUMN--x!!!!!!!!!
                road[self.y][self.x] = 0  #The car is leaving this tile
                self.x = self.x - 1
                self.y = self.y + 1     #The car will always drive down
                road[self.y][self.x] = self.idNum   #Update the car's position
            else:                            #...else, stay in lane
                road[self.y][self.x] = 0  #The car is leaving this tile
                self.y = self.y + 1
                road[self.y][self.x] = self.idNum   #Update the car's position
        elif(road[self.y][self.x-1] == -1 and self.y < (len(road) - 1)):   #If the car IS adjacent to the left barrier and has room to drive downward...
            if(random.randint(1,101) < self.laneSwitchProb):   #If the random number is less than 21, switch lanes
                road[self.y][self.x] = 0  #The car is leaving this tile
                self.x = self.x + 1
                self.y = self.y + 1     #The car will always drive down
                road[self.y][self.x] = self.idNum   #Update the car's position
            else:                            #...else, stay in lane
                road[self.y][self.x] = 0  #The car is leaving this tile
                self.y = self.y + 1
                road[self.y][self.x] = self.idNum   #Update the car's position
        
       
         
#Define list of car objects
carList = []
#Poulate carList:
for i in range(1, numCars+1):    #Range goes from to +1 so that idNum goes from 1 to numCars
    match = True
    randomPosition = [random.randint(1,numcols-2), random.randint(0,numrows/2)]    #Random position for car to start in
    #numcols - 2 is the rightmost lane of any size road (works in general!)
    #numrows/2 is near halfway down from the top of the road (that way a car can't spawn near the bottom and cant move for most of the simulation)
    while(match):   #This while loop ensures that no two cars are randomly initialized in the same position
        if(road[randomPosition[1]][randomPosition[0]] == 0):  #If the road at the randomly-picked position is free...
            match = False                                     #...stop the while loop for this car...
            road[randomPosition[1]][randomPosition[0]] = 1    #...and populate this road element with a car
    
    carList.append(Car(randomPosition,i))  #Initialize new Car and add it to carList
    
for timeStep in range(0,numTimeSteps):
    for car in carList:     #Currently drives cars sequentially, instead of randomly
        car.drive()
    
    #Prints the road as a road:
    print()    #Print new line
    #Printing for each time step shows progress of car along road
    for row in road:
        print(row)
    
    

    



                
                
            
            