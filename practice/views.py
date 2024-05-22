from django.http import HttpResponse
from django.shortcuts import render


def index(request): #// we use request variable as convection but you can use any name 
    return render(request,'index.html')
    # return HttpResponse("index")


def analyze(request):
    dataanalyze=request.POST.get('textareaData',"default")
    punc=request.POST.get('checkboxAnalyze',"off")
    upperCase=request.POST.get('checkboxUppercase','off')
    print(punc)
    analyzedtext=""
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if punc=="on" and upperCase == "on":
        analyzedtext=""
        for char in dataanalyze:
            if char not in punctuation:
                analyzedtext=analyzedtext+char.upper()
        

    elif punc=="on":
        analyzedtext=""
        for char in dataanalyze:
            if char not in punctuation:
                analyzedtext=analyzedtext+char
        analyzedtext.upper()
    
    elif upperCase=="on":
        analyzedtext=dataanalyze.upper()
    else:
        analyzedtext=dataanalyze
        
        
    params={"name":"removed punctuation","analyzedtext" :analyzedtext}
    return render(request,"about.html",params)

# def contact(request):
#     return HttpResponse("contact")

def about(hello):
    return HttpResponse("<em>my seconed apps</em>")