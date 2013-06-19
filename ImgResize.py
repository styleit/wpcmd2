'''
Created on 2013-3-30

@author: Laoe
'''
import PIL.Image as Image
import sys

def AdPicbyRate(img,width=-1,height=-1):
    w,h = img.size                 
    if(width==-1 and height==-1):
        width=w
        height=h
    elif(width==-1 and height>-1):
        rate = (height*1.0)/h
        width = int(rate * w)
    elif((width>-1 and height==-1) or (width>-1 and height>-1)):
        rate = (width*1.0)/w
        height = int(rate * h)
    return img.resize((width,height),Image.ANTIALIAS) 

def ResizePicbyRate(image_path,small_img_path,width=-1,height=-1):              
    img = Image.open(image_path)   
          
    small_img = AdPicbyRate(img,width,height)
    small_img.save(small_img_path)

def CropCenter(img,width,height):
    w,h = img.size
    x0=(w-width)/2
    x1=x0+width
    
    y0 =(h-height)/2
    y1 = y0+height
    
    region =(x0,y0,x1,y1)
    return img.crop(region)    

def CropPic(image_path,crop_img_path,width,height): 
    img = Image.open(image_path)
    w,h = img.size
    
    tmpImg=None
    if(w<width and h<height):
        if ((w*1.0)/width < (h*1.0)/height):
            tmpImg = AdPicbyRate(img, width)
        else:
            tmpImg = AdPicbyRate(img, -1, height)
    elif(w<width):
        tmpImg = AdPicbyRate(img, width)
    elif(h<height):
        tmpImg = AdPicbyRate(img, -1, height)
    else:
        tmpImg = img
        
    cropImg = CropCenter(tmpImg, width, height)
    cropImg.save(crop_img_path)

if __name__ == '__main__':
    if(len(sys.argv)>2):
        for item in sys.argv[1:]:
            if (len(item.split('.'))>1) :
                file_name = item.split('\\')[-1].split('.')
                post_target_img = file_name[0]+'_post.'+file_name[1]
                thumb_target_img = file_name[0]+'_thumb.'+file_name[1]
                ResizePicbyRate(item, post_target_img , 598)
                CropPic(item, thumb_target_img,240, 135)