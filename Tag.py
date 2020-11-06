from TagProperty import HTMLProperty

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

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
