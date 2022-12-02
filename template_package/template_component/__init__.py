#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pathlib import Path
from psychopy.experiment.components import BaseComponent, Param, _translate, getInitVals
from psychopy import prefs


class TemplatePluginComponent(BaseComponent):
    """
    A template component which does absolutely nothing, purely exists to show you how to 
    add a component to a plugin.
    """
    targets = ['PsychoPy', 'PsychoJS']
    categories = ['Other']
    iconFile = Path(__file__).parent / 'unknownPlugin.png'
    tooltip = _translate('Template: A template component purely for instructional purposes.')

    def __init__(self, exp, parentName, name='', exampleParam=""):
        # Setup markers
        self.type = 'Template'
        # Initialise from parent class
        BaseComponent.__init__(self, exp, parentName, name=name)
    
    def writeInitCode(self, buff):
        """
        Code to initialise this component in Python experiments
        """
        # Get init values (substitutes values set each frame/repeat for reasonable starting values)
        inits = getInitVals(self.params, target="PsychoPy")
        # Write some code
        code = (
            "# Create %(name)s, just a dictionary with param values, to show you how to include param values\n"
            "%(name)s = {\n"
            "    'win': win,\n"
            "    'name': '%(name)s',\n"
            "    'exampleParam': %(exampleParam)s,\n"
            "}\n"
        )
        buff.writeIndentedLines(code % inits)
    
    def writeInitCodeJS(self, buff):
        """
        Code to initialise this component in JS experiments
        """
        # Get init values (substitutes values set each frame/repeat for reasonable starting values)
        inits = getInitVals(self.params, target="PsychoJS")
        # Write some code
        code = (
            "// Create %(name)s, just a dictionary with param values, to show you how to include param values\n"
            "%(name)s = {\n"
            "    'win': win,\n"
            "    'name': '%(name)s',\n"
            "    'exampleParam': %(exampleParam)s,\n"
            "};\n"
        )
        buff.writeIndentedLines(code % inits)


    def writeFrameCode(self, buff):
        """
        Code to execute each frame in Python experiments
        """
        # If starting this frame...
        indented = self.writeStartTestCode(buff)
        if indented:
            buff.setIndentLevel(-indented, relative=True)
        # If active this frame...
        indented = self.writeActiveTestCode(buff)
        if indented:
            buff.setIndentLevel(-indented, relative=True)
        # If finishing this frame...
        indented = self.writeStopTestCode(buff)
        if indented:
            buff.setIndentLevel(-indented, relative=True)
    
    def writeFrameCodeJS(self, buff):
        """
        Code to execute each frame in JS experiments
        """
        # If starting this frame...
        indented = self.writeStartTestCodeJS(buff)
        if indented:
            buff.setIndentLevel(-indented, relative=True)
            buff.writeIndentedLines("};\n")
        # If active this frame...
        indented = self.writeActiveTestCodeJS(buff)
        if indented:
            buff.setIndentLevel(-indented, relative=True)
            buff.writeIndentedLines("};\n")
        # If finishing this frame...
        indented = self.writeStopTestCodeJS(buff)
        if indented:
            buff.setIndentLevel(-indented, relative=True)
            buff.writeIndentedLines("};\n")