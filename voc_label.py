import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = ['train', 'val', 'test']

classes = ["0/其他垃圾/快餐盒", "1/其他垃圾/塑料袋", "2/其他垃圾/烟头", "3/易腐垃圾/果皮", "4/易腐垃圾/叶子", "5/可回收垃圾/泡沫",
           "6/可回收垃圾/易拉罐", "7/可回收垃圾/玻璃瓶", "8/可回收垃圾/纸", "9/可回收垃圾/绳子", "10/可回收垃圾/饮料瓶",
           "11/可回收垃圾/纸袋"]
# classes = ["bottle", "glass", "leaf", "milk-box", "plastic-bag", "branch"]
# classes = ["0-other garbage-fast food box", "1-other garbage-soiled plastic", "2-other garbage-cigarette",
#            "3-blet waste-fruit peel", "4-blet waste-leaf", "5-recyclables-foam", "6-recyclables-can",
#            "7-recyclables-bottle", "8-recyclables-paper", "9-recyclables-rope", "10-recyclables-drink bottle",
#            "11-recyclables-paper bags"]

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(image_id):
    in_file = open('E:/example/PycharmProjects/datasets/VOCwater_garbages/Annotations/%s.xml' % (image_id), encoding='UTF-8')
    out_file = open('E:/example/PycharmProjects/datasets/VOCwater_garbages/labels/%s.txt' % (image_id), 'w', encoding='UTF-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()

for image_set in sets:
    if not os.path.exists('VOCwater_garbages/labels/'):
        os.makedirs('VOCwater_garbages/labels/')
    image_ids = open('E:/example/PycharmProjects/datasets/VOCwater_garbages/ImageSets/Main/%s.txt' % (image_set),
                     encoding='UTF-8').read().strip().split()
    #image_ids = open('VOC2007/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    list_file = open('%s.txt' % (image_set), 'w', encoding='UTF-8')
    for image_id in image_ids:
        list_file.write('VOCwater_garbages/JPEGImages/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()

# os.system("cat 2007_train.txt 2007_val.txt 2012_train.txt 2012_val.txt > train.txt")
# os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")

# sets = ['train', 'val', 'test']
# classes = ["瓶子", "玻璃", "叶子", "牛奶盒", "塑料袋", "树枝"]