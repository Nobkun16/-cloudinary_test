from django.shortcuts import render
from .models import IMG
from django.http import JsonResponse
# Create your views here.


def upload_img(request):
    imgs=''
    if request.method == 'POST':
        img=request.FILES.get("img")
        imgs=IMG(img=img)
        imgs.save()
        print("Image uploaded to:", imgs.img.url)
        return render(request, "upload_img/index.html",{
        'reply':imgs.img.url,
        'storage_type': type(imgs.img.storage),
        'img':imgs.img
    })
    return render(request, "upload_img/index.html",{

    })

import cloudinary.uploader

def test_cloudinary(request):
    result = cloudinary.uploader.upload("path/to/sample.jpg")
    return JsonResponse(result)

