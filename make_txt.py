import os
import random
trainval_percent = 0.7 #可以根据自己需要调整数据
train_percent = 0.8 #可以根据自己需要调整
xmlfilepath = 'Annotations'
txtsavepath = 'imageSets'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open('imageSets/Main/trainval.txt', 'w')
ftest = open('imageSets/Main/test.txt', 'w')
ftrain = open('imageSets/Main/train.txt', 'w')
fval = open('imageSets/Main/val.txt', 'w')
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
