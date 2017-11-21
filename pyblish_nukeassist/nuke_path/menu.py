import logging

import nuke

logging.basicConfig(level=logging.INFO)

try:
    __import__("pyblish_nukeassist")
    __import__("pyblish")

    # Only load integration in NukeAssist
    if "--nukeassist" not in nuke.rawArgs:
        raise ImportError("pyblish-nuke only works in Nuke or NukeX.")

except ImportError as e:
    nuke.tprint("pyblish: Could not load integration: %s " % e)

else:

    import pyblish_nukeassist

    # Setup integration
    pyblish_nukeassist.setup()
