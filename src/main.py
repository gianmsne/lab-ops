from sense_hat import SenseHat
import time

sense = SenseHat()


def blank(self):

        W = (255,255,255) # white

        blank = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        ]
        return blank

def main():

    sense.low_light = True
    sense.set_pixels(blank())

    while True:
        events = sense.stick.get_events()

        for event in events:
            if event.action == "pressed":
                print("pressed")
 
                if event.direction == "left":
                    print("left")

                elif event.direction == "right":
                    print("right") 

                elif event.direction == "middle":
                    print("middle") 

                elif event.direction == "up":
                    print("up") 

                elif event.direction == "down":
                    print("down") 

        time.sleep(0.01)

main()