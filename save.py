import os
import signal
import time 
from subprocess import check_output

# Get all of the PID's of a running process
def get_pid(name):
    return list(map(int,check_output(["pidof",name]).split()))

# Kill the process based on all of the process ID's. Use SIGTERM to cleanly exit the processes.
def kill_pid(pid):
    #Cycle through all of the PID's and kill all of them individually.
    for i in range(len(pid)):
        os.kill(pid[i], signal.SIGTERM)

# Include some way of sending out a key press. I'd prefer to do this with a default library, but if I really need to I'm cool having a library auto-install itself.
# def key_input():
#    try:
#        import 

def countdown(time):
    while time:
        # Convert time form minutes into seconds (60 seconds in 1 minute)
        time *= 60

        # Break up time into minutes and seconds (to be displayed later)
        mins, secs = divmod(time, 60)

        # Format time into minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)

        # Print out minutes and seconds in "minutes:seconds" format
        print(timer, end="\r")

        # Count down as time goes on
        time -= 1

    print("Time's up!")

#------------------------------------------------------------------------------------------

# Execution:

# Save the output of get_pid() to a variable, to be used elsewhere
global_pid = get_pid("steam")

# Be sure that we have some output for the pid.
print(global_pid)

# Get the total play time in minutes (This will be converted into seconds later on)
time_limit = input("Enter the time limit for the play session (in minutes): ")

# Start the countdown timer with the time limit variable
countdown(int(time_limit))

# After the timer is done, kill the process
kill_pid(global_pid)
