from cli import askForLanguage,askForModelNames,askForAttributes
from developer import developer
from ai import askAi
import os
import sys

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
print('your path provided is: ',path)

for modelAttr, modelName in zip(modelAttributes, modelNames):
    # response = askAi(language, modelAttr, modelName)
    print(f"{modelName=}, {modelAttr=}")

# for modelAttr in modelAttributes:
#     # response = askAi(language,modelAttr)
#     # print(response)