import cv2, os
base_path = "tiff_images/"
new_path = "jpg_images/"
for infile in os.listdir(base_path):
    try:
        print ("file : " + infile)
        #read = cv2.imread(base_path + infile)
        img = cv2.imread(base_path + infile,cv2.IMREAD_UNCHANGED)
        outfile = infile.split('.')[0] + '.jpg'
        cv2.imwrite(new_path+outfile,img,[int(cv2.IMWRITE_JPEG_QUALITY), 200])
    except:
        print("error while converting")


