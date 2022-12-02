.. rst-class:: component-bio
Template Plugin Component
============================================================

A template component which does absolutely nothing, purely exists to show you how to 
add a component to a plugin.
    
.. toctree::
  :maxdepth: 2

Name : code
    Name of this component (alphanumeric or _, no spaces)

Start : code
    When does the component start?

Expected start (s) : code
    (Optional) expected start (s), purely for representing in the timeline

start type : str
    How do you want to define your start point?

Stop : code
    When does the component end? (blank is endless)

Expected duration (s) : code
    (Optional) expected duration (s), purely for representing in the timeline

stop type : str
    How do you want to define your end point?

Data
------------------------------------------------------------
Save onset/offset times : bool
    Store the onset/offset times in the data file (as well as in the log file).

Sync timing with screen refresh : bool
    Synchronize times with screen refresh (good for visual stimuli and responses based on them)

Testing
------------------------------------------------------------
Disable component : bool
    Disable this component

