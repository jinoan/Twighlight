from django.urls import path
from . import views

# 경로 앱 이름 지정 'twighlight:???'
app_name = 'twighlight'

# twighlight/
urlpatterns = [
    path('', views.index, name='index'),
    path('streamer/', views.streamer, name='streamer'),
    path('streamer/<int:streamer_sid>/video/', views.video, name='video'),
    path('streamer/<int:streamer_sid>/video/<int:video_vid>/chat/', views.chat,  name='chat'),
]