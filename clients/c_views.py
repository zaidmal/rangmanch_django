from django.shortcuts import render,redirect
from adminsite.models import *
from django.contrib import messages
from adminsite.forms import *


# Create your views here.
def client_index(request):
    events = event.objects.all()
    return render(request, "index-1.html",{"events":events})

def event_detail(request,event_id):
    eve = event.objects.filter(event_id=event_id)
    pak = package.objects.filter(event_id=event_id)
    return render(request, "event-detail.html",{"eve":eve,"pak":pak})


def event_list(request):
    events = event.objects.all()
    return render(request, "event-list.html",{"events":events})


def c_profile(request):
    cid=request.session['customer_id']
    ue=users.objects.get(user_id=cid)
    return render(request,"profile.html",{"u":ue})


def event_list_bycate(request,subcat_id):
    events = event.objects.filter(subcat_id=subcat_id)
    return render(request, "event-list.html",{"events":events})

def event_list_bysub_cate(request,category_id):
    even = categorys.objects.filter(category_id=category_id)
    events = event.objects.filter(sub_categorys_id__in=even)
    return render(request, "event-list.html",{"events":events})




def client_contact(request):
    return render(request, "c-contactus.html")

def client_f(request):
    return render(request, "forgot.html")

def about_us(request):
    return render(request, "c-aboutus.html")




def register(request):
    if request.method == "POST":
        froms = RegisterFroms(request.POST)

        print("===resgidskd============FROMS ERRORS", froms.errors)
        if froms.is_valid():
            # newform = froms.save(commit=False)
            # newform.users_password = hashlib.md5(newform.users_password.encode('utf')).hexdigest()

            froms.save()
            return redirect("/clientindex/")
        else:
            pass
    else:
        froms = RegisterFroms()

    return render(request, "index-1.html", {"froms": froms,})


def load_menu(request):
    c=categorys.objects.all()
    sue=subcategory.objects.all()
    return render(request,"c_menu.html",{"c":c,"sc":sue})



def client_login(request):
    if request.method == "POST":
        u_email = request.POST["email"]
        p_email = request.POST["password"]
        val = users.objects.filter(user_email=u_email, user_password=p_email).count()
        if val == 1:
            data = users.objects.filter(user_email=u_email, user_password=p_email)
            for n in data:
                request.session['customer_id'] = n.user_id
                request.session['customer_email'] = n.user_email
                request.session['customer_pwd'] = n.user_password

            return redirect("/clientindex/")
        else:
            messages.error(request, "Invaild password and email")
            return redirect("/clientindex/")





def clogout(request):
    try:
        del request.session['customer_id']
        del request.session['customer_email']
        del request.session['customer_pwd']
        return redirect("/clientindex/")
    except:
        pass
    return redirect("/clientlogin/")
