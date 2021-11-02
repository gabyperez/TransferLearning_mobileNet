import os
path = 'C:/Users/agust/Documents/ia/models/research/object_detection/images/train'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1
