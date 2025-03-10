from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employee')

urlpatterns = [
    path('students/',views.studentsView),
    path('student/<int:pk>/',views.StudentDetailedView),
    # path('employees/',views.Employees.as_view()),
    # path('employee/<int:pk>/',views.EmployeeDetail.as_view()),
    path('', include(router.urls)),
    path('',include('blog.urls'))
]