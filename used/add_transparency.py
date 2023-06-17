from PIL import Image

# Open the RGB image
image = Image.open('C:/Users/yujir/Downloads/Solid_red.png')

# Create a new image with an alpha channel
rgba_image = image.convert('RGBA')

# Create a transparent mask
alpha_mask = Image.new('L', rgba_image.size, 128)

# Apply the alpha mask to the RGBA image
rgba_image.putalpha(alpha_mask)

# Save the resulting image with transparency
rgba_image.save('C:/Users/yujir/Downloads/Solid_red_50.png')