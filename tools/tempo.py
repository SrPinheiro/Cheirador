from pybricks.tools import wait, StopWatch, DataLog

class tempo:
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
