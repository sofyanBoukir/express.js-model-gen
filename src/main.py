from cli import askForLanguage,askForModelNames,askForAttributes
from developer import developer
from ai import askAi
import os
import sys
from resultPath import createFileInDir

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.paths import askForPath

developer()

language = askForLanguage()
modelNames = askForModelNames()
modelAttributes = askForAttributes(modelNames)

if(len(modelNames) == 0):
    print('BYEE!!!')
    exit()

path = askForPath()
folderToStoreResults = createFileInDir(path)

languages = {
    'javascript' : 'js',
    'typescript' : 'ts',
}

for modelAttr, modelName in zip(modelAttributes, modelNames):
    print('Asking ai.....')
    response = askAi(language, modelAttr)

    file_path = os.path.join(folderToStoreResults, f"{modelName}.model.{languages[language.lower()]}")
    with open(file_path, 'w') as f:
        f.write(response)
