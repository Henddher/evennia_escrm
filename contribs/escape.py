from evennia import CmdSet
from evennia.contrib.ingame_python.commands import CmdCallback

class ExtrasCmdSet(CmdSet):

    def at_cmdset_creation(self):
        super(ExtrasCmdSet, self).at_cmdset_creation()
        self.add(CmdCallback())
