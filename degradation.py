from PIL import Image
import math

img = Image.open("assets/room1.png")
pixels = img.load()
width, height = img.size

print(f"image chargée : {width}x{height}")



def vignette(image, center_x, center_y, radius, intensity=1.0, block_size=8):
    """
    Assombrit les pixels par BLOCS en fonction de la distance au centre.
    block_size = taille des blocs (8 = effet pixelisé)
    """
    img_copy = image.copy()
    pixels = img_copy.load()
    w, h = img_copy.size
    
    for y in range(h):
        for x in range(w):
            # Arrondir la position au bloc le plus proche
            bx = (x // block_size) * block_size + block_size // 2
            by = (y // block_size) * block_size + block_size // 2
            
            # Distance du BLOC au centre (pas du pixel)
            distance = math.sqrt((bx - center_x)**2 + (by - center_y)**2)
            
            # Facteur d'assombrissement
            if distance < radius:
                factor = (distance / radius) * intensity
            else:
                factor = intensity
            
            # Appliquer
            r, g, b = pixels[x, y][:3]
            r = int(r * (1 - factor))
            g = int(g * (1 - factor))
            b = int(b * (1 - factor))
            pixels[x, y] = (r, g, b)
    
    return img_copy

# Test avec blocs de 8 pixels
img_vignette = vignette(img, center_x=192, center_y=192, radius=150, intensity=1.0, block_size=16)
img_vignette.save("assets/test_vignette.png")
print("✓ test_vignette.png créé")