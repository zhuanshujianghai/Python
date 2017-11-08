from math import log
import operator

def clacShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelConnts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelConnts.keys():
            labelConnts[currentLabel] = 0
        labelConnts[currentLabel]+=1
    shannoEnt = 0.0
    for key in labelConnts:
        prob = float(labelConnts[key])/numEntries
        shannoEnt -= prob * log(prob,2)
    return shannoEnt

def createDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfactin','flippers']
    return dataSet,labels

def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = clacShannonEnt(dataSet)
    bestInfoGain = 0.0;bestFeature=-1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*clacShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree
myData,labels=createDataSet()
# print(myData)
# print(labels)
# shan = clacShannonEnt(myData)
# print(shan)
# myData[0][-1] = "maybe"
# print(myData)
# shan1 = clacShannonEnt(myData)
# print(shan1)
# result = splitDataSet(myData,0,1)
# print(result)
# result = splitDataSet(myData,0,0)
# print(result)
# result = splitDataSet(myData,1,1)
# print(result)
# result = splitDataSet(myData,1,0)
# print(result)
# index = chooseBestFeatureToSplit(myData)
# print(index)
myTree = createTree(myData,labels)
print(myTree)