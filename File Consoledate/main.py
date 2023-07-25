import os
from file_manager import FileManager
from logger import logging, log_exception

@log_exception
def main():
    target_folder_path = os.path.join("target_folder")
    source_folders_list = [
        os.path.join("data", "folder1"),
        os.path.join("data", "folder2"),
        os.path.join("data", "folder3"),
         # More folders can be added if needed 
    ]

    file_manager = FileManager(target_folder_path)
    file_manager.consolidate_files(source_folders_list)

if __name__ == "__main__":
    main()
