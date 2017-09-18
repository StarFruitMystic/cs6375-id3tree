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
         def clean(self):
            self.remainingAttributes = None 
            self.remainingStimuli = None

         #not done
         def IG(self, dataSet, attr):
            stimTuple = self.genStimList(dataSet, attr)
            sizeZero = len(stimTuple[0])
            sizeOne = len(stimTuple[1])
            return self.entropy(dataSet) - 

         def entropy(self, dataSet):
            return entropy(dataSet, self.remainingStimuli)
            
         def genStimLists(self, dataSet, attr):
            listZero = list(filter(lambda x: dataSet[attr][x] == 0, self.remainingStimuli))
            listOne = list(filter(lambda x: dataSet[attr][x] == 1, self.remainingStimuli))
            return (listZero, ListOne)

         def clasDist(self, dataSet, stimuliList):
            ones = len(filter(lambda x: dataSet["Class"] == 1, stimuliList))
            zeros = len(filter(lambda x: dataSet["Class"] == 1, stimuliList))
            return (zeros, ones)

         def isPure(self, dataSet, stimuliList = self.remainingStimuli):
            if len(stimuliList) < 2:
               return True
            y = stimuliList[0]
            for x in stimuliList:
               if dataSet["Class"][x] != y:
                  return False
            return True



   def __init__(self):
      #probably would be useful for pruning algorithm
      self.leafNodes=[]
      
   def train(self, trainSet):
      attributeList = list(trainSet.keys())
      stimuliList = list(range(trainSet.shape[0]))
      node = Node(None, [],attributeList, stimuliList, None, None)

      for attr in node.remainingAttributes:
         
   def classify(self, data):

   def prune(self):
