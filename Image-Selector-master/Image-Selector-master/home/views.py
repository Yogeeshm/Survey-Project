from django.shortcuts import render
from home.models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        education=request.POST.get('education')
        location=request.POST.get('location')
        living_in=request.POST.get('living')
        occupation=request.POST.get('occupation')
        annual_income=request.POST.get('annual_income')
        comments=request.POST.get('comments')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        email=request.POST.get('email')
        curr_location=request.POST.get('curr_location')
        ip_address=request.POST.get('ip_address')
        

        res=User(name=name,education=education,location=location,living_in=living_in,occupation=occupation,annual_income=annual_income,comments=comments,sex=sex,age=age,email=email,curr_location=curr_location,ip_address=ip_address,)
        res.save()
        print(request.POST.get('name'))
    return render(request , 'index.html')