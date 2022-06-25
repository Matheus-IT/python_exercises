from django.urls import path, re_path
from matrix_app import views

urlpatterns = [
    path('', views.matrix_index_view),
    re_path(
        r'operation/(?P<op>add|sub|mul|div|inv)/', views.matrix_operation_view
    ),
]
