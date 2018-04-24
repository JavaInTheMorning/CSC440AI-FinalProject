'''
Created on Apr 24, 2018

@author: danielfinlay
'''

class X:
    def __init__(self, x):
        self.x = x
    
    def tobyteArray(self):
        pass
    
    
class FileParser:
    def __init__(self, imagefile, labelfile):
        self.imagefile = imagefile
        self.labelfile = labelfile
        self.x = []
    
    def extractAllX(self, numOrFace):
        index = 1
        lines = []
        with open(self.imagefile, 'r',encoding="utf-8") as in_file:
            for line in in_file:
                lines.append(line)  
                index = index + 1
                
                if numOrFace is 'num':
                    if index is 28:
                        currentX = X(lines)
                        self.x.append(currentX.tobyteArray())
                        index = 1
                        lines = []
                elif numOrFace is 'face':
                    if index is 70:
                        currentX = X(lines)
                        self.x.append(currentX.tobyteArray())
                        index = 1
                        lines = []
                    
                    
                    