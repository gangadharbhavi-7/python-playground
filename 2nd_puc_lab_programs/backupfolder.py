import os
import zipfile
def backup_folder(folder_path, backup_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
    else:
        with zipfile.ZipFile(backup_path, 'w',zipfile.ZIP_DEFLATED) as backup_zip:
            for foldername, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path=os.path.join(foldername, filename)
                    backup_zip.write(file_path, os.path.relpath(file_path, folder_path))

folder_path=input("Enter the path of the folder to backup: ")
backup_path=input("Enter the path of the backup zip file: ")
backup_folder(folder_path, backup_path)