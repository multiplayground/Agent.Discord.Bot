''' 
    Module to check if new ceres state different from previous by comparing image's hash
    if images differs then it replace 
'''
import imagehash
import os

from PIL import Image

def is_similar(img_1:str,img_2:str)-> bool:
    '''
        take names of two images and compare are they identical
        return: bool
    '''
    # directory with images
    static=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'static/')

    img_1_hash = imagehash.average_hash(Image.open(static+img_1))
    img_2_hash = imagehash.average_hash(Image.open(static+img_2))

    if img_1_hash != img_2_hash:
        os.remove(static+img_1)
        os.rename(static+img_2,static+img_1)
        return False
    
    return True
    
