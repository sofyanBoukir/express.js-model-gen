import os

def createFileInDir(folderPath):
    folder_path = os.path.join(folderPath, 'models')
    os.makedirs(folder_path, exist_ok=True)
    return folder_path