from django.urls import path
from .views import SignUpView, Reset_Password_View, Reset_Password_Done_View


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('reset/', Reset_Password_View, name='reset'),
    path('reset_done/', Reset_Password_Done_View, name='reset_done')
]
