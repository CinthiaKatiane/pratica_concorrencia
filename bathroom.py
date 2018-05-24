# -*- coding: ISO-8859-1 -*-
import thread
import time, random
import threading

class BancoDados:
    contMulheres = 0
    contHomens = 0
    mutex      = threading.Semaphore(1)
    bd         = threading.Semaphore(1)

    def acquireMulherLock(self):
        global contMulheres, contHomens
        self.mutex.acquire()
        self.contMulheres += 1

        if self.contMulheres == 1 and self.contHomens == 0:
            self.bd.acquire()
            print "dentro"

        self.mutex.release()

    def releaseMulherLock(self):
        global contMulheres
        self.mutex.acquire()
        self.contMulheres -= 1

        if self.contMulheres == 0:
            self.bd.release()

        self.mutex.release()

    def acquireHomemLock(self):
        global contMulheres, contHomens
        self.mutex.acquire()
        self.contHomens += 1

        if self.contHomens == 1 and self.contMulheres == 0:
            self.bd.acquire()
            print "Dentro"

        self.mutex.release()

    def releaseHomemLock(self):
        global contHomens
        self.mutex.acquire()
        self.contHomens -= 1

        if self.contHomens == 0:
            self.bd.release()

        self.mutex.release()