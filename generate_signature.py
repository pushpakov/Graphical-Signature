from PIL import Image, ImageDraw, ImageFont

# Create a blank image with a white background
width, height = 300, 100
background_color = (255, 255, 255)  # White
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Specify the signature text and font
signature_text = input("Enter your name for generating graphical signature: ")

font_size = 28
font_color = (0, 0, 0)  # Black
font = ImageFont.truetype("Alivia.otf", font_size)   # you can use any font instead of Alivia you just need to download it and give the correct path here.

# Calculate the position to center the text
text_width, text_height = draw.textsize(signature_text, font)
x = (width - text_width) / 2
y = (height - text_height) / 2

# Draw the text on the image
draw.text((x, y), signature_text, font=font, fill=font_color)

# Save the signature image
image.save("signature.png")

# Optionally, display the image
image.show()
