import sys

from django.shortcuts import render, redirect
from adminsite.models import *
from django.contrib import messages
from adminsite.forms import *
from adminsite.functions import handle_uploaded_file

# Create your views here.
def users_table(request):
    s = users.objects.all()
    return render(request, "users-table.html", {"users": s})



def booking_tables(request):
    s = bookevent.objects.all()
    return render(request, "bookevent-table.html", {"bevent": s})


def package_tables(request):
    s = package.objects.all()
    return render(request, "package-table.html", {"package1": s})


def services_table(request):
    s = event.objects.all()
    return render(request, "services-table.html", {"events": s})


def category_table(request):
    s = categorys.objects.all()
    return render(request, "category-table.html", {"category": s})


def subcategory_table(request):
    s = subcategory.objects.all()
    return render(request, "subcategory-table.html", {"subcat": s})


# =======================================insert
def insert_event(request):
    scat = subcategory.objects.all()
    if request.method == "POST":
        forms = eventForms(request.POST, request.FILES)
        print("==Docter============FROMS ERRORS", forms.errors)
        if forms.is_valid():
            handle_uploaded_file(request.FILES['event_image'])
            forms.save()
            return redirect("/event-table/")
        else:
            pass
    else:
        forms = eventForms()

    return render(request, "insert_event.html", {"forms": forms,"scat":scat})



def insert_category(request):
    scat = subcategory.objects.all()
    if request.method == "POST":
        forms = catFroms(request.POST)
        print("==Event============FROMS ERRORS", forms.errors)
        if forms.is_valid():
            forms.save()
            return redirect("/category-table/")
        else:
            pass
    else:
        forms = catFroms()
    return render(request, "insert_category.html",{"forms": forms})


def insert_sub_category(request):
    cat = categorys.objects.all()
    if request.method == "POST":
        forms = subcategoryFroms(request.POST)
        print("==Event============FROMS ERRORS", forms.errors)
        if forms.is_valid():
            forms.save()
            return redirect("/subcategory-table/")
        else:
            pass
    else:
        forms = subcategoryFroms()
    return render(request, "insert_subcat.html",{"forms": forms,"cat":cat})

def insert_package(request):
    pack = package.objects.all()
    if request.method == "POST":
        forms = packageFroms(request.POST)
        print("==Event============FROMS ERRORS", forms.errors)
        if forms.is_valid():
            forms.save()
            return redirect("/package-table/")
        else:
            pass
    else:
        forms = packageFroms()
    return render(request, "insert_package.html",{"forms": forms,"pack":pack})


# ============================================delete
def delete_event(request,event_id):
    cate_d=event.objects.get(event_id=event_id)
    cate_d.delete()
    return redirect("/event-table/")


def delete_category(request,category_id):
    categ_d=categorys.objects.get(category_id=category_id)
    categ_d.delete()
    return redirect("/categorys-table/")

def delete_subcategory(request,subcat_id):
    subcat_d=subcategory.objects.get(subcat_id=subcat_id)
    subcat_d.delete()
    return redirect("/subcategory-table/")

def delete_package(request,pack_id):
    pack_d=package.objects.get(pack_id=pack_id)
    pack_d.delete()
    return redirect("/package-table/")





# ===================================================update
def event_edit(request,event_id):
    ev=event.objects.get(event_id=event_id)
    scat= subcategory.objects.all()
    return render(request,"update_event.html",{"scat":scat,"ev":ev})



def update_event(request, event_id):
    ev = event.objects.get(event_id=event_id)
    scat = subcategory.objects.all()
    froms = eventForms(request.POST, request.FILES, instance=ev)
    print("===update_docter-from== errors====", froms.errors)
    if froms.is_valid():
        try:
            handle_uploaded_file(request.FILES['event_image'])
            froms.save()

            return redirect("/event-table/")
        except:
            print("================", sys.exc_info())
    else:
        pass

    return render(request,"update_event.html",{"scat":scat,"ev":ev})





def admin_login(request):
    if request.method == "POST":
        u_email = request.POST["email"]
        p_email = request.POST["password"]
        admin = 1
        val = users.objects.filter(user_email=u_email, user_password=p_email, is_admin=1).count()
        if val == 1:
            return redirect("/dashboard/")
        else:
            messages.error(request, "Invaild password and email")
            return render(request, "admin_login.html")
    else:
        return render(request, "admin_login.html")


def admin_profile(request):
    return render(request, "admin_profile.html")

def admin_dashboard(request):
    s = users.objects.all()
    return render(request, "adminDashboard.html",{"users":s})

def admin_form(request):
    return render(request, "adminForm.html")
