from PIL import Image

rows = 6

print("Input: big / small (chest), item (der genaue name, statt unterstrich leertaste) z.B.: big, melon slice")
eingabe = input()
config = eingabe.split(", ")
if " " in config[1]:
    item_url = config[1].replace(" ", "_")
else:
    item_url = config[1]

try:
    item_img = Image.open(f"res/items/{item_url}.png")
    item_img = item_img.convert("RGBA")
except FileNotFoundError:
    print(f"{config[1]} ist kein item in minecraft.")
    exit(1)
if item_url == "ender_pearl":
    count_img = Image.open("res/count16.png")
else:
    count_img = Image.open("res/count64.png")
count_img = count_img.convert("RGBA")

if config[0] == "big":
    rows = 6
    chest_img = Image.open("res/chest_big.png")
elif config[0] == "small":
    rows = 3
    chest_img = Image.open("res/chest_small.png")
chest_img = chest_img.convert("RGBA")

for y in range(rows):
    for x in range(9):
        chest_img.paste(item_img, (x * 18 + 8, y * 18 + 8), item_img)
        chest_img.paste(count_img, (x * 18 + 9, y * 18 + 9), count_img)

chest_img.save("output.png", quality=100)
