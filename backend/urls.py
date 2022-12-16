from django.urls import path
from .views import *

urlpatterns = [
    path('events/', getEvents, name='events'),
    path('events/<str:pk>/', getEvent, name='event'),
    path('event/create/', createEvent, name='create-event'),
    path('events/<str:pk>/update/', updateEvent, name='update-event'),
    path('events/<str:pk>/delete/', deleteEvent, name='delete-event'),
    path('event/delete-all/', deleteAll, name='delete-all'),
    path('results/', getResults, name='results'),
    # path('month_results/', getMonthResults, name='month_results'),
    path('month_results/', createMonthResults, name='month_results'),
]