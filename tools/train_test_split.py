
from sklearn.model_selection import train_test_split
import os 

img_dir = "/home/disk2/new_gesture_two_boxes_temperature_down_bulge_left_right_221020/data/down_bulge/images"

train_valid_dir = "/home/disk2/new_gesture_two_boxes_temperature_down_bulge_left_right_221020/data/down_bulge"

train_pth = os.path.join(train_valid_dir, "train.txt")
valid_pth = os.path.join(train_valid_dir, "val.txt")
img_lst = os.listdir(img_dir)
train_list, valid_list = train_test_split(img_lst, test_size=0.2)

with open(train_pth, "w") as f:
    for img in train_list:
        tmp = os.path.join(img_dir, img)
        f.write(tmp+"\n")
f.close()

with open(valid_pth, "w") as f:
    for img in valid_list:
        tmp = os.path.join(img_dir, img)
        f.write(tmp+"\n")
f.close()