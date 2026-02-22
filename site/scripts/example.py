# Example script for Jumperless MicroPython
# Open in JumperIDE and run on your board

from jumperless import connect, disconnect

# Connect two nodes (example)
connect("N1", "N2")
# ... do something ...
disconnect("N1", "N2")
