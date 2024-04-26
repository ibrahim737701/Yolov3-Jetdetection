import os

def write_image_paths_to_file(image_folder, output_file):
    with open(output_file, 'w') as file:
        # Traverse the directory and its subdirectories
        for root, dirs, files in os.walk(image_folder):
            for file_name in files:
                # Check if the file is an image file
                if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                    # Write the absolute path of the image to the text file
                    file.write(os.path.join(root, file_name) + '\n')

# Path to the directory containing the images
image_folder = '/raid/users/mohammadibrahim-st/TSAI/YoloV3/data/customdata/images'

# Path to the output text file
output_file = '/raid/users/mohammadibrahim-st/TSAI/YoloV3/data/customdata/custom.txt'

# Write image paths to the text file
write_image_paths_to_file(image_folder, output_file)

print("Image paths have been written to", output_file)
