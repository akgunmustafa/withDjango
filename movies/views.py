from django.shortcuts import render
from .models import Category, Movie

## kategori_Liste= ["macera","romantik","dram","bilim kurgu"]
"""
film_Liste = [
    {
        "id": 1,
        "film_adi": "film 1",
        "aciklama": "film 1 açıklama",
        "resim": "1.webp",
        "anasayfa": True
    },
    {
        "id": 2,
        "film_adi": "film 2",
        "aciklama": "film 2 açıklama",
        "resim": "2.webp",
        "anasayfa": True
    },
    {
        "id": 3,
        "film_adi": "film 3",
        "aciklama": "film 3 açıklama",
        "resim": "3.webp",
        "anasayfa": True
    },
    {
        "id": 4,
        "film_adi": "film 4",
        "aciklama": "film 4 açıklama",
        "resim": "4.webp",
        "anasayfa": False
    },
    {
        "id": 5,
        "film_adi": "film 5",
        "aciklama": "film 5 açıklama",
        "resim": "5.webp",
        "anasayfa": False
    }
    
]
"""


def home(request):
    data={
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.filter(anasayfa=True)
    }
    return render(request, "index.html", data) 

def movies(request):
    data={
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request,"movies.html", data)
def about(request):   
    return render(request,"about.html")
def moviedetails(request, id):
    data={
        "movie": Movie.objects.get(id=id)
    }
    return render(request,"details.html", data)
