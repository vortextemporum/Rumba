import random
from moviepy.editor import *

class Grid():
    '''
YO YO YO YO YO YO YO YO YO YO YO
    '''
    def __init__(self, x=0, y=0, addToList=True, direction=0):

        self.addToList = addToList
        self.x = x
        self.y = y
        self.startx = x
        self.starty = y
        
        self.directionList = ["moveRight", "moveDownRight", "moveDown", "moveDownLeft", "moveLeft", "moveUpLeft", "moveUp", "moveUpRight"]
        self.directionIndex = direction
        
        self.currentDirection = self.directionList[self.directionIndex]
        self.currentPosition = [self.x, self.y]
        
        if self.addToList:
            self.sequence = [[x,y]]
        else:
            self.sequence = [] 

        self.scaled_sequence = []


    def addPosition(self, x=1, y=1, addToList=True, direction=None):
        self.x = x
        self.y = y

        if direction.isnumeric():
            self.directionIndex = direction
        
        if self.addToList:
            self.sequence.append([self.x,self.y])
        
    def moveLeft(self, steps=1, jump=1):
        for i in range(steps):
            self.x = self.x - jump
            self.sequence.append([self.x,self.y])
        # return [self.x,self.y]
    
    def moveRight(self, steps=1, jump=1):
        for i in range(steps):
            self.x = self.x + jump
            self.sequence.append([self.x,self.y])
        # return [self.x,self.y]
    
    def moveUp(self, steps=1, jump=1):
        for i in range(steps):
            self.y = self.y - jump
            self.sequence.append([self.x,self.y])
        # return [self.x,self.y]
    
    def moveDown(self, steps=1, jump=1):
        for i in range(steps):   
            self.y = self.y + jump
            self.sequence.append([self.x,self.y])
        # return [self.x,self.y]

    def moveDownLeft(self, steps=1, jump=1):
        for i in range(steps):
            self.x = self.x - jump
            self.y = self.y + jump
            self.sequence.append([self.x,self.y])
        # return [self.x,self.y]
    
    def moveDownRight(self, steps=1, jump=1):
        for i in range(steps):
            self.x = self.x + jump
            self.y = self.y + jump
            self.sequence.append([self.x,self.y])
        # return [self.x,self.y]
    
    def moveUpLeft(self, steps=1, jump=1):
        for i in range(steps):
            self.x = self.x - jump
            self.y = self.y - jump
            self.sequence.append([self.x,self.y])
        # return [self.x,self.y]
    
    def moveUpRight(self, steps=1, jump=1):
        for i in range(steps):
            self.x = self.x + jump
            self.y = self.y - jump
            self.sequence.append([self.x,self.y])
        # return [self.x,self.y]
    
    
    def turn(self, direction=0, steps=1):
        
        '''
        Turns the agent regarding to the previous direction and moves. The current direction can be checked with currentDirection method.
        
        Example: 
        Grid.currentDirection  ==> "moveRight"
        Grid.turn(2,3) ==> Turns right, and walks for 3 steps.
        Grid.currentDirection ==> "moveDown"

        Hint:       
        0° =   + 0 -> Forward
        45° =  + 1 
        90° =  + 2 -> Right
        135° = + 3
        180° = + 4 -> Back
        225° = + 5
        270° = + 6 -> Left
        315° = + 7
        360° = + 8 -> Forward again
        '''
        # Question: Shall I change the name to move() ? 
        if steps <= 0:
            break

        self.directionIndex = (self.directionIndex + direction) % 8
        
        return getattr(self, self.directionList[self.directionIndex])(steps)
    
    # MIRRORS
    
    
    def mirrorX(self,row):
        self.x = row - 1 - self.x
        # return [self.x,self.y]
    
    def mirrorY(self,row):
        self.y = row - 1 - self.y
        # return [self.x,self.y]
    
    def mirror(self,row):
        self.x = row - 1 - self.x
        self.y = row - 1 - self.y
        # return [self.x,self.y]

    def swapXY(self):
        # Not Tested
        x = self.x
        y = self.y

        self.x = y
        self.y = x
        # Check if there is any need of such thing
        pass
    

    #SEQUENCE TRANSFORMATIONS


    def mirrorXAll(self, row):
        for couple in self.sequence:
            couple[0] = row - 1 - couple[0]
            couple[1] = couple[1]
       # return self.sequence
    
    def mirrorYAll(self, row):
        for couple in self.sequence:
            couple[0] = couple[0]
            couple[1] = row - 1 - couple[1]
       # return self.sequence
        
    def mirrorAll(self, row):
        for couple in self.sequence:
            couple[0] = row - 1 - couple[0]
            couple[1] = row - 1 - couple[1]
       # return self.sequence
    
    def reverse(self):
        self.sequence = self.sequence[::-1]
       # return self.sequence

    def swapXYAll(self):
         # Not Tested
        self.sequence = [(t[1], t[0]) for t in self.sequence]
        pass

    def moveAll(self, x=0, y=0):
         # Not Tested
        for couple in self.sequence:
            couple[0] = couple[0] + x
            couple[1] = couple[1] + y

    def shuffle(self):
         # Not Tested
        self.sequence = random.shuffle(self.sequence)
    
    def reset(self):

        # Resets everything

        self.x = self.startx
        self.y = self.starty
        
        if self.addToList:
            self.sequence = [[x,y]]
        else:
            self.sequence = []
        
        # print("resetted to:" + [self.startx,self.starty])
        return [self.x,self.y]

    def scaleToVideo(self, rows=1, resolution=[1280,720]):
        # Not tested
        self.video_resolution = resolution
        self.cell_x = float(self.resolution[0] / self.rows)
        self.cell_y = float(self.resolution[1] / self.rows)
        self.cell_size = [self.cell_x,self.cell_y]
        self.scaled_sequence = []

        for couple in self.sequence:
            position = [self.cell_x * couple[0], self.cell_y * couple[1]]
            self.scaled_sequence.append(position)
    
    def testPattern(output="", length = 1, offset=0.1):
        '''
        Won't work with doubleSpiral,
        '''
        # Not tested
        duration = offset * length
        start = 0.0
        clip = ColorClip(size=composition1.cell_size, color=(0,255,0), duration=duration)
        final_score = []

        for i in range(len(self.scaled_sequence)):
            final = clip.set_position(self.scaled_sequence[i]).set_start(start))
            final_score.append(final)
            start += offset

        finalvideo = CompositeVideoClip(final_score,self.video_resolution)
        finalvideo.fps= 30

        finalvideo.write_videofile(output)




''' 

PATTERNS START HERE

'''

def doubleSpiral(n):
    seq1 = Grid(x=-1, y=0, addToList=False, direction=0)
    seq2 = Grid(x=n, y=n-1,addToList=False, direction=4)
    
    seq1.turn(0,n)
    seq2.turn(0,n)
    
    d = n-2
    for i in range(n):
        for i in range(2):
            seq1.turn(2,d)
            seq2.turn(2,d)
        d -= 2
    return seq1.sequence, seq2.sequence

def Square(n, corner=4):
    # Not Tested
    seq = Grid(x=0,y=0,addToList=True,direction=6)
    
    for i in range(corner):
        seq.turn(2,n-1)
    
    return seq


def Spiral(n):
    # Not Tested
    seq = Grid(x=-1,y=0,addToList=False,direction=6)
    
    for newn in range(rows, 2, -2):
        seq.turn(2, newn)
        seq.turn(2, newn-1)
        seq.turn(2, newn-1)
        seq.turn(2, newn-2)
    
    if rows % 2 == 1:
        seq.turn(2,1)

    return seq

def Regular(n):
     # Not Tested
    seq = Grid(addToList=False)

    for column in range (n):
        for row in range(n):
            seq.addPosition(row,column)
    return seq

def Shuffle(n):
     # Not Tested
    return Regular(n).shuffle


def Karo(n):
     # Not Tested
    seq = Grid(x=int(n/2)-1, y=0, addToList=False, direction=7)
    
    if n % 2 == 0:
        for i in range(n/2-1, 0, -1):
            seq.turn(1,2)
            seq.turn(1,i)
            seq.turn(1,1)
            seq.turn(1,i)
            seq.turn(1,1)
            seq.turn(1,i)
            seq.turn(1,1)
            seq.turn(1,i-1)
    elif n % 2 == 1:
        for i in range(int(n/2),0,-1):
            seq.turn(1,1)
            seq.turn(1,i)
            seq.turn(1,i)
            if i != 1:
                seq.turn(1,i-1)
            else:
                seq.turn(1,i)
            seq.turn(3,1)

    return seq
        
def Z(n=5, corners = 3):
     # Not Tested
    seq = Grid(x=0,y=0,addToList=True,direction=5)

    for i in range(corners):
        if i % 4 == 0 or i % 4 == 1:
            seq.turn(3, n - 1)
        if i % 4 == 2 or i % 4 == 3: 
            seq.turn(5, n - 1)

    return seq

def Snake(n, repeat=1):
     # Not Tested
    seq = Grid(x=0,y=-1, addToList=False  direction=4)

    for i in range(repeat):
        for column in range(n):
            
            if i % 2 == 0:
                seq.turn(6,1)
                seq.turn(6,n-1)

            elif i % 2 == 1:
                seq.turn(2,1)
                seq.turn(2,n-1)

    return seq

'''
DRAW ALPHABET START
'''

def LetterB(n):

    pass


'''
DRAW ALPHABET END
'''