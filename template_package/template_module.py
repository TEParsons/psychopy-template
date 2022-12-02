class TemplateClass:
    clsAttrib = None

    def __init__(self, compulsoryAttrib, optionalAttrib=None):
        self.compulsoryAttrib = compulsoryAttrib
        self.optionalAttrib = optionalAttrib

    def someFunction(input1, input2, namedInput=None):
        return input1, input2, namedInput