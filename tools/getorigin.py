import os
import cv2
import numpy as np

def process_images(path_a, path_b, output_path):
    a_files = os.listdir(path_a)
    b_files = os.listdir(path_b)

    common_files = set(a_files) & set(b_files)

    for file in common_files:
        image_a = cv2.imread(os.path.join(path_a, file))
        image_b = cv2.imread(os.path.join(path_b, file))

        # Calculate the mean value of non-black pixels in each channel of image A
        non_black_pixels = np.logical_or.reduce((image_a[:,:,0] > 10, image_a[:,:,1] > 10, image_a[:,:,2] > 10))
        mean_value_c = np.mean(image_a[non_black_pixels],axis=0)
        print(mean_value_c)
        # Resize image A to the size of image B
        image_a_resized = cv2.resize(image_a, (image_b.shape[1], image_b.shape[0]))

        # Convert image A to grayscale for comparison
        image_a_gray = cv2.cvtColor(image_a_resized, cv2.COLOR_BGR2GRAY)

        # Create a mask based on the condition
        mask = (image_a_gray < 128).astype(np.uint8) * 255

        # Combine images based on the mask
        result_image = np.where(mask[:, :, np.newaxis] == 255, image_b, mean_value_c).astype(np.uint8)

        output_file_path = os.path.join(output_path, file)
        cv2.imwrite(output_file_path, result_image)

    return "操作完成"


# Example usage:
path_a = './result/inferv7-seg-a5/lcz/NG/'
path_b = './datasets/lcz/NG'
output_path = './result/inferv7-origin/'
process_images(path_a, path_b, output_path)