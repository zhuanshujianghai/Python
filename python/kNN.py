from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet0():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A','A','B','B']
    return group,labels

def createDataSet1():
    group = array([[1.0, 1.1, 1.2], [1.0, 1.0, 0.8], [0, 0, 0], [0, 0.1, 0.3]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def classify1(inx,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inx,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file3(filename,filename1):
    fr = open(filename)
    content = fr.read()
    content = content.replace("didntLike","1")
    content = content.replace("smallDoses", "2")
    content = content.replace("largeDoses", "3")
    fr1 = open(filename1,'w')
    fr1.write(content)
    fr.close()
    fr1.close()

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals-minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def figure(datingDataMat,datingLabels):
    #https://www.zhihu.com/question/37146648
    zhfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    a=ax.scatter(datingDataMat[:, 0],datingDataMat[:, 1], 15.0*array(datingLabels), 15.0*array(datingLabels))
    plt.xlabel(u'每年获取的飞行里程数', fontproperties=zhfont)
    plt.ylabel(u'玩视频游戏所消耗的事件百分比', fontproperties=zhfont)
    plt.show()

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify1(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],10)
        print("the classifier came back with %d,the real answer is:%d"%(classifierResult,datingLabels[i]))
        if classifierResult!=datingLabels[i]:errorCount+=1.0
    print("the total error rate is:%f"%(errorCount/float(numTestVecs)))

def classifyPerson():
    resutlList = ['not at all','in small doses','in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify1((inArr-minVals)/ranges,normMat,datingLabels,3)
    print("you will probably like this person:",resutlList[classifierResult-1])