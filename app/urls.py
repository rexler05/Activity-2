from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePageView,
                    AboutPageView,
                    ContactPageView,
                    PetCreateView,
                    PetListView,
                    PetDetailView,
                    PetUpdateView,
                    PetDeleteView
                    )
urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('', PetListView.as_view(), name='pets'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('pets/create/', PetCreateView.as_view(), name='pet_create'),
    path('pets/<int:pk>/edit/', PetUpdateView.as_view(), name='pet_update'),
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




