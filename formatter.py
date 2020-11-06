import os

ORIGINAL_FILES_DIRECTORY="./original-files"

originalFiles=os.listdir(ORIGINAL_FILES_DIRECTORY)

class HTMLTag:
    def __init__(self, html):
        self.isSelfClosing=html.find("><") == -1

        self.name=html.split(" ")[0][1:]

        if self.isSelfClosing:
            pass
        else:
            tags=html.split(">")
            self.openingTag=f"{tags[0]}>"
            self.closingTag=f"{tags[-2]}>"
            self.body=[]
            body=tags[1:-2]
            for i in range(len(body)):
                body[i]=f"{body[i]}>"
            for tag in body:
                self.body.append(HTMLTag(tag))


f=open(f"{ORIGINAL_FILES_DIRECTORY}/{originalFiles[0]}", "r")
mySVG=HTMLTag(f.readline())
print(mySVG.body[0].name)