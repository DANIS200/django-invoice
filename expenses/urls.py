from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns =[
    path('', views.index, name="expenses"),
    path('add-expense', views.add_expense, name="add-expenses"),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('search_expenses', csrf_exempt(views.search_expenses),
        name="search_expenses"),
    path('export_csv', views.export_csv,
         name="export-csv"),
    path('export_excel', views.export_excel,
        name="export-excel"),
    path('export_pdf', views.export_pdf,
         name="export-pdf"),
    path('summary-by-category/', views.summary_by_category, name='summary_by_category'),
]