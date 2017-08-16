#!/usr/bin/python3
# coding: utf8

from components import Fortune
from inoutputs import OutputCLI, InputCLI
from instance import Instance

def instance_creation():
    """
    Build the Instance instance
    """
    instance = Instance()
    
    output_comp = OutputCLI()
    instance.add_output(output_comp)
    
    input_comp = InputCLI()
    instance.add_input(input_comp)
    
    fortune = Fortune()
    instance.add_component(fortune)
    
    return instance


def main():
    instance = instance_creation()
    
    while(True):
        request = instance.asking_message()

        if request == instance.stop_message():
            instance.leaving_message()
            break
        res = instance.run(request)
        
        #instance.write(res)

if __name__ == '__main__':
    
    try:
        main()
    except KeyboardInterrupt:
        print("Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        exit(1)
    exit(0)
