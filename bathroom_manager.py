#!/usr/bin/python3
import random, time
import threading

class Banheiro:
    def __init__(self,c):
        self.contMulheres = 0
        self.contHomens = 0
        self.lista_espera_f = []
        self.lista_espera_m = []
        self.capacidade = int(c)
        self.mutex = threading.Semaphore(1)
        self.bd = threading.Semaphore(int(c))

    def acquireLock(self, thr):
        self.mutex.acquire()
        if thr.genre == "F":
            self.contMulheres += 1
            if self.contMulheres >= 1 and self.contHomens == 0 and self.contMulheres < self.capacidade:
                print (thr.genre, thr.id,  " - entrando...")
                thr.done = True
                self.bd.acquire()
            else:
                self.contMulheres -= 1
                pass
        else:
            self.contHomens += 1
            if self.contHomens >= 1 and self.contMulheres == 0 and self.contHomens < self.capacidade:
                print (thr.genre, thr.id,  " - entrando...")
                thr.done = True
                self.bd.acquire()
            else:
                self.contHomens -= 1
                pass

        self.mutex.release()

    def releaseLock(self, thr):
        self.mutex.acquire()

        if thr.genre == "F":
            self.contMulheres -= 1
            print (thr.genre, thr.id," - saindo.")
            self.bd.release()
        elif thr.genre == "M":
            self.contHomens -= 1
            print (thr.genre, thr.id," - saindo.")
            self.bd.release()

        self.mutex.release()

class Pessoa (threading.Thread):

    def __init__(self, gen, id, ban):
        threading.Thread.__init__(self)
        self.genre = gen
        self.id = id
        self.ban = ban
        self.done = False

    def run(self):
        while self.done == False:
            time.sleep(random.randint(1, 5))
            self.ban.acquireLock(self)

        time.sleep(random.randint(1, 5))
        self.ban.releaseLock(self)

if __name__ == "__main__":
    import sys
    cap = sys.argv[1]
    ban = Banheiro(cap)
    for i in range(25):
        mulher = Pessoa("F", i, ban)
        mulher.start()

        homem = Pessoa("M", i, ban)
        homem.start()
