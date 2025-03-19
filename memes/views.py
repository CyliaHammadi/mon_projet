import os
from django.conf import settings
from django.shortcuts import render
from .form import ImageForm
from .models import Image
from .utils import ajouter_texte_sur_image
from django.shortcuts import render, get_object_or_404

import json
import base64
from django.http import JsonResponse, HttpResponseNotAllowed
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def gallery_add(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        image_data = data.get('image', None)
        if image_data:
            # Décode l'image encodée en base64
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            image_file = ContentFile(base64.b64decode(imgstr), name='modif_meme.' + ext)
            
            # Créer un nouvel objet Image en sauvegardant l'image modifiée dans le champ modif_image
            meme = Image.objects.create(modif_image=image_file, caption="Meme ajouté")
            return JsonResponse({'message': 'Image ajoutée à la galerie'})
    return HttpResponseNotAllowed(['POST'])



def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Sauvegarde de l'image et mise à jour du modèle
            obj = form.save(commit=False)
            obj.caption = os.path.basename(obj.image.name)  # Définir le nom de l'image dans caption
            obj.text = ""  # On ne renseigne pas le texte ici
            obj.save()
            
            # Construction du chemin de l'image originale
            image_path = os.path.join(settings.MEDIA_ROOT, obj.image.name)
            
            # Définir le dossier de sortie pour les images modifiées
            output_dir = os.path.join(settings.MEDIA_ROOT, 'modif_images')
            os.makedirs(output_dir, exist_ok=True)
            
            # Créer le nom et le chemin de l'image modifiée
            image_name = os.path.basename(obj.image.name)
            output_image_name = "modif_" + image_name
            output_image_path = os.path.join(output_dir, output_image_name)
            
            # Générer l'image sans texte initial
            ajouter_texte_sur_image(image_path, "", output_image_path)
            
            # Construire l'URL de l'image modifiée
            modif_image_url = os.path.join(settings.MEDIA_URL, 'modif_images', output_image_name)
            
            return render(request, "memes/modif.html", {"obj": obj, "modif_image_url": modif_image_url})
    else:
        form = ImageForm()
    return render(request, "memes/index.html", {"form": form})



def update_meme(request, pk):
    obj = get_object_or_404(Image, pk=pk)
    if request.method == "POST":
        # Récupérer le nouveau texte saisi
        new_text = request.POST.get("text", "")
        obj.text = new_text
        obj.save()

        # Chemin de l'image originale
        image_path = os.path.join(settings.MEDIA_ROOT, obj.image.name)

        # Définition du dossier de sortie
        output_dir = os.path.join(settings.MEDIA_ROOT, 'modif_images')
        os.makedirs(output_dir, exist_ok=True)

        # Création du nom et chemin de l'image modifiée
        image_name = os.path.basename(obj.image.name)
        output_image_name = "modif_" + image_name
        output_image_path = os.path.join(output_dir, output_image_name)

        # Appel de la fonction pour ajouter le texte sur l'image
        ajouter_texte_sur_image(image_path, new_text, output_image_path)

        # Construction de l'URL de l'image modifiée
        modif_image_url = os.path.join(settings.MEDIA_URL, 'modif_images', output_image_name)

        return render(request, "memes/modif.html", {"obj": obj, "modif_image_url": modif_image_url})
    else:
        # Pour une requête GET, on affiche simplement la page sans modification
        image_name = os.path.basename(obj.image.name)
        output_image_name = "modif_" + image_name
        modif_image_url = os.path.join(settings.MEDIA_URL, 'modif_images', output_image_name)
        return render(request, "memes/modif.html", {"obj": obj, "modif_image_url": modif_image_url})






def gallery(request):
    memes = Image.objects.exclude(modif_image='')  # ou modif_image__isnull=False
    return render(request, "memes/gallery.html", {"gallery_images": memes})
