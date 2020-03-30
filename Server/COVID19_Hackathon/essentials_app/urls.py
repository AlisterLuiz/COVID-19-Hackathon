from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
# router.register(r'places', views.matchData)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('', views.matchData, name='home-page'),
#     url(r'^signup/$', views.SignUpView.as_view(), name='signup')
# ]

urlpatterns = [
    path('shop/<str:category>/', views.ShopPageCategory.as_view()),
    path('shop/admin', views.AdminPageView.as_view()),
    path('shop/<str:category>/<int:shopId>/', views.ShopPageView.as_view()),
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]

   
