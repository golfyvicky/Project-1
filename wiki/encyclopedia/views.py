from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import util
from django import forms


class NewTaskForm(forms.Form):
    pagetitle = forms.CharField(max_length=200, label="New Page Title")
    pagecontent = forms.CharField(max_length=20000, label="New Page Content")

def index(request):
    if request.POST :
        
        #searchtag = request.POST.get("q")
        searchtagupper = request.POST.get("q").upper()
        
        entries = util.list_entries()
        entriesupper = [entry.upper() for entry in entries]
        
        if searchtagupper in entriesupper:
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

  
