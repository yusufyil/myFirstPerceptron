import pygame
import time
import random
random.seed(0)
pygame.init()
height=640
width=640
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("ML<3")
#colorss
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
#colorss
FPS=60

class perceptron:
    def __init__(self, learningRate):
        self.w0 = random.random()
        self.w1 = random.random()
        self.bias = random.random()
        self.learningRate = learningRate
    def predict(self,x0,x1):
        sum = self.w0 * x0 + self.w1 * x1 + self.bias
        if sum >= 1:
            return 1
        else:
            return -1
    def makePredictionList(self, x0List, x1List, sampleNum):
        pList = []
        for i in range(sampleNum):
            pList.append(self.predict(x0List[i],x1List[i]))
        return pList

    def train(self, x0, x1, output):
        """x0 and x1 inputs should be come from x0list and x1list whereas output value should come from ylist"""
        prediction = self.predict(x0, x1)
        self.w0 = self.w0 + (output - prediction) * x0 * self.learningRate
        self.w1 = self.w1 + (output - prediction) * x1 * self.learningRate
        self.bias = self.bias + (output - prediction) * self.learningRate * 640
    def showAcc(self, x0List, x1List, yList, sampleNum):
        hit = 0
        for i in range(sampleNum):
            if self.predict(x0List[i], x1List[i]) == yList[i]:
               hit = hit + 1
        print("Accuracy = {}".format(hit/sampleNum))

class sample:
    def __init__(self, sampleNum, x0Range, x1Range):
        self.sampleNum = sampleNum
        self.x0List = []
        self.x1List = []
        self.yList = []
        self.x0Range = x0Range
        self.x1Range = x1Range
        #initializing samples to the lists
        self.initializeSample()
    def initializeSample(self):
        for i in range(self.sampleNum):
            self.x0List.append((random.random() - 0.5) * self.x0Range)
            self.x1List.append((random.random() - 0.5) * self.x1Range)
            if self.x0List[i] >= self.x1List[i] - self.x0Range / 2:
                self.yList.append(1)
            else:
                self.yList.append(-1)
class coordinate:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
    def drawCoordinats(self):
        #drawing y axis
        pygame.draw.line(self.screen,WHITE,self.convertCoord(0,self.height/2),self.convertCoord(0,-self.height/2),1)
        pygame.draw.line(self.screen,WHITE,self.convertCoord(-self.width/2,0),self.convertCoord(self.width/2,0),1)

    def convertCoord(self,x, y):
        newX = x + self.width/2
        newY = self.height/2 - y
        return [newX, newY]
    def drawSamples(self,x0List, x1List, predictionList, yList, sampleNum):
        """xList yList and result should be list and the rest is just numbers"""
        for i in range(sampleNum):
            if predictionList[i] == 1:
                pygame.draw.circle(self.screen,GREEN,self.convertCoord(x0List[i],x1List[i]),5,2)
                if predictionList[i] == yList[i]:
                    pygame.draw.circle(self.screen, WHITE, self.convertCoord(x0List[i], x1List[i]), 2, 2)
                else:
                    pygame.draw.circle(self.screen, RED, self.convertCoord(x0List[i], x1List[i]), 2, 2)
            else:
                pygame.draw.circle(self.screen, BLUE, self.convertCoord(x0List[i], x1List[i]), 5, 2)
                if predictionList[i] == yList[i]:
                    pygame.draw.circle(self.screen, WHITE, self.convertCoord(x0List[i], x1List[i]), 2, 2)
                else:
                    pygame.draw.circle(self.screen, RED, self.convertCoord(x0List[i], x1List[i]), 2, 2)




lRate = 0.000001
sNum= 1000
p1 = perceptron(lRate)
s1 = sample(sNum,width,height)
c1 = coordinate(screen,width,height)

def main():
    run=True
    epoch = 0
    clock=pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        screen.fill((BLACK))
        """pygame.draw.circle(screen,BLUE,[width//2,height//2],100,0,)
        pygame.draw.line(screen, (0,255,255),(-4,-4),(360,360),9)"""
        c1.drawCoordinats()
        c1.drawSamples(s1.x0List,s1.x1List,p1.makePredictionList(s1.x0List,s1.x1List,sNum),s1.yList,sNum)
        p1.train(s1.x0List[epoch], s1.x1List[epoch], s1.yList[epoch])
        epoch = (epoch + 1) % sNum
        print(p1.w0, p1.w1, p1.bias)
        #time.sleep(1)
        pygame.display.update()

    pygame.quit()
if __name__ == "__main__":
    main()