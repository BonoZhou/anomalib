import os
from PIL import Image

folder_path = r"D:\hust\MediaLab\IAD\Anomalib\anomalib\datasets\fu\train\good"
output_folder_path = r"D:\hust\MediaLab\IAD\Anomalib\anomalib\datasets\fucut\train\good"
# crop_x = 1000  # 裁剪起始横坐标
# crop_y = 20  # 裁剪起始纵坐标
crop_x = 4096  # 裁剪起始横坐标
crop_y = 1500  # 裁剪起始纵坐标
crop_size_x = 4096  # 裁剪大小
crop_size_y = 1500  # 裁剪大小


if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        
        # 裁剪图像
        cropped_img = img.crop((crop_x, crop_y, crop_x+crop_size_x, crop_y+crop_size_y))
        
        # 保存裁剪后的图像
        output_path = os.path.join(output_folder_path, "1_"+filename)
        cropped_img.save(output_path)
