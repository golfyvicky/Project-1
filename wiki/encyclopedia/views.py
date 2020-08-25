from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def checkentry(request, name):
    #name1=util.get_entry(name)
    if (util.get_entry(name)==None):
        return render(request, "encyclopedia/error.html",{
            "nametitle":name
        })
    else:    
        return render(request, "encyclopedia/test.html",{
            "nametitle" : name,
            "name": util.get_entry(name)
        })
        
    

