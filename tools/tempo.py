from pybricks.tools import wait, StopWatch

class Tempo:
    def pausar(tempo):
        wait(tempo)

    def getCronometro():
        return StopWatch.time()
    
    def pausarCronometro():
        StopWatch.pause()
    
    def retomarCronometro():
        StopWatch.resume()

    def resetarCronometro():
        StopWatch.reset()
