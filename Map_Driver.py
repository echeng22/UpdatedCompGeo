import cv2
import numpy as np
from Bug1 import Bug1
import time

class MapDriver:
    def __init__(self, bugList, worldsize, obstacleList, timeStep):
        self.bugList = bugList
        self.timeStep = timeStep
        self.mapCanvas = self.mapInit(worldsize)
        self.obsList = obstacleList

    def update(self, listCollision):
        listRobotPos = []
        for bug in self.bugList:
            bug.checkCollisions(self.bugList)
        for bug in self.bugList:
            bug.step()
        self.drawMap(self.bugList)

    def drawMap(self, bugList):
        for bug in bugList:
            bug.drawBug(self.mapCanvas)
            bug.drawInitPos(self.mapCanvas)
            bug.drawDesired(self.mapCanvas)
            bug.drawGoal(self.mapCanvas)
            print self.mapCanvas.shape
            cv2.imshow("Map", self.mapCanvas)
        cv2.waitKey(20)

    def checkBugPos(self):
        for bug in self.bugList:
            bugPos = bug.getPosition()
            bugGoal = bug.getGoal()
            distance = np.linalg.norm(np.asarray(bugPos) - np.asarray(bugGoal))
            if distance > 10:
                return False
        return True


    def mapClear(self):
        canvasSize = self.mapCanvas.shape
        clear = np.zeros((canvasSize[0], canvasSize[1], canvasSize[2]), np.uint8)
        clear[:] = (255, 255, 255)
        self.mapCanvas = clear

    @staticmethod
    def mapInit(worldsize):
        canvas = np.zeros((worldsize[0],worldsize[1], 3), np.uint8)
        canvas[:] = (255,255,255)
        return canvas

    # def checkCollisions(self):
    #     collisionCheck = []
    #     for i in range(len(self.bugList)-1):
    #         robot1 = self.bugList[i]
    #         pos1 = np.asarray(robot1.getPosition())
    #         for j in range(i+1, len(self.bugList)):
    #             robot2 = self.bugList[j]
    #             pos2 = np.asarray(robot2.getPosition())
    #             distance = np.linalg.norm(np.asarray(pos1)-np.asarray(pos2))
    #             if distance < (robot1.getRadius() + robot2.getRadius() + 30):
    #                 collisionCheck.append([robot1, robot2])
    #                 print robot1.getName()
    #                 print robot2.getName()
    #                 raw_input()
    #     return collisionCheck

def main():
    bug1 = Bug1('bug1', 10, [600, 200], [400, 600], .01, 1, False, (0, 255, 0))
    bug2 = Bug1('bug2', 10, [200, 600], [600, 600], .01, 1, True, (0, 0, 255))
    bug3 = Bug1('bug3', 10, [200, 200], [600, 600], .01, 1, True, (255, 0, 0))
    map = MapDriver([bug1, bug2, bug3], [1000, 1000], [], .1)
    time = 500
    t_count = 0
    # map = MapDriver([],[250,250],[],time/100)
    while not map.checkBugPos():
        print t_count
        # listCollision = []
        # listCollision = map.checkCollisions()
        # print ''
        # print listCollision
        map.update([])
        map.mapClear()
        t_count = t_count + 1


if __name__ == "__main__":
    main()