import os
import signal
import time
import pyautogui
from subprocess import check_output

# Get all of the PID's of a running process
def get_pid(name):
    # Save all of the PID's into a variable, so I can verify that it is not null
    pid_list = list(map(int,check_output(["pidof",name]).split()))

    # Check if pid_list is null or not
    if len(pid_list) == 0:
        print('Process' + name + 'does not seem to be running')
        quit()

    else:
        return pid_list

# Kill the process based on all of the process ID's. Use SIGTERM to cleanly exit the processes.
def kill_pid(pid):
    #Cycle through all of the PID's and kill all of them individually.
    for i in range(len(pid)):
        os.kill(pid[i], signal.SIGTERM)

# Include some way of sending out a key press. I'd prefer to do this with a default library, but if I really need to I'm cool having a library auto-install itself.
def key_input():
    pyautogui.press('f5')

def countdown(t):

    # Convert time form minutes into seconds (60 seconds in 1 minute)
    t *= 60

    while t:
        # Break up time into minutes and seconds (to be displayed later)
        mins, secs = divmod(t, 60)

        # Format time into minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)

        # Print out minutes and seconds in "minutes:seconds" format
        print(timer, end="\r")

        time.sleep(1)

        # Count down as time goes on
        t -= 1

    print("Time's up!")

#------------------------------------------------------------------------------------------

# Execution:

# Name of the PID (to be used later
pid = "steam"

# Save the output of get_pid() to a variable, to be used elsewhere
global_pid = get_pid(pid)

# Be sure that we have some output for the pid.
print(global_pid)

# Get the total play time in minutes (This will be converted into seconds later on)
time_limit = input("Enter the time limit for the play session (in minutes): ")

# Start the countdown timer with the time limit variable
countdown(int(time_limit))

# Press the 'save' key (NOTE: f5 is the default save key for Fallout: New Vegas. In order to use this script for other games, this will have to be changed or commented out.)
# key_input()

# Wait 1 minute for the game to properly save the game, so as not to corrupt a save (NOTE: From my experimentation, this is fine for my config. However, New Vegas seems to be held together by spit and frayed duct tape at time of writing on other OS's, from what I understand. As such, this approach of saving the game, waiting a bit, and then killing it outright rather than properly waiting may not work for some.)
print('Waiting a bit to properly save game')
countdown(int(1))

# After the timer is done, and the game has (hopefully) properly saved itself, kill the entire game based on the PID.
kill_pid(global_pid)
