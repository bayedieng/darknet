from eagle_labels import data_root
import glob 

write_path = "build/darknet/x64/data/train.txt"

with open(write_path, "w") as f:
    img_files = glob.glob(data_root + "/*.png")
    img_files.sort()
    for img in img_files:
        f.write(img + "\n")

    
         


