from math import log

#logarithm such that log(0) is 0
def entlog(val):
    if val == 0:
        return 0
    return val*log(val,2)

#clasdist is a list contianing the number of instances of each class value.
#for instance, in a data set where there are 5 instances classified as 0
#and 3 as 1, clasDist would be [5,3]
def entropy(clasdist):
    summe = sum(clasdist)
    #if there is no data in our partition, then the entropy is effectively zero
    if summe == 0:
        return 0
    return sum(map(lambda x: -entlog(x/float(summe)), clasdist))         
 
#Information Gain.
#newclasdists is a list containing class distributions of the resulting splits.
#it is a list of lists, ie: [[2,1],[3,2]]
def IG(clasdist,newclasdists):
    summe = sum(clasdist)
    newE= sum(map(lambda x: (sum(x)/float(summe))*entropy(x), newclasdists))
    return entropy(clasdist) - newE
