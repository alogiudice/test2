import visa
  


class tekgen:
    
    def __init__(self, rm, num):
        data = rm.list_resources()
        self.inst = rm.open_resource('{}'.format(data[num]))
        
    def set_freq(self, value):
        self.inst.write("SOUR1:FREQ:FIX {}".format(value))
        
    def set_amp(self, value):
        self.inst.write("SOUR1:VOLT:AMPL {}".format(value))
        

class tekosc:
    
    def __init__(self, rm, num):
        data = rm.list_resources()
        self.inst = rm.open_resource('{}'.format(data[num]))
        
    def pantalla_ascii(self):    
        self.inst.write("DAT:ENC ASCII")
        pantalla = self.inst.query_ascii_values('CURV?')
        return pantalla
        
        
rm = visa.ResourceManager('@py')
