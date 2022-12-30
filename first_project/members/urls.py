from django.urls import path
from members.views import MembersView

urlpatterns = [
    # path('first', views.members, name='members'),
    # path('name', views.members_name, name='members_name'),
    path('member', MembersView.as_view(), name='members_view'),
]