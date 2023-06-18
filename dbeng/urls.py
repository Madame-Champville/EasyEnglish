from django.urls import path

from . import views

urlpatterns = [
    path('', views.user, name='student_list'),
    path('enroll/', views.enroll, name='enroll'),
    path('teacher/', views.teacher, name='employee'),
    path('assessment/', views.assessment, name='assessment'),
    path('about/', views.AboutList.as_view(), name='about_list'),
    path('blogs/', views.BlogsList.as_view(), name='blogs_list'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('eng-test/', views.EngTestList.as_view(), name='eng-test_list'),
    path('courses/', views.CoursesList.as_view(), name='courses_list'),
    path('course-inner/', views.CourseInnerList.as_view(), name='course-inner_list'),
    path('course-inner_individual/', views.CourseInnerIndividualList.as_view(), name='course-inner_individual_list'),
    path('contact/', views.ContactList.as_view(), name='contact_list'),
]