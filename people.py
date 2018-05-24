# -*- coding: ISO-8859-1 -*-
import thread
import time, random
import threading
from bathroom import BancoDados

bd = BancoDados()

def homem(e):
   while True:
      time.sleep(random.randint(1, 5))
      bd.acquireHomemLock()
      print "Homem %i - entrando..." %e
      time.sleep(random.randint(1, 5))
      bd.releaseHomemLock()
      print "Homem %i - saindo." %e

def mulher(l):
   while True:
      time.sleep(random.randint(1, 5))
      bd.acquireMulherLock()
      print "Mulher %i - entrando..." %l
      time.sleep(random.randint(1, 5))
      bd.releaseMulherLock()
      print "Mulher %i - saindo." %l

for i in range(20):
   print "Homem", i
   thread.start_new_thread(homem, tuple([i]))
for i in range(25):
   print "Mulher", i
   thread.start_new_thread(mulher, tuple([i]))

while 1: pass