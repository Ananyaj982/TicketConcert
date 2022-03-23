from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

	path('list',views.level_list,name='level_list'),
	path('list/<level>',views.level_detail,name='level_detail'),
	path('<int:pk>',views.studentdetails,name='studentdetails'),
	
	path('register',views.register,name="register"),
    path('registered',views.registered,name="registered"),
    path('login', views.LoginView.as_view(),name="login"),
	path('logout/', views.logout_request,name="logout"),
	path('new', views.ticket_new, name='ticket_new'),
	path('pay',views.payment,name="payment"),
	path('credit/<int:pk>/',views.credit,name="credit"),
	path('success',views.success,name="success"),
	
	path('faq',views.doubt,name="doubt"),
	path('addfaq',views.faq,name="faq"),
	path('question/new',views.question_new,name="question_new"),
	path('question/<int:pk>',views.ansquestion,name="ansquestion"),
	path('question/<pk>/remove/',views.question_remove, name='question_remove'),
	path('faq/<pk>/remove/',views.faq_remove, name='faq_remove'),
	
	path('',views.index,name="index"),
	path('logout/', views.logout_request,name="logout"),
	
]