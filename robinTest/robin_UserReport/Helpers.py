
def getClassColorForValue(inputValue, lowLimit, highLimit):
    # these are implemented in CSS
    if(lowLimit > inputValue):
        return "redText"
    if(highLimit < inputValue):
        return "greenText"
    return "blackText" # nothing extraordinary happened..