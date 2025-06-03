import os

def createFileInDir(folderPath, fileName, content=""):
    folder_path = os.path.join(folderPath, 'models')
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, fileName)
    with open(file_path, 'w') as f:
        f.write(content)