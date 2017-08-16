import os

from components.component import Component


class Fortune(Component):
    """ This component will be asked for an random fortune, 
    will get one from the Linux command line, 
    and will give it """
    
    def is_string_understood(self, message):
        if message == "fortune":
            return True

        return False


    def run(self, message):
        """ Execute the command fortune and gives the result
        Does not use message: execute "fortune" whatever happens """
        res = os.popen("fortune")
        return str(res.read())
    
    
    def confirm_message(self):
        return "do you want the fortune message ?"
