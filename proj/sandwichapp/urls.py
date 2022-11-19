from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsListView, SandwichGeneratorView, MenuView

urlpatterns = [
    # sandwich/
    path('', SandwichappView.as_view(), name='sandwich'),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view()),
    path('menu', MenuView.as_view())
]
