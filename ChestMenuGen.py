from PIL import Image

rows = 6
non_stackable = False
non_stackable_items = ["_bucket",
                       "boat",
                       "sword",
                       "pickaxe",
                       "axe",
                       "hoe",
                       "shovel",
                       "helmet",
                       "chestplate",
                       "leggings",
                       "boots",
                       "bow",
                       "cake",
                       "elytra",
                       "flint_and_steel",
                       "fishing_rod",
                       "minecart",
                       "music_disc",
                       "writable_book",
                       "trident"]

print("Input: big / small (chest), item (der genaue name, statt unterstrich leertaste) z.B.: big, melon slice")
eingabe = input()  # Input in 'eingabe' speichern
configuration = eingabe.split(", ")  # Kisten-Typ und Item speichern
if " " in configuration[1]:
    item_url = configuration[1].replace(" ", "_")  # Leerzeichen mit Unterstrich ersetzen
else:
    item_url = configuration[1]

try:
    item_img = Image.open(f"res/items/{item_url}.png")  # versuchen, das Bild des Items zu laden
    item_img = item_img.convert("RGBA")
except FileNotFoundError:
    print(f"{configuration[1]} ist kein item in minecraft oder du hast dich verschrieben.")
    exit(1)

if item_url == "ender_pearl" or "sign" in item_url or "egg" in item_url:
    count_img = Image.open("res/count16.png")  # wenn ein Stack 16 ist
else:
    count_img = Image.open("res/count64.png")  # wenn ein Stack 64 ist
count_img = count_img.convert("RGBA")

# Kisten-Typ abgleichen und das passende Bild laden
if configuration[0] == "big":
    rows = 6
    chest_img = Image.open("res/chest_big.png")
elif configuration[0] == "small":
    rows = 3
    chest_img = Image.open("res/chest_small.png")
chest_img = chest_img.convert("RGBA")

# check ob das Item sich überhaupt stacken lässt (z.B. Rüstung kann man nicht stacken)
for z in non_stackable_items:
    if z in item_url:
        non_stackable = True

# die Item-Bilder und "16" bzw. "64" in jeden Slot des Kisten-Menüs einfügen
for y in range(rows):
    for x in range(9):
        chest_img.paste(item_img, (x * 18 + 8, y * 18 + 8), item_img)
        if not non_stackable:
            chest_img.paste(count_img, (x * 18 + 8, y * 18 + 8), count_img)

# das fertige Bild speichern
chest_img.save("kiste.png", quality=100, format="png")
