
import simpy 
import random 
import statistics 

def Processqty(env, nameProcess, RAM, timeProcess, amountProcess):
    global totalTimeProcess, start

    interval = 10
    timeProcess = random.expovariate(1.0 / interval) # ciclos de reloj 

    amountProcess = random.randint(1,10)

    # entra por ciclo de reloj 
    yield env.timeout(timeProcess)
    print("El programa: %a necesita la una cantidad total de %b de RAM para realizar proceso" (nameProcess, amountProcess))

    start = env.now 

    # suspende el proceso si no puede ingresar a RAM
    yield RAM.get(amountProcess)
    print("El programa: %a puede hacer uso de %b de la cantitdad total de RAM" (nameProcess, amountProcess))
    
    totalInstructions = random.randint(1,10)

    CPUtotalInstructions = 3 

    while CPUtotalInstructions < totalInstructions: 
        
        yield (CPU.request()) # pregunta al CPU si se puede ejectuar, si no, queda en cola de espera
# ----------------------------------------------------------------

env = simpy.Environment()

RAM = simpy.Container(env, init=100, capacity=100) # contenedor de RAM 
CPU = simpy.Resource(env, capacity=1) # capacidad de CPU 
random.seed(10) # fijar inicio de random 

totalTimeProcess = env.now - start #tiempo total del proceso 

averageTime = statistics.mean(totalTimeProcess) # tiempo promedio 
sdv = statistics.stdev(totalTimeProcess) # desviacion estandar 

print("El tiempo promedio total fue de: ", averageTime)
print("La desviacion estandar del proceso fue de: ", sdv)


