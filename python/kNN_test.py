import kNN

# group,labels = kNN.createDataSet0()
#
# result = kNN.classify0([1,0.5],group,labels,3)
# print(result)
#
# group,labels = kNN.createDataSet1()
# result = kNN.classify1([1,1,1],group,labels,3)
# print(result)

#kNN.file3('datingTestSet.txt','datingTestSet3.txt');

datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')

result = kNN.classify1([136,50,0.428964],datingDataMat,datingLabels,20)
print(result)