import cv2
import glob
import os


video_path = r"C:\Users\111\Desktop\REPORT APPS\dataset"
lenght = len(r"C:\Users\111\Desktop\REPORT APPS\dataset")+1
print(lenght)
video_list = glob.glob(video_path+'/*')
print("video list",video_list)

def images_from_video(vid):
        i=0
        while True:
            try:
                _, img = vid.read()
                if not os.path.exists(each_video[lenght:-4]):
                    os.makedirs(each_video[lenght:-4])
                #print(r'{}/image {}.jpg'.format(each_video[:-4],i))
                cv2.imwrite(r'{}/image {}.jpg'.format(each_video[lenght:-4],i),img)
                i+=1
                print("image = ",i)
            except:
                print("excption")
                
                return

for each_video in video_list:
        vid = cv2.VideoCapture(each_video)
        images_from_video(vid)


