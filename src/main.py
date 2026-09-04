from sense_hat import SenseHat
from utils.matrix import blank, success, reject
from utils.ssh_handler import ssh
import time

sense = SenseHat()

HOLD_THRESHOLD = 3.0  # seconds
press_times = {}  
triggered = set() 

def main():
    sense.low_light = True
    sense.set_pixels(blank())

    press_start_time = None
    action_triggered = False

    while True:
        for event in sense.stick.get_events():
            # Start tracking when pressed
            if event.action == 'pressed':
                press_start_time = time.time()
                action_triggered = False  # Reset flag for new press
                
            # Stop tracking if released early
            elif event.action == 'released' and not action_triggered:
                press_start_time = None
                ssh()
                sense.set_pixels(blank())

        # Check if the button is currently being held
        if press_start_time is not None and not action_triggered:
            elapsed_time = time.time() - press_start_time
            
            # Send shutdown command
            if elapsed_time >= 3.0:
                print("Shutdown not implemented yet.")
                sense.set_pixels(blank())
                action_triggered = True 

        time.sleep(0.05)
        
if __name__ == "__main__":
    main()