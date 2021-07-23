"""rangmanch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminsite import views
from clients import c_views

urlpatterns = [
    path('', c_views.client_index),
    path('admin/', admin.site.urls),
    path('adminlogin/', views.admin_login),
    path('dashboard/', views.admin_dashboard),
    path('adminform/',views.admin_form),
    path('adminprofile/', views.admin_profile),
    path('userstables/', views.users_table),
    path('bookevent-tables/', views.booking_tables),
    path('event-table/', views.services_table),
    path('category-table/', views.category_table),
    path('subcategory-table/', views.subcategory_table),
    path('event_edit/<int:event_id>/',views.event_edit),
    path('insert_event/',views.insert_event),
    path('update_event/<int:event_id>/',views.update_event),



    #===========================================================
    path('delete_event/<int:event_id>/',views.delete_event),
    path('delete_category/<int:category_id>/',views.delete_category),
    path('delete_subcategory/<int:subcat_id>/',views.delete_subcategory),

    # ===============================================================

    # clients  urls

    # -------------------------------------------------------------------
    path('clientprofile/',c_views.c_profile),
    path('clientindex/', c_views.client_index),
    path('contact-us/', c_views.client_contact),
    path('clientlogin/', c_views.client_login),
    path('clientmenu/', c_views.load_menu),
    path('clientreg/', c_views.register),
    path('clientf/', c_views.client_f),
    path('aboutus/', c_views.about_us),
    path('clientlogout/', c_views.clogout),
    path('event-detail/<int:event_id>/', c_views.event_detail),
    path('event-list/', c_views.event_list),
    path('event_list_bycate/<int:subcat_id>/', c_views.event_list_bycate),
    path('event_list_bysub_cate/<int:category_id>/', c_views.event_list_bysub_cate),

]
