from components.component import Component


class NiceWords(Component):
    """ This component will be asked for an random insult, 
    will retrieve one from the storage, 
    and will give it """
    
    
    def is_string_understood(self, message):
        if message is "insult":
            return True
        
        return False


    def run(self, message):
        pass

