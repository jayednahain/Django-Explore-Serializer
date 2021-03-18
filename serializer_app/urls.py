
from django.urls import path
from serializer_app import views

urlpatterns = [



   path('students/',views.studetn_list),
   path('students/<int:pk>',views.student_detail)

]
