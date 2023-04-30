from django.urls import path

from . import views

app_name = 'shootout'
urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('<int:expression_id>/delete/', views.delete, name='delete'),
    path('recentExpressions/', views.recent_expressions, name='recent_expressions'),
    path('undefinedExpressions/', views.undefined_expressions, name='undefined_expressions'),
    path('disagreeingResults/', views.disagreeing_results, name='disagreeing_results'),
    path('expressionsByOperator/', views.expressions_operator, name='expressions_operator'),
    path('plan/', views.plan, name='plan'),
]
