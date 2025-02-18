import os
import shutil
import time
import logging
import yaml
import argparse
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from concurrent.futures import ThreadPoolExecutor

source_dir = "/users/hassan/Downloads"
dest_dirs = {
    "pdf": "/users/hassan/Hassan's Resumes",
    "docx": "/users/hassan/Other Documents",
    "jpg": "/users/hassan/Downloads/Pictures",
    "jpeg": "/users/hassan/Downloads/Pictures",
    "png": "/users/hassan/Downloads/Pictures",
    "mp4": "/users/hassan/Downloads/Videos",
    "mov": "/users/hassan/Downloads/Videos"
}

def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

config = load_config()
source_dir = config["source_dir"]
dest_dirs = config["dest_dirs"]

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

executor = ThreadPoolExecutor(max_workers=5)

def makeUnique(path):
    base, ext = os.path.splitext(path)
    counter = 1
    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base} ({counter}){ext}"
        counter += 1
    return new_path


def move(dest, entry, name):
    file_exists = os.path.exsits(dest + "/" + name )
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry,dest)


class MoverHandler(LoggingEventHandler):
  def move(dest, entry, name):
    dest_path = os.path.join(dest, name)
    
    if os.path.exists(dest_path):
        dest_path = makeUnique(dest_path)

    shutil.move(entry.path, dest_path)
        
                
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
def parse_arguments():
    parser = argparse.ArgumentParser(description="Automatically organize files into designated folders.")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to config file")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    
    observer = Observer()
    event_handler = MoverHandler()
    observer.schedule(event_handler, source_dir, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
