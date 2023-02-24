import simpy
import random 
import statistics 

env = simpy.Environment() 

class runTimeAndSD: 
    
    def __init__(self, env):
        self.env = env
        self.cantidadRecurso = simpy.Resource(env, capacity = 1)