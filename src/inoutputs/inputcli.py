from inoutputs.iinput import IInput


class InputCLI(IInput):

    def read(self, message):
        return input(message)
    
    
    def asking_message(self): 
        #os.system("clear")
        query = self.read("Do you have a request ? \n")
        return query.lower()
