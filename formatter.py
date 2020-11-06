import os

ORIGINAL_FILES_DIRECTORY="./original-files"

originalFiles=os.listdir(ORIGINAL_FILES_DIRECTORY)

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

class HTMLProperty:
    def __init__(self, tag):
        vals=tag.split("=")
        self.name=vals[0]
        self.value=vals[1]

class HTMLTag:
    def __init__(self, html):
        self.isSelfClosing=html.find("><") == -1

        self.name=html.split(" ")[0][1:]
        self.createTagProperties(html)

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

    def createTagProperties(self, html):
        self.tagProperties=[]
        if(self.isSelfClosing):
            pass
        else:
            rawProps = f'{html.split("><")[0][len(self.name)+2:-1]}"'.split("=")
            for i in range(len(rawProps)-1):
                name=rawProps[i].split(" ")[-1]
                nextItem=rawProps[i+1]
                tag=nextItem[:find_nth(nextItem, '\"', 2)]+"\""
                self.tagProperties.append(HTMLProperty(f"{name}={tag}"))


f=open(f"{ORIGINAL_FILES_DIRECTORY}/{originalFiles[0]}", "r")
mySVG=HTMLTag(f.readline())
print(mySVG.tagProperties)