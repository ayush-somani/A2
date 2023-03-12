import os
import shutil
import multiprocessing as mp
import socket 
import uuid

num_replicas = 5

class KeyValueStore:
    def __init__(self, storage_path):
        self.path = storage_path
        self.store = {}
        self.counter = {}
    
    def _get_filename(self, key, counter):
        return os.path.join(self.path, f'{key}_{counter}.txt')

    def write(self, key, name, value):
        if key is None:
            key = str(uuid.uuid4())
        # Get counter for this key
        counter = self.counters.get(key, 0) + 1
        file_name = self._get_filename(key, counter)

        # Write data to file
        with open(file_name, 'w') as f:
            f.write(name+'\t'+value+'\n')
        
        # Add Key-Value to dictionary
        self.store[key] = file_name
        return key
    
    def read(self, key):
        # Get latest version of file for the given key 
        counter = self.counters.get(key, 0)
        file_name = self._get_filename(key, counter)

        if not os.path.exists(file_name):
            print("!!!! File doesn't exists !!!!")
            return None
        
        with open(file_name, 'r') as f:
            for line in f:
                name, value = line.strip().split('\t')
                return name, value
    
    def delete(self, key):
        # Remove all versions of file for the given key
        for counter in range(1, self.counter.get(key, 0)+1):
            file_name = self._get_filename(key, counter)
            if os.path.exists(file_name):
                os.remove(file_name)

def process_start(process_id, folder_path):
    """
    The process function that each process will execute.
    """

    print(f"Starting process {process_id}.....")

    # Get a ip and unique port number for this process
    ip, port = get_free_port().getsockname()

    # Each process has access to its own dedicated folder path
    process_folder_path = os.path.join(folder_path, f"replica_{process_id}")
    os.makedirs(process_folder_path)

    # Each process has access to its own dedicated KV data store
    process_data_store = KeyValueStore(process_folder_path)

def get_free_port():
    """
    Returns a free port number on localhost.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 0))
        return s

if __name__ == '__main__':

    #Create a folder to hold each server data
    folder_path = "/Users/ayushsomani/Desktop/A2"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

    # Create and start the worker processes
    replicas = []
    for i in range(num_replicas):
        process = mp.Process(target=process_start, args=(i, folder_path))
        process.start()
        replicas.append(process)

    # Wait for all the worker processes to finish
    for process in replicas:
        process.join()
