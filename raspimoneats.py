from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) #blank
w = (255, 255, 255) #white 
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen
r = (255, 0, 0) #red

class Game:
    def __init__(self):
        self.raspimon_x = 0
        self.raspimon_y = 0

        sense.set_pixel(self.raspimon_x, self.raspimon_y, w)

        self.food_x = 6
        self.food_y = 6

        sense.set_pixel(self.food_x, self.food_y, r)

        self.is_hungry = True

        self.score = 0

    def down(self):
        global raspimon_y
        if self.raspimon_y < 7:
           self.raspimon_y += 1
           print("y: " + str(self.raspimon_y))
           self.update()

    def up(self):
        global raspimon_y
        if self.raspimon_y > 0:
           self.raspimon_y -= 1
           print("y: " + str(self.raspimon_y))
           self.update()

    def left(self):
        global raspimon_x
        if self.raspimon_x > 0:
           self.raspimon_x -= 1
           print("x: " + str(self.raspimon_x))
           self.update()

    def right(self):
        global raspimon_x
        if self.raspimon_x < 7:
           self.raspimon_x += 1
           print("x: " + str(self.raspimon_x))
           self.update()

    def update(self):
        global raspimon_x, raspimon_y
        sense.clear()
        sense.set_pixel(self.raspimon_x, self.raspimon_y, d)
        sense.set_pixel(self.food_x, self.food_y, c)
        print("Updation completed")
    
    def reset(self):
        sense.clear()
        self.raspimon_x = random.randint(0,7)
        self.raspimon_y = random.randint(0,7)
        same_spot = True
        while same_spot:
            self.food_x = random.randint(0,7)
            self.food_y = random.randint(0,7)
            if self.raspimon_x != self.food_x and self.raspimon_y != self.food_y:
                same_spot = False
                break
        sense.set_pixel(self.raspimon_x, self.raspimon_y, d)
        sense.set_pixel(self.food_x, self.food_y, c)
        print("Reset completed")

    def run(self):
        self.update()
        while self.is_hungry:
            for event in sense.stick.get_events():    
                if event.direction == "down" and event.action == "released":
                    self.down()
                if event.direction == "up" and event.action == "released":
                    self.up()
                if event.direction == "left" and event.action == "released":
                    self.left()
                if event.direction == "right" and event.action == "released":
                    self.right()
                if self.raspimon_x == self.food_x and self.raspimon_y == self.food_y:
                    self.score += 1
                    if self.score < 10:
                        sense.show_letter(str(self.score))
                        time.sleep(.25)
                        self.reset()
                    else:
                        sense.show_message("Game Over...")
                        break

# my_game = Game()
# my_game.run()