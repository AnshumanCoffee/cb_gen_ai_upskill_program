import os
import csv
import shutil
from datetime import datetime
from utils import get_unique_filename


class FileManager:
    def __init__(self, target_folder):
        self.target_folder = target_folder
        self.file_details_file = os.path.join("data", "file_details.csv")
        self.file_details = self._load_file_details()

    def _load_file_details(self):
        file_details = {}
        if os.path.exists(self.file_details_file):
            with open(self.file_details_file, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    file_details[row['File Name']] = {
                        'Source Folder': row['Source Folder'], 
                        'Date Added': row['Date Added'] 
                    }
        return file_details

    def _save_file_details(self, file_name, source_folder):
        with open(self.file_details_file, 'a', newline='') as csvfile:
            fieldnames = ['File Name', 'Source Folder', 'Date Added']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'File Name': file_name,
                'Source Folder': source_folder,
                'Date Added': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            })

    def consolidate_files(self, source_folders):
        if not os.path.exists(self.target_folder):
            os.makedirs(self.target_folder)

        for folder in source_folders:
            if not os.path.exists(folder):
                raise FileNotFoundError(f"Source folder '{folder}' not found.")
            
            for root, _, files in os.walk(folder):
                for file in files:
                    source_file = os.path.join(root, file)
                    if os.path.isfile(source_file):
                        target_file = os.path.join(self.target_folder, get_unique_filename(self.target_folder, file))
                        shutil.copy2(source_file, target_file)
                        self._save_file_details(file, folder)


if __name__ == "__main__":
    # For testing the File Manager class
    target_folder_path = os.path.join("target_folder")
    source_folders_list = [
        os.path.join("data", "folder1"),
        os.path.join("data", "folder2"),
        os.path.join("data", "folder3"),
        # More folders can be added if needed 
    ]

    file_manager = FileManager(target_folder_path)
    file_manager.consolidate_files(source_folders_list)
