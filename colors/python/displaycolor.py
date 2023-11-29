from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Color data
colors = {
    "Trustworthy Blue": "#003366",
    "Clean Turquoise": "#7FDBFF",
    "Calm Sky Blue": "#89CFF0",
    "White": "#FFFFFF",
    "Modern Grey": "#D3D3D3",
    "Midnight Black": "#1c1c1cff",
    "Harmony Green": "#4CAF50",
    "Growth Green": "#085E2B"
}

# Image size and other parameters
img_width = 600
img_height = 600
rectangle_height = img_height // len(colors)
font_size = 20

# Create a blank image and a drawing context
img = Image.new('RGB', (img_width, img_height), color='white')
draw = ImageDraw.Draw(img)

# Use a basic font included with PIL, or specify your own font file if you have one
font = ImageFont.truetype("LiberationSans-Regular.ttf", font_size)

# Drawing the colored rectangles and labels
y = 0
for color_name, hex_code in colors.items():
    draw.rectangle([0, y, img_width, y + rectangle_height], fill=hex_code)
    text = f"{color_name} ({hex_code})"

    # Calculate text width using textlength and height using font size
    text_width = draw.textlength(text, font=font)
    text_height = font_size  # Approximation for single line of text

    draw.text(((img_width - text_width) / 2, y + (rectangle_height - text_height) / 2), text, fill='black', font=font)
    y += rectangle_height

# Show the image using matplotlib
plt.imshow(img)
plt.axis('off')
plt.show()
