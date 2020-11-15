import os
from PIL import Image
parent_path = os.getcwd()
directory = "Converted"
convert_path = os.path.join(parent_path,directory)
if os.path.exists(convert_path) == False:
    os.mkdir(convert_path)
i = 1
for filename in os.scandir(parent_path):
    try:
        new_file = convert_path + "\\Image" + str(i) + ".png"
        i = i+1
        im = Image.open(filename.path)
        im.thumbnail((512,512))
        im.save(new_file,"PNG",dpi=(300,300))
        print("Converted " + str(i-1))   
    except:
        continue
