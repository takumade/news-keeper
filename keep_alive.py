from threading import Thread

from main import main

def run():
  main()

def keep_alive():  
    t = Thread(target=run)
    t.start()
