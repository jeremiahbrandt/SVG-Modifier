from TagProperty import HTMLProperty
from Tag import HTMLTag

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
            currTag.tagProperties.append(HTMLProperty('transform=translate(8, 8)'))
            currTag.tagProperties.append(HTMLProperty('fill=white'))

    # Return modified SVG
    return SVGtag