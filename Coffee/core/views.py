from django.shortcuts import render, HttpResponse
from .forms import ImageForm
from .models import Image

# Homepage view

def homepage(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if(form.is_valid()):
            clean = form.cleaned_data
            pc = Image(upload_image = clean['upload_image'])
            pc.save()
    
    else:
        print('in else ')
        form = ImageForm()
    return render(request, 'core/index.html', {'form':form})


def handle_uploaded(file):
    print(type(file))
    return