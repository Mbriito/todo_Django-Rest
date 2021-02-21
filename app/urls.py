from app.views import TodoListAndCreate, todo_detail_change_delete      

from django.urls import path


urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', todo_detail_change_delete),

]