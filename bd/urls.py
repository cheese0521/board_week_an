from django.urls import path
from . import views

app_name = "board"
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<num>', views.detail, name="detail"),
    path('delete/<num>', views.delete, name="delete"),
    path('update/<num>', views.update, name="update"),
    path('up/<conid>/<st>', views.up, name="up"),
    path('create_reply/<conid>', views.create_reply, name="create_reply"),
    path('rep_up/<conid>/<num>/<st>', views.rep_up, name="rep_up")
]
