from django.urls import path

from .views import *

urlpatterns = [
    path('',index),
    path('login/',login),
    path('login/register/',regis),
    path('success/',success),
    path('verify/<auth_token>',verify),
    path('error/',error),
    path('usrlogin/',usrlogin),
    path('usrlogin/usrregister/',usrregister),
    path('edituser/<int:id>',edit_user),
    path('postjob/<int:id>',postjob),
    path('viewjobs/<int:id>',viewjob),
    path('jobd/<int:id1>/<int:id2>',jobdet),
    path('applyjob/<int:comid>/<int:userid>',jobapply),
    path('application/<int:id>',applied),
    path('viewcom/',viewcompany),
    path('jobapplied/<int:id>',japplied),
    path('sendm/<int:id>',sendmail)
    ]