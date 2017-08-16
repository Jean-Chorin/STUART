
class Component():
    """ This class is an Interface that englobes all the component that can be added to STUART """

    def is_string_understood(self, message):
        """ This method take a string and return a boolean
        True if the component can execute some tasks with the given string
        False otherwise """
        raise NotImplementedError()


    def run(self, message):
        """ The function that will be run to do the task of the component
        'message' : the given input, to be handled """
        raise NotImplementedError()
    
    
    def confirm_message(self):
        """ This message will be given if two or more components are understood, to confirm the choice """
        raise NotImplementedError()
