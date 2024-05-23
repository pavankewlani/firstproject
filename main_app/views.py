from django.shortcuts import render
from django.views import View

# Create your views here.


def index(request):
    if request.method == "GET":
        data = request.GET
        if data:
            pass
    else:
        print("I am post")
        data = request.POST    
        print('➡ main_app/views.py:14 data:', data)
    return render(request, "login.html")



class IndevView(View):
    template = "login.html"

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        print('➡ main_app/views.py:28 request.POST:', request.POST)
        return render(request, self.template)

