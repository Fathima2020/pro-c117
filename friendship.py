from ctypes import sizeof
import os
import cv2


path = "Images"


images = []





for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        

size=(width,height)
print(size,width,height)
out=cv2.VideoWriter("friendship.mp4",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
        
print(len(images))
count = len(images)
frame=cv2.imread(images[0.8])
height,width,channels=frame.shape


print(height,width)

for i in range(0,-1):
    image=cv2.imread
    out.write(image)

out.release()
print("done")    