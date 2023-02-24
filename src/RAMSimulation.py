
import simpy 

class RAMSimuation:
    
    def __init__(self, env, capacity): 
        self.env = env
        self.capacidad = capacity
        self.memoria = simpy.Container(env, capacity = capacity, init = 0) 

    def escribirRAM(self, value, directionMemory): 
        yield self.memory.put(value)

        print("El valor" + value + "ha sido colocado en la direccion " + directionMemory)

    def leerRAM(self, direccion): 
        valueinRAM = yield self.memory.get() 


    env = simpy.Environment()

    newRAM = RAMSimuation(env, capacity = 25)

