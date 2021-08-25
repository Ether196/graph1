from os import urandom
from random import randrange
import random as rand
from matplotlib import pyplot as plt

#change name of file and class name to time_window_graph.py
class TimeWindowGraph:
    
    # empty init
    mylist =[]
    listsize = 0
    windowsize = 0 

    def __init__(self,listsize):
        self.listsize=listsize
        # fill array with random values from range [0:50]
        for _ in range(listsize):
            self.mylist.append(randrange(0,50))
    
    def showWindows(self,listsize,windowsize):
        self.windowsize = windowsize
        #print the list
        print("Display the list: " + str(self.mylist) + "")
        numofwindows = int(listsize/windowsize)
        print(f"Displaying {numofwindows} windows, each of size {windowsize}:".format(numofwindows,windowsize))
        i=1
        for _ in range(0,listsize,windowsize):
            print(f"Window number {i}: ".format(i) + str(self.mylist[_:_+windowsize]))
            # show the graph of each list            
            plt.plot(range(0,windowsize), (self.mylist[_:_+windowsize]))
            plt.title("Graph number {} of range [{}:{}]".format(i, _, _+windowsize-1))
            plt.show()
            i += 1
        i=1

# get the list and window size from user
listsize = int(input("Enter list size: "))
windowsize = int(input("Enter Window size: "))

array = TimeWindowGraph(listsize)

# display the windows one by one
TimeWindowGraph.showWindows(array,listsize,windowsize)