# encoding:utf-8
import os
import xml.etree.ElementTree as ET

#将xml文件里的英文标签转化为中文标签
count = 0
list_xml = []
dict = {
        "0-other garbage-fast food box": "0/其他垃圾/快餐盒",
        "1-other garbage-soiled plastic": "1/其他垃圾/塑料袋",
        "2-other garbage-cigarette": "2/其他垃圾/烟头",
        "3-blet waste-fruit peel": "3/易腐垃圾/果皮",
        "4-blet waste-leaf": "4/易腐垃圾/叶子",
        "5-recyclables-foam": "5/可回收垃圾/泡沫",
        "foam": "5/可回收垃圾/泡沫",
        "6-recyclables-can": "6/可回收垃圾/易拉罐",
        "7-recyclables-bottle": "7/可回收垃圾/玻璃瓶",
        "8-recyclables-paper": "8/可回收垃圾/纸",
        "paper": "8/可回收垃圾/纸",
        "9-recyclables-rope":  "9/可回收垃圾/绳子",
        "rope": "9/可回收垃圾/绳子",
        "10-recyclables-drink bottle":  "10/可回收垃圾/饮料瓶",
        "11-recyclables-paper bags":  "11/可回收垃圾/纸袋"
        }

openPath = "E:\example\PycharmProjects\datasets\VOCwater_garbages\Annotations"
savePath = "E:\example\PycharmProjects\datasets\VOCwater_garbages\Annotations"
fileList = os.listdir(openPath)  # 得到进程当前工作目录中的所有文件名称列表
for fileName in fileList:  # 获取文件列表中的文件
    if fileName.endswith(".xml"):  # 只看xml文件
        print("filename=:", fileName)
        tree = ET.parse(os.path.join(openPath, fileName))
        root = tree.getroot()
        print("root-tag=:", root.tag)  # ',root-attrib:', root.attrib, ',root-text:', root.text)
        for child in root:  # 第一层解析
            if child.tag == "object":  # 找到object标签
                print(child.tag)
                for sub in child:
                    if sub.tag == "name":
                        print("标签名字:", sub.tag, ";文本内容:", sub.text)
                        if sub.text not in list_xml:
                            list_xml.append(sub.text)
                        if sub.text in list(dict.keys()):
                            sub.text = dict[sub.text]
                            print(sub.text)
                            count = count + 1
        tree.write(os.path.join(savePath, fileName), encoding='utf-8')
    print("=" * 20)

print(count)
for i in list_xml:
    print(i)