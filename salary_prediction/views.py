from django.shortcuts import render

# Create your views here.


def prediction(request):
    if request.method == 'POST':
        domain = request.POST['domain']
        age = request.POST['age']
        print(domain, age)
        
    return render(request, 'prediction.html')