import PIL as pil
import PIL.Image
from PIL import Image

rows = 6
non_stackable = False
# Liste mit unstackable Items
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
                       "trident",
			     "totem_of_undying"]

print("Input: big / small (chest), item (der genaue name, statt unterstrich leertaste), scale")
eingabe = input()  # Input in 'eingabe' speichern
configuration = eingabe.split(", ")  # Kisten-Typ und Item speichern
if " " in configuration[1]:
    item_url = configuration[1].replace(" ", "_")  # Leerzeichen mit Unterstrich ersetzen
else:
    item_url = configuration[1]

if len(configuration) == 2:
    scale = 1
else:
    scale = configuration[2]

chest_size = configuration[0]

try:
    item_img = Image.open(f"res/items/{item_url}.png")  # versuchen, das Bild des Items zu laden
    item_img = item_img.convert("RGBA")
except FileNotFoundError:
    print(f"{configuration[1]} ist kein item in minecraft oder du hast dich verschrieben.")
else:

    if item_url == "ender_pearl" or "sign" in item_url or "egg" in item_url or "honey_bottle" in item_url:
        count_img = Image.open("res/count16.png")  # wenn ein Stack 16 ist
    else:
        count_img = Image.open("res/count64.png")  # wenn ein Stack 64 ist
    count_img = count_img.convert("RGBA")

    # Kisten-Typ abgleichen und das passende Bild laden
    if chest_size == "big":
        rows = 6
        chest_img = Image.open("res/chest_big.png")
    elif chest_size == "small":
        rows = 3
        chest_img = Image.open("res/chest_small.png")
    chest_img = chest_img.convert("RGBA")

    # checkt ob das Item sich überhaupt stacken lässt (z.B. Rüstung kann man nicht stacken)
    for z in non_stackable_items:
        if z in item_url:
            non_stackable = True
    # bow ist in der Liste der unstackable Items (für bow, crossbow, usw.), aber in bowl ist bow, deswegen für bowl trotzdem stackable setzen
    if item_url == "bowl":
        non_stackable = False

    # die Item-Bilder und "16" bzw. "64" in jeden Slot des Kisten-Menüs einfügen
    for y in range(rows):
        for x in range(9):
            chest_img.paste(item_img, (x * 18 + 8, y * 18 + 8), item_img)
            if not non_stackable:
                chest_img.paste(count_img, (x * 18 + 8, y * 18 + 8), count_img)

    # das Bild mit scale vergräßern
    width, height = chest_img.size
    output_img = chest_img.resize((int(width) * int(scale), int(height) * int(scale)), resample=Image.Resampling.NEAREST)

    # die schärfe verbessern und das Bild speichern
    output_img.save("kiste.png", quality=200, format="png")
