from msilib.schema import File
import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/KaviNithin/Desktop/downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey,{event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops Someone deleted {event.src_path}")
    
    def on_modified(self, event):
        print(f"Yay! it looks that someone is modified {event.src_path}")
    
    def on_moved(self, event):
        print(f"Yay! it looks that someone moved {event.src_path} to {event.dest_path}")
        
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()