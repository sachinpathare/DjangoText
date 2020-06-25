from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def removespace(request):
    djtext=request.GET.get('text', 'default')
    removespace = request.GET.get('removespace', 'off')
    upper = request.GET.get('upper', 'off')
    if removespace=='on' and upper=='on':
        return HttpResponse("<script>alert('I am an alert box!');</script>")
    elif removespace=='on':
        spacecut=djtext.replace(" ", "")
        params={'Utext':djtext,'output':spacecut}
        return render(request,'removespace.html',params)
    elif upper =='on':
        spacecut = djtext.upper()
        params = {'Utext': djtext, 'output': spacecut}
        return render(request, 'removespace.html', params)

    else:
        return HttpResponse("Error")

def about(request):
    return render(request,"about.html")
def contact(request):
    return  HttpResponse("<h1>this is contact</h1>")