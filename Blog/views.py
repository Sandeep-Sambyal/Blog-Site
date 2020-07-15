from django.shortcuts import render,redirect
from django.http import HttpResponse
from Blog.models import blogpost,Blogcomment
from django.contrib import messages
from Blog.templatetags import extra
# Create your views here.



def blogs(request,slug):
    var=blogpost.objects.filter(slug=slug).first()
    var.views=var.views+1
    
    var.save()
    comment=Blogcomment.objects.filter(post=var,parent=None)
    childcomment=Blogcomment.objects.filter(post=var).exclude(parent=None)
    replydict={}
    for x in comment:
        print(x.sno)
    for reply in childcomment:
        print(reply.parent.sno)
        
        if reply.parent.sno not in replydict:
            replydict[reply.parent.sno]=[reply]
        else:
            replydict[reply.parent.sno].append(reply)
    print("replydict :",replydict)
    content={'post':var,'comment':comment,'user':request.user,'childcomments':replydict}
    return render(request,'blog/blogfile.html',content)

def search(request):
    search=request.GET.get("search")
    titlecontains=blogpost.objects.filter(title__icontains=search)
    contentcontains=blogpost.objects.filter(desc__icontains=search)
    authorcontains=blogpost.objects.filter(author__icontains=search)
    val=titlecontains.union(contentcontains,authorcontains)
    content={'allposts':val,'query':search}
    return render(request,'blog/search.html',content)

def commenthandler(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        slug=request.POST.get("slug")
        id=request.POST.get("postid")
        print("POST ID ",id)
        user=request.user
        post=blogpost.objects.filter(id=id).first()
        parentsno=request.POST.get("parentsno")
        if parentsno=="":
            val=Blogcomment(comment=comment ,user=user ,post=post )
            val.save()
            messages.success(request,'Comment Updated.')
        else:
            link=Blogcomment.objects.get(sno=parentsno)
            val=Blogcomment(comment=comment ,user=user ,post=post,parent=link )
            val.save()
            messages.success(request,'Reply Updated.')   
        
        return redirect(f'/blog/blogpost/{slug}')
    else:
        return HttpResponse("Error 404- Forbidden Access.")
    



    

    
