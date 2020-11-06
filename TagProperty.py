class HTMLProperty:
    def __init__(self, tag):
        vals=tag.split("=")
        self.name=vals[0]
        self.value=vals[1]

    def toHTML(self):
        return self.name+"=\""+self.value+"\""