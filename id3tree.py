#contains Information gain, entropy functions, etc
import myFunctos as fu

#numpy to be safe. probably not needed.
import numpy as np

#will contain however we decide to define our data set
import DataSet as ds

class Id3Tree:
   class Node:
      def __init__(parent = None, subNodes = [], remainingAttributes = [], remainingStimuli = [], splittingAttribute = None, myClass = None):

         #might not need this???
         self.parent = parent

         #a list of Nodes.
         self.subNodes = subNodes 

         #list of attributes left to split over on this node
         self.remainingAttributes = remainingAttribute

         #list of Stimuli still being considered in this tree.
         self.remainingStimuli = remainingStimuli

         #attribute the node splits over
         self.splittingAttribute = splittingAttribute

         #Classification. None if not leaf node.
         self.myClass = myClass

         def isLeaf(self):
            if self.classify == None:
               return False
            return True

         #removes data that is no longer necessary after a tree is fully grown
         def clean():
            self.remainingAttributes = None 
            self.remainingStimuli = None

   def __init__(self):
      #probably would be useful for pruning algorithm
      self.leafNodes=[]
      
   def train(self, trainSet):
      
   def classify(self, data):

   def prune(self):
