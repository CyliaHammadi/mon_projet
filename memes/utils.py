# memes/utils.py

from PIL import Image, ImageDraw, ImageFont

def ajouter_texte_sur_image(image_path, text, output_image_path):
    """
    Ouvre l'image située à image_path, ajoute le texte en haut à gauche et sauvegarde l'image modifiée dans output_image_path.
    """
    # Ouvrir l'image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Définir une police (vous pouvez changer "arial.ttf" par une autre police disponible)
    try:
        font = ImageFont.truetype("arial.ttf", size=40)
    except IOError:
        # Si la police n'est pas disponible, utiliser la police par défaut
        font = ImageFont.load_default()

    # Ajouter le texte (position (10,10), couleur blanche)
    draw.text((10, 10), text, font=font, fill=(255, 255, 255))

    # Sauvegarder l'image modifiée
    img.save(output_image_path)