#Provides the logic for the terminal commands
import os
import subprocess
import sys

current_dir = "."

def folder(name):
    os.makedirs(name, exist_ok=True)

def cd(name):
    global current_dir
    if name == "..":
        current_dir = os.path.dirname(current_dir)
    else:
        new_path = os.path.join(current_dir, name)
        if os.path.exists(new_path):
            current_dir = new_path

def touch(name):
    file_path = os.path.join(current_dir, name + ".txt")
    open(file_path, 'w').close()

def ls():
    files = os.listdir(current_dir)
    for f in files:
        print(f)

def rm(name):
    path = os.path.join(current_dir, name)
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        os.rmdir(path)

def nano(name):
    file_path = os.path.join(current_dir, name)
    if not name.endswith('.txt'):
        file_path += '.txt'
    
    # Create file if it doesn't exist
    if not os.path.exists(file_path):
        open(file_path, 'w').close()
    
    # Open with system default editor
    if sys.platform == "win32":
        os.startfile(file_path)
    elif sys.platform == "darwin":  # macOS
        subprocess.call(["open", file_path])
    else:  # Linux
        subprocess.call(["xdg-open", file_path])

# Interactive terminal
while True:
    command = input("$ ").split()
    
    if not command:
        continue
        
    if command[0] == "folder":
        folder(command[1])
    elif command[0] == "open":
        cd(command[1])
    elif command[0] == "create":
        touch(command[1])
    elif command[0] == "list":
        ls()
    elif command[0] == "remove":
        rm(command[1])
    elif command[0] == "edit":
        nano(command[1])
    elif command[0] == "exit":
        break
##I decided to keep the logic of what I am used to in linux but change the command names for a bit more clarity
##Especially in this note taking environment, I want it to be its own thing, even if I am borrowing concepts form elsewhere. 