from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import util
from django import forms


class NewTaskForm(forms.Form):
    pagetitle = forms.CharField(max_length=200, label="Page Title")
    #pagecontent = forms.CharField(max_length=20000, label="New Page Content")
    #pagecontent = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}),label="Page Content")
    pagecontent = forms.CharField(widget=forms.Textarea(attrs={'cols': 50}),label="Page Content")

def index(request):
    if (request.POST and request.POST.get("q") !="") :
        
        searchtagupper = request.POST.get("q").upper()
        entries = util.list_entries()
        entriesupper = [entry.upper() for entry in entries]
        
        if searchtagupper in entriesupper:
            
            searchtag = request.POST.get("q")
           
            return render(request, "encyclopedia/searchresult.html",{
                "pagetitle" : searchtagupper,
                "page": util.get_entry(request.POST.get("q"))
            })
        else:
            return render(request, "encyclopedia/error.html",{
                "searchtag" : request.POST.get("q")
            })
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def checkentry(request, name):
    if name == 'add':
        add(request)
    if (util.get_entry(name) == None):
        return render(request, "encyclopedia/error.html",{
            "nametitle":name
        })
    else:
        return render(request, "encyclopedia/searchresult.html",{
            "pagetitle" : name,
            "page": util.get_entry(name)
    })
        
def add(request):

    form = NewTaskForm()

    if request.method=="POST":
        form = NewTaskForm(request.POST)

        if form.is_valid():
            pagetitle = form.cleaned_data["pagetitle"]
            pagecontent = form.cleaned_data["pagecontent"]
            util.save_entry(pagetitle,pagecontent)
            return render(request,"encyclopedia/index.html",{
            "entries": util.list_entries()
        })
    
    else:
        return render(request,"encyclopedia/add.html",{
            "form":form
        })

def edit(request):
    if (request.POST) :
        #form = NewTaskForm(request.POST)
        pagetitle = request.session["pagetitle"]
        pagecontent = request.session["title"]
        #form.pagecontent = util.get_entry(form.pagetitle)
        """if form.is_valid():
            pagetitle = form.cleaned_data['pagetitle']
            pagecontent = form.cleaned_data['pagecontent']
            #form.pagetitle = "pagetitle"
            #form.pagecontent = "pagecontent"
            """
        return render(request,"encyclopedia/add.html",{
            "form":form
        })
    else: 
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })    
    
