'''
Created on Apr 24, 2018

@author: danielfinlay
'''

#Class that stores an image with it's corresponding label, for easy manipulation
#So you can have a list of datapoints
class DataPoint:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        
#Class X represents Image/Text to be parsed
class X:
    def __init__(self, x):
        self.x = x
    #Method turns an image into a 2d array
    def tobyteArray(self):
        image = []
        row = []
        for line in self.x:
            for char in line:
                if char is ' ':
                    row.append('0')
                else:
                    row.append(char)
            image.append(row)
            row = []
        return image
    

        
#Method takes in image file & corresponding label file
#Call getDataPoints to return a list of all images with their corresponding labels as shown in main below 
class FileParser:
    def __init__(self, imagefile, labelfile):
        self.imagefile = imagefile
        self.labelfile = labelfile
        if 'face' in imagefile or 'face' in labelfile:
            self.numOrFace = 'face'
        else:
            self.numOrFace = 'num'
        self.x = []
        self.y = []
        self.dataPoints = []
    
    def getDataPoints(self):
        self.extractAllX()
        self.extractAllY()
        return self.dataPoints
    
    def extractAllY(self):
        index = 0
        with open(self.labelfile, 'r') as in_file:
            for lines in in_file:
                self.y.append(lines)
                dp = DataPoint(self.x[index], self.y[index])
                self.dataPoints.append(dp)
                index = index + 1
                
            
            
    def extractAllX(self):
        index = 0
        lines = []
        with open(self.imagefile, 'r') as in_file:
            for line in in_file:
                lines.append(line)  
                index = index + 1
                
                if self.numOrFace is 'num':
                    if index is 28:
                        currentX = X(lines)
                        self.x.append(currentX.tobyteArray())
                        index = 0
                        lines = []
                elif self.numOrFace is 'face':
                    if index is 70:
                        currentX = X(lines)
                        self.x.append(currentX.tobyteArray())
                        index = 0
                        lines = []


if __name__ == '__main__':
    #Create a fileparser object with image & corresponding label file
    fp = FileParser('trainingimages.txt', 'traininglabels.txt')
    #Extract the images & labels
    datapoints = fp.getDataPoints()
    
    #Print out the 2d arrays with their corresponding labels
    for point in datapoints:
        for line in point.x:
            print(line)
        print(point.y)
    
    #for line in fp.x[1]:
        #print(line)
    
    #for image in fp.x:
        #for line in image:
            #print(line)
        #print("**********************************************************************************************************************************")
        
        
                       
                    
                    