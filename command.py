#import linuxcnc

class commands():
    def __init__(self, command, status, error):
        self.c = command
        self.s = status
        self.e = error
    
    def get_pos(self):
        return ["%4.2f" % self.s.position[0], 
                "%4.2f" % self.s.position[1], 
                "%4.2f" % self.s.position[2], 
                "%4.2f" % self.s.position[3], 
                "%4.2f" % self.s.position[4], 
                "%4.2f" % self.s.position[5], 
                ]
