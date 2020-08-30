from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import util


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
    if (util.get_entry(name) == None):
        return render(request, "encyclopedia/error.html",{
            "nametitle":name
        })
    else:
        return render(request, "encyclopedia/searchresult.html",{
            "pagetitle" : name,
            "page": util.get_entry(name)
    })
        
def search(request,searchtag):
    entries = util.list_entries()
    search_box = request.POST.get("q").capitalize()
    #search_box = searchtag.capitalize()

    if search_box in entries:
        return HttpResponseRedirect(f"wiki/{search_box}")

