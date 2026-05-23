from rest_framework.viewsets import ModelViewSet
from .models import Category, SubCategory, Product
from .serializers import (
    CategorySerializer,
    SubCategorySerializer,
    ProductSerializer
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filterset_fields = ['subcategory']
    search_fields = ['title']
    ordering_fields = ['price', 'created_at']