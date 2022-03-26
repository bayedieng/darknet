from eagle_labels import root
import glob 

write_path = "build/darknet/x64/data/train.txt"

with open(write_path, "w") as f:
    img_files = glob.glob(root + "/*.png")
    img_files.sort()
    for img in img_files:
        f.write(img + "\n")

    
         


