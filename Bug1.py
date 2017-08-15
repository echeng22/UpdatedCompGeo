import numpy as np
import cv2

class Bug1:
    def __init__(self, name, radius, init_position, goal, K, dt, passive, color):
        self.name = name
        self.radius = radius
        self.init_position_x = init_position[0]
        self.init_position_y = init_position[1]
        self.currentPosition_x = init_position[0]
        self.currentPosition_y = init_position[1]
        self.pixel_x = self.currentPosition_x
        self.pixel_y = self.currentPosition_y
        self.goal_x = goal[0]
        self.goal_y = goal[1]
        self.x_desired = self.goal_x
        self.y_desired = self.goal_y
        self.velocity_x = 0
        self.velocity_y = 0
        self.DT = dt
        self.color = color
        self.K = K
        self.possibleCollisions = []
        self.passive = passive

    def getName(self):
        return self.name

    def getPosition(self):
        return (self.currentPosition_x,self.currentPosition_y)

    def drawInitPos(self, canvas):
        cv2.circle(canvas, (self.init_position_x, self.init_position_y), 2, (0,0,0), -1)

    def drawGoal(self, canvas):
        cv2.circle(canvas, (self.goal_x, self.goal_y), 2, (125, 125, 125), -1)

    def drawDesired(self, canvas):
        cv2.circle(canvas, (self.goal_x, self.goal_y), 3, self.color, -1)

    def getRadius(self):
        return self.radius

    def getGoal(self):
        return [self.goal_x, self.goal_y]

    def getVelocity(self):
        return (self.velocity_x, self.velocity_y)

    def setPosition(self, newPosition):
        self.currentPosition_x = newPosition[0]
        self.currentPosition_y = newPosition[1]

    def setVelocity(self):
        print "SPEED -1-1-1-1--1-1-1-1-1--1-1-1-1-"
        self.velocity_x = self.K * (self.x_desired - self.currentPosition_x)
        self.velocity_y = self.K * (self.y_desired - self.currentPosition_y)
        print self.velocity_x
        print self.velocity_y
        print "SPEED END - - - - - - - -- - - - - -"

    def calculateVelocity(self, fx, fy):
        return (self.K * (self.goal_x - fx),self.K * (self.goal_y - fy))

    def drawBug(self, canvas):
        cv2.circle(canvas, (self.pixel_x, self.pixel_y), self.radius, self.color, -1)


    def checkCollisions(self, bugList):
        collisionCheck = []
        if not self.passive:
            print ""
            print "self: "
            print self.getName()
            robot1 = self
            pos1 = np.asarray(robot1.getPosition())
            print pos1
            print ""
            for bug in bugList:
                print bug.getName()
                if(bug != self):
                    robot2 = bug
                    print "buffer: "
                    print robot1.getRadius() + robot2.getRadius() + 30
                    pos2 = np.asarray(robot2.getPosition())
                    print "pos2: "
                    print pos2
                    distance = np.linalg.norm(np.asarray(pos1)-np.asarray(pos2))
                    print "distance: "
                    print distance
                    if distance < (robot1.getRadius() + robot2.getRadius() + 30):
                        print "----------------------------------------------------------------------"
                        collisionCheck.append([robot1, robot2])
        self.possibleCollisions = collisionCheck



    def step(self, collisionList):
            if not self.passive:

                self.setVelocity()
                self.currentPosition_x = self.currentPosition_x + self.velocity_x * self.DT
                self.currentPosition_y = self.currentPosition_y + self.velocity_y * self.DT
                self.pixel_x = int(np.around(self.currentPosition_x))
                self.pixel_y = int(np.around(self.currentPosition_y))
            else:
                self.setVelocity()
                # self.currentPosition_x = int(np.around(self.currentPosition_x + self.velocity_x*self.DT))
                # self.currentPosition_y = int(np.around(self.currentPosition_y + self.velocity_y*self.DT))
                self.currentPosition_x = self.currentPosition_x + self.velocity_x * self.DT
                self.currentPosition_y = self.currentPosition_y + self.velocity_y*self.DT
                self.pixel_x = int(np.around(self.currentPosition_x))
                self.pixel_y = int(np.around(self.currentPosition_y))
            print "FINAL POSITION------------------------------------"
            print self.currentPosition_x
            print self.currentPosition_y

