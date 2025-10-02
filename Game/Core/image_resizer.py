from PIL import Image
import os

# pasta de entrada e saída
input_folder = r"C:\Users\User\Desktop\Drakoria\Drakoria\Game\Assets\UIs\UI_Game\Profile"
output_folder = r"C:\Users\User\Desktop\Drakoria\Drakoria\Game\Assets\UIs\UI_Inventory"

# cria a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# novo tamanho
new_size = (200, 100)

for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # redimensiona
        img_resized = img.resize(new_size, Image.NEAREST)  # NEAREST = mantém pixel art sem borrar

        # salva
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)

print("✅ Todas as imagens foram redimensionadas!")
