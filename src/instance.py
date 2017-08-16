
from inoutputs import IOutput, IInput
from components import Component


class Instance():

    def __init__(self):
        self.output = None
        self.input = None
        self.components = []


    def add_output(self, output):
        if isinstance(output, IOutput):
            self.output = output
        else:
            raise TypeError()


    def write(self, message):
        self.output.write(message)


    def add_input(self, inputs):
        if isinstance(inputs, IInput):
            self.input = inputs
        else:
            raise TypeError()


    def read(self, message):
        return self.input.read(message)

    def asking_message(self):
        return self.input.asking_message()


    def add_component(self, component):
        if isinstance(component, Component):
            self.components.append(component)
        else:
            raise TypeError()


    def leaving_message(self):
        self.write("Good bye")
        
        
    def run(self, message):
        """ Has a different behaviour if 0, 1 or more components are understood
        give a different output message """
        count = []
        understood = False
        
        """ Try the number of components that can understand the given message """
        for component in self.components:
            if component.is_string_understood(message) :
                count.append(component)     

        """ Try the given message on all the components stored
        If only of them understands: 
        If more than one understand: 
        If no one understand:  """
        counter = len(count)
        
        if counter == 1 :
            output_mess = count[0].run(message)
            understood = True
        elif counter == 0:
            output_mess = "I did not understand the message"
        else:
            output_mess = self.construct_confirm_message(count)

        self.write("\n" + output_mess)

        return understood
    
    
    def construct_confirm_message(self, count):
        """ Used if more than one component understand the message
        Create a confirmation message depending on the component that understood """
        res = ""
        for comp in count :
            res += comp.confirm_message() + ", "
    
    
    def stop_message(self):
        return "stop"
    
    