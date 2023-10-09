# Description: This is the main file for the project. It starts two processes, one for the GUI and one for the noise
# presentation. The GUI is implemented using tkinter and the noise presentation is implemented using pyglet.
# Author: Marvin Seifert

from multiprocessing import Process, Queue, Lock
from main_gui import tkinter_app
from play_noise import pyglet_app_lead, pyglet_app_follow



# Configuration dictionary for the pyglet app window. Change according to your needs.
config_dict = {
    "y_shift": 0,
    "x_shift": 2560,
    "gl_version": (4, 1),
    "window_size": (500, 500),
    "fullscreen": False}



# Start the GUI and the noise presentation in separate processes
if __name__ == '__main__':
    queue1 = Queue() # Queue for communication between the processes
    #queue2 = Queue()

    sync_queue = Queue()
    queue_lock = Lock()
    p1 = Process(target=tkinter_app, args=(queue1,queue_lock)) # Start the GUI
    p2 = Process(target=pyglet_app_lead, args=(config_dict, queue1,sync_queue,queue_lock)) # Start the pyglet app
    p3 = Process(target=pyglet_app_follow, args=(config_dict, queue1,sync_queue,queue_lock))  # Start the pyglet app
    p4 = Process(target=pyglet_app_follow, args=(config_dict, queue1, sync_queue, queue_lock))  # Start the pyglet app

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()
    p3.join()
    p4.join()
