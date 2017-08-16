class IInput():

    def read(self, message):
        raise NotImplementedError()
        
        
    def asking_message(self):
        """ Message given to ask for an input """
        raise NotImplementedError() 