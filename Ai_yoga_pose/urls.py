"""untitled URL Configuration

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

from Ai_yoga_pose import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('admin_home/',views.admin_home),
    path('addtrainer/',views.addtrainer),
    path('add_trainer_post/',views.add_trainer_post),
    path('edittrainer/<id>',views.edittrainer),
    path('edit_trainer_post/',views.edit_trainer_post),
    path('view_trainer/',views.view_trainer),
    path('viewtrainer_post/',views.viewtrainer_post),
    path('delete_trainer/<id>',views.delete_trainer),
    path('Logout/', views.Logout),
    path('Viewcomplaints/', views.Viewcomplaints),
    path('sendreplypost/', views.sendreplypost),
    path('view_approved_trainer_post/', views.view_approved_trainer_post),
    path('view_rejected_trainer_post/', views.view_rejected_trainer_post),
    path('view_approved_trainer/', views.view_approved_trainer),
    path('view_rejected_trainer/', views.view_rejected_trainer),
    path('approve_triner/<id>', views.approve_triner),
    path('reject_triner/<id>', views.approve_triner),
    path('approve_triner_new/<id>', views.approve_triner_new),
    path('reject_triner_new/<id>', views.reject_triner_new),
    path('Sendreply/<id>', views.Sendreply),

    ################################################## trainer ########################

    path('Trainer_view_profile/',views.Trainer_view_profile),
    path('reg/',views.reg),
    path('User_login_post/',views.User_login_post),
    path('User_signup_post/',views.User_signup_post),
    path('trainer_home/',views. trainer_home),
    path('trainer_Addtips/',views.Addtips),
    path('trainer_Addtips_post/',views.Addtips_post),
    path('trainer_Viewtips/',views.Viewtips),
    path('trainer_Viewtips_post/',views.Viewtips_post),
    path('email_exist/',views.email_exist),
    path('Edittips/<id>',views.Edittips),
    path('Deletetips/<id>',views.Deletetips),
    path('Edittips_post/',views.Edittips_post),
    path('User_Viewyogatrainers/',views.User_Viewyogatrainers),
    path('user_send_trainer_requests/',views.user_send_trainer_requests),
    path('viewrequests/',views.Viewrequest),
    path('approvereq/<id>',views.approvereq),
    path('rejectreq/<id>',views.rejectreq),
    path('Viewapprovedrequest/',views.Viewapprovedrequest),
    path('Viewrejectedrequest/',views.Viewrejectedrequest),
    path('viewrequest_post/',views.viewrequest_post),
    path("viewapprovedrequest_post/",views.viewapprovedrequest_post),
    path("viewrejectedrequest_post/",views.viewrejectedrequest_post),
    path("user_viewprofile/",views.user_viewprofile),
    path("user_editprofile/",views.user_editprofile),
    path("User_Viewmytrainers/",views.User_Viewmytrainers),
    path("User_Viewmyrequeststatus/",views.User_Viewmyrequeststatus),
    path("User_Viewyogatrainersearch/",views.User_Viewyogatrainersearch),
    path("Trainer_edit_profile/",views.Trainer_edit_profile),
    path("Trainer_edit_profile_post/",views.Trainer_edit_profile_post),
    path("deleted_trainer/",views.deleted_trainer),
    path("deleted_trainer_Post/",views.deleted_trainer_Post),
    path("user_add_diet_profile/",views.user_add_diet_profile),
    # path("user_edit_diet_profile/",views.user_edit_diet_profile),
    path("user_viewhealthprofile/",views.user_viewhealthprofile),
    path("user_edithealthprofile/",views.user_edithealthprofile),
    path("user_edit_diet_profile_Post/",views.user_edit_diet_profile_Post),
    path("Trainer_Adddietchart/",views.Trainer_Adddietchart),
    path("Trainer_Viewdietchart/",views.Trainer_Viewdietchart),
    path("Trainer_Editdietchart/<id>",views.Trainer_Editdietchart),
    path("Editdietchart_post/",views.Editdietchart_post),
    path("Trainer_Deletedietchart/<id>",views.Trainer_Deletedietchart),
    path("Adddietchart_post/",views.Adddietchart_post),
    path("Viewdietchart_post/",views.Viewdietchart_post),
    path("Trainer_add_diet_profile/",views.Trainer_add_diet_profile),
    path("Trainer_add_diet_profile_post/",views.Trainer_add_diet_profile_post),
    path("userhome/",views.userhome),
    path("yogapose/",views.yogapose),
    path("MySendComplaintPage/",views.MySendComplaintPage),
    path("chat1/<id>",views.chat1),
    path("chat_view/",views.chat_view),
    path("chat_send/<msg>",views.chat_send),
    path("User_sendchat/",views.User_sendchat),
    path("User_viewchat/",views.User_viewchat),
    path("Viewcomplaints/",views.Viewcomplaints),
    path("User_Viewreply/",views.User_Viewreply),
    path("Get_health_pr/",views.Get_health_pr),
    path("Viewcomplaintspost/",views.Viewcomplaintspost),
    path("User_Viewtips/",views.User_Viewtips),
    path("view_user/",views.view_user),
    path("MySendfeedbacktPage/",views.MySendfeedbacktPage),
    path("Viewfeedback/",views.Viewfeedback),
    path("Viewfeedbackspost/",views.Viewfeedbackspost),
    path("user_removetrainer/",views.user_removetrainer),
    path("Get_trainerhealth_pr/",views.Get_trainerhealth_pr),
    path("User_Viewtrainertips/",views.User_Viewtrainertips),



]
