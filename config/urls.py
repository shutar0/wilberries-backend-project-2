from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from products.views import (
    CategoryViewSet,
    SubCategoryViewSet,
    ProductViewSet,
)

from users.views import RegisterView

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/register/', RegisterView.as_view()),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]