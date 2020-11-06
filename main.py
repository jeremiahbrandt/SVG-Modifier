import os
import configparser

from Tag import HTMLTag
from MySVGFilter import applySVGChanges

ORIGINAL_FILES_DIRECTORY="./original-files"
NEW_FILES_DIRECTORY="./new-files"
DEFAULT_COLOR="black"

originalFiles=os.listdir(ORIGINAL_FILES_DIRECTORY)
config=configparser.ConfigParser()
config.read("config.ini")

for eachFile in originalFiles:
    f=open(f"{ORIGINAL_FILES_DIRECTORY}/{eachFile}", "r")
    mySVG=HTMLTag(f.readline())

    color=DEFAULT_COLOR
    if eachFile in config["Rectangle_Fills"]:
        color=config["Rectangle_Fills"][eachFile]
    myNewSvg=applySVGChanges(mySVG, color)

    # Export SVG
    if not os.path.exists(NEW_FILES_DIRECTORY):
        os.makedirs(NEW_FILES_DIRECTORY)

    nf = open(f"{NEW_FILES_DIRECTORY}/{eachFile}", "w")
    nf.write(myNewSvg.toHTML())