
import simpy 
import random 
import statistics 

def Processqty(env, nameProcess, RAM, timeProcess, amountProcess, totalInstructions, CPUactualInstruction):
    global totalTime,start

    # entra por ciclo de reloj 
    yield env.timeout(timeProcess)
    print("El programa: %s necesita la una cantidad total de %d de RAM para realizar proceso\n" % (nameProcess, amountProcess))

    start = env.now 

    # suspende el proceso si no puede ingresar a RAM
    yield RAM.get(amountProcess)
    print("El programa: %s puede hacer uso de %d de la cantidad total de RAM\n" % (nameProcess, amountProcess))

    actualProgramInstruction = 0   

    while actualProgramInstruction < totalInstructions: 

        with CPU1.request() as CPU: 
            yield(CPU) # pregunta al CPU si se puede ejectuar, si no, queda en cola de espera

            if((totalInstructions - actualProgramInstruction) >= CPUactualInstruction): 
             
                newProgramInstruction = CPUactualInstruction 

            else: 
            
                newProgramInstruction = (totalInstructions - actualProgramInstruction) 
        
            print("El programa: %s realizara %s instrucciones dentro del CPU\n" % (nameProcess, newProgramInstruction))

            waitOrReady = random.randint(1, 2)

            if(waitOrReady == 1 and (actualProgramInstruction < totalInstructions)):
                with Wait.request() as execute: 

                    yield (execute) # espera ejecucion 
                    yield (env.timeout(1)) # espera hasta que cumpla la condicion de arriba 

                    print("\tEl programa %a ha realizado operaciones de I/O\n" % (nameProcess))
            
        yield(env.timeout(newProgramInstruction/CPUactualInstruction)) # suspende durante el tiempo que tarda en ejecutarse a la velocidad de 3 por ciclo de reloj
        actualProgramInstruction += newProgramInstruction
        print("\tEl programa %s ha realizado %d de %f instrucciones del CPU\n" % (nameProcess, actualProgramInstruction, totalInstructions))

        if(actualProgramInstruction == totalInstructions):
            print("\tEl programa %s ha finalizado" % (nameProcess)) # imprime cuando el programa cumple todas las instrucciones 
        
        yield RAM.put(amountProcess) # regresa a la RAM la cantidad de proceso usado 
        print("\tLa cantidad total %s de memoria ha sido liberada a la RAM\n" % (amountProcess))

        totalTime += env.now - start
        arrayTime.append(totalTime)
        
# ----------------------------------------------------------------

env = simpy.Environment()

totalProcess = 100 # cantidad inicial de procesos 

start = 0 
arrayTime = []
totalTime = 0 

RAM = simpy.Container(env, init=100, capacity=100) # contenedor de RAM 
CPU1 = simpy.Resource(env, capacity=1) # capacidad de CPU 
Wait = simpy.Resource(env, capacity=1) # guarda las instrucciones 

random.seed(10) # fijar inicio de random 

for i in range(totalProcess): #cantidad de procesos, cambiar por procesos  
    timeProcess = random.expovariate(1.0 / 10) # ciclos de reloj
    amountProcess = random.randint(1,10)
    totalInstructions = random.randint(1,10)

    env.process(Processqty(env, "no.%a" % i, RAM, timeProcess, amountProcess, totalInstructions, 3)) 

env.run() 

averageProcess = statistics.mean(arrayTime)
sdv = statistics.stdev(arrayTime)

print("\nInformación obtenida de la RAM: ")

print("\tEl tiempo promedio fue de: ", averageProcess)
print ("\tLa desviacion estandar de los tiempos es: ", sdv )

