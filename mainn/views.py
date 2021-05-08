from django.shortcuts import render,HttpResponse,redirect
from mainn.models import Contract
from datetime import datetime
import requests
from urllib.request import urlopen
from PIL import Image
from django.core.files.storage import FileSystemStorage


def index(request):
    context={
        'app':'ajajaj'
    }
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['picture']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        r = requests.post(
            "https://api.deepai.org/api/toonify",
            files={
                'image': open('media/'+uploaded_file.name, 'rb'),
            },
            headers={'api-key': 'f429f853-dfa2-4fd7-960d-95a7d7ce1c7b'}
        )
        link =str(r.json()['output_url'])
        linker={
            "link":link
        }
        return render(request, 'services.html',linker)
    linker={
        "link":"/static/default.png"
    }    
    return render(request, 'services.html',linker)    
 

def contract(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        descp = request.POST.get('password')
        rating = request.POST.get('rating')
        contract = Contract(email=email, descp=descp, date = datetime.now(), name = name,rating=rating)
        contract.save()
        return redirect('/responces')
    return render(request, 'contract.html')

def responces(request):
    contract = Contract.objects.all()
    contracter={
        "contract" : contract
    }

    return render(request, 'responces.html',contracter)

 