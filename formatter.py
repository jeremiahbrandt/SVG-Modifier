import os
import configparser

ORIGINAL_FILES_DIRECTORY="./original-files"
NEW_FILES_DIRECTORY="./new-files"

originalFiles=os.listdir(ORIGINAL_FILES_DIRECTORY)
config=configparser.ConfigParser()
config.read("config.ini")

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

    def toHTML(self):
        return self.name+"=\""+self.value+"\""

class HTMLTag:
    def __init__(self, html):
        self.isSelfClosing=html.find("><") == -1

        self.name=html.split(" ")[0][1:]
        self.createTagProperties(html)

        if self.isSelfClosing:
            pass
        else:
            self.createTagBody(html)


    def createTagProperties(self, html):
        self.tagProperties=[]
        if(self.isSelfClosing):
            rawProps = f'{html.split("/>")[0][len(self.name)+2:-1]}"'.split("=")
        else:
            rawProps = f'{html.split("><")[0][len(self.name)+2:-1]}"'.split("=")
        for i in range(len(rawProps)-1):
            name=rawProps[i].split(" ")[-1]
            nextItem=rawProps[i+1]
            tag=nextItem[:find_nth(nextItem, '\"', 2)]+"\""
            self.tagProperties.append(HTMLProperty(f"{name}={tag[1:-1]}"))

    def createTagBody(self, html):
        tags=html.split(">")
        self.body=[]
        body=tags[1:-2]
        for i in range(len(body)):
            body[i]=f"{body[i]}>"
        for tag in body:
            self.body.append(HTMLTag(tag))

    def toHTML(self):
        htmlString=f"<{self.name}"

        for prop in self.tagProperties:
            htmlString=f"{htmlString} {prop.toHTML()}"

        if self.isSelfClosing:
            htmlString=f"{htmlString} />"
        else:
            htmlString=f"{htmlString}>"
            for tag in self.body:
                htmlString=f"{htmlString}{tag.toHTML()}"

            htmlString=f"{htmlString}</{self.name}>"
        return htmlString

def applySVGChanges(SVGtag, color):
    # Change viewbox of SVG
    for i in range(len(SVGtag.tagProperties)):
        if(SVGtag.tagProperties[i].name=="viewBox"):
            SVGtag.tagProperties.pop(i)
            break

    SVGtag.tagProperties.append(HTMLProperty("viewBox=0 0 40 40"))

    # Remove width & height from SVG
    for i in range(len(SVGtag.tagProperties)):
        if(SVGtag.tagProperties[i].name=="width"):
            SVGtag.tagProperties.pop(i)      
            break
    for i in range(len(SVGtag.tagProperties)):
        if(SVGtag.tagProperties[i].name=="height"):
            SVGtag.tagProperties.pop(i)      
            break

    # Add rect
    SVGtag.body.insert(0, HTMLTag(f'<rect fill= {color} x="0" y="0" width="40" height="40" rx="15"  ry="15"/>'))

    # Add translate & fill properties to path
    for i in range(len(SVGtag.body)):
        currTag=SVGtag.body[i]
        if currTag.name == "path":
            currTag.tagProperties.append(HTMLProperty('transform=translate(7, 7)'))
            currTag.tagProperties.append(HTMLProperty('fill=white'))

    # Return modified SVG
    return SVGtag

for eachFile in originalFiles:
    f=open(f"{ORIGINAL_FILES_DIRECTORY}/{eachFile}", "r")
    mySVG=HTMLTag(f.readline())

    color=config["Rectangle_Fills"][eachFile]
    myNewSvg=applySVGChanges(mySVG, color)

    # Export SVG
    if not os.path.exists(NEW_FILES_DIRECTORY):
        os.makedirs(NEW_FILES_DIRECTORY)

    nf = open(f"{NEW_FILES_DIRECTORY}/{eachFile}", "w")
    nf.write(myNewSvg.toHTML())