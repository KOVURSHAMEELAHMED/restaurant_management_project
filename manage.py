urlpatterns = [

    path('categories/', MenuCategoryList.as_view(), name='category-list'),
]
