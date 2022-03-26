import xml.etree.ElementTree as ET
import os

xml_path = "build/darknet/x64/data/eagle_labels"
root = "build/darknet/x64/data/obj/"

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def create_labels():
    for i in range(len(os.listdir(xml_path))):
        in_file = open(xml_path + f"Cars{i}.xml")
        out_file = open(root + f"Cars{i}.txt", 'w+')
        tree=ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        cls_id = 0
        obj = root.find("object")
        bndbox = obj.find("bndbox")
        b = (float(bndbox.find("xmin").text), float(bndbox.find("xmax").text), float(bndbox.find("ymin").text), float(bndbox.find("ymax").text))
        bb = convert((w, h), b)
        x_bb, y_bb, w_bb, h_bb = bb 
        out_file.write(str(cls_id) + " " + f"{x_bb} {y_bb} {w_bb} {h_bb}")

if __name__ == "__main__":
    create_labels()
    