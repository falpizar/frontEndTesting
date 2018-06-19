def getClassColorForValue(inputValue, lowLimit, highLimit):
    # these are implemented in CSS
    if(lowLimit > inputValue):
        return "redText"
    if(highLimit < inputValue):
        return "greenText"
    return "blackText" # nothing extraordinary happened..
def getFormatColumn(inputValue, columnSize, divId):
    #based on Bootstrap classes
    return "<div id=\"{}\" class=\"col-sm-{}\">{}</div>".format(divId, columnSize, inputValue)
def getPlusButton(buttonId):
    return "<plusButton id=\"{}\" class=\"glyphicon glyphicon-plus-sign\"/>".format(buttonId)