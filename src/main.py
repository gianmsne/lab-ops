from sense_hat import SenseHat
import time

sense = SenseHat()

def main():

    sense.low_light = True

    while True:
        events = sense.stick.get_events()
        current_time = time.time()

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