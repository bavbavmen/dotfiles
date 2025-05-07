#!/bin/python3
import subprocess

def attach_or_create_tmux(session_name="bob3"):
    # Check if the session exists
    result = subprocess.run(["tmux", "has-session", "-t", session_name], capture_output=True)
    
    if result.returncode == 0:
        # Session exists, create a new window and attach
        subprocess.run(["tmux", "new-window", "-t", session_name])
        subprocess.run(["tmux", "attach-session", "-t", session_name])
    else:
        # Session does not exist, create and enter it
        subprocess.run(["tmux", "new-session", "-s", session_name])

if __name__ == "__main__":
    attach_or_create_tmux()
