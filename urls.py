from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('login/',views.login),
    path('user_reg/',views.user_reg),
    path('doctor_reg/',views.doctor_reg),
    path('logout/',views.logout),


    #Admin
    path('admin_home/',views.admin_home),
    path('admin_view_users/',views.admin_view_users),
    path('admin_view_doctors/',views.admin_view_doctors),
    path('admin_user_approve/',views.admin_user_approve),
    path('admin_user_reject/',views.admin_user_reject),
    path('admin_approved_users/',views.admin_approved_users),
    path('admin_rejected_users/',views.admin_rejected_users),
    path('admin_doctor_approve/',views.admin_doctor_approve),
    path('admin_doctor_reject/',views.admin_doctor_reject),
    path('admin_approved_doctor/',views.admin_approved_doctor),
    path('admin_rejected_doctor/',views.admin_rejected_doctor),
    path('admin_view_questions/',views.admin_view_questions),
    path('admin_feedback/',views.admin_feedback),
    path('admin_view_result/',views.admin_view_result),
    path('resultpdf/',views.resultpdf),
    path('forward/',views.forward),
    path('remove_normal_user/',views.remove_normal_user),
    path('admin_view_report/',views.admin_view_report),  

    #User
    path('user_home/',views.user_home),
    path('user_feedback/',views.user_feedback),
    path('user_profile/',views.user_profile),
    path('user_selfcorner/',views.user_selfcorner),
    path('user_editprofile/',views.user_editprofile),
    path('user_view_selfcorner/',views.user_view_selfcorner),
    path('user_test/',views.user_test),
    path('user_remove_self/',views.user_remove_self),

    #Doctor
    path('doctor_profile/',views.doctor_profile),
    path('doctor_home/',views.doctor_home),
    path('doctor_edit_profile/',views.doctor_edit_profile),
    path('doctor_feedback/',views.doctor_feedback),
    path('doctor_view_patient/',views.doctor_view_patient),
    path('doctor_add_report/',views.doctor_add_report),
    path('doctor_mail/',views.doctor_mail),





















    


]
