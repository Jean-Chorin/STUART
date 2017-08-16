
from inoutputs.ioutput import *


class OutputCLI(IOutput):

    def write(self, message):
        print(message)