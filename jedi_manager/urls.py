from django.urls import path
from .views import IndexView
from .views import create_candidate #, candidates_list, CandidateDetail

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

]

# app_name = 'candidates'
#
# urlpatterns = [
#     path('create', create_candidate, name='create'),
#     # path('list', candidates_list, name='list'),
#     # path('<int:pk>', CandidateDetail.as_view(), name='detail')
# ]
