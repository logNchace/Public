from PIL import Image
import random

image_path = input("Please enter the name of the image file (e.g., towncity.jpg): ")
number_of_parts = int(input("Please enter the number of parts to cut the image into: "))
cut_direction = input("Do you want to cut the image horizontally or vertically? (h/v): ")

image = Image.open(image_path)
width, height = image.size
base_name = image_path.split('.')[0]
cropped_images = []

# Divide the image into the specified number of equal parts
for i in range(number_of_parts):
    if cut_direction.lower() == 'h':
        top = i * height // number_of_parts
        bottom = (i + 1) * height // number_of_parts
        cropped_image = image.crop((0, top, width, bottom))
    elif cut_direction.lower() == 'v':
        left = i * width // number_of_parts
        right = (i + 1) * width // number_of_parts
        cropped_image = image.crop((left, 0, right, height))
    else:
        print("Invalid direction entered, please use 'h' or 'v'.")
        exit()

    cropped_image.save(f"{base_name}_{i}.jpg")
    cropped_images.append(cropped_image)

print(f"The image {image_path} has been cut into {number_of_parts} parts.")

attempt = 0

# Continue asking if the user wants to reglue the parts in a random order until they press 'N'
while True:
    reglue_choice = input("Do you want to reglue all the parts in a random order? (Y/N): ")

    if reglue_choice.lower() == 'y':
        random.shuffle(cropped_images)

        if cut_direction.lower() == 'h':
            new_image = Image.new('RGB', (width, height))
            for i, cropped_image in enumerate(cropped_images):
                new_image.paste(cropped_image, (0, i * height // number_of_parts))
        else:
            new_image = Image.new('RGB', (width, height))
            for i, cropped_image in enumerate(cropped_images):
                new_image.paste(cropped_image, (i * width // number_of_parts, 0))

        new_image.save(f"{base_name}_random_{attempt}.jpg")
        print(f"The randomly ordered image has been saved as {base_name}_random_{attempt}.jpg.")
        attempt += 1
    else:
        print("The image parts were not reglued. The script has finished.")
        break
