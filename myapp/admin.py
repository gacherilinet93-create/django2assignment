from django.contrib import admin
from .models import Student, Payment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'created_at')
    search_fields = ('name', 'email', 'course')
    list_filter = ('course',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('phone', 'amount', 'status', 'mpesa_receipt', 'created_at')
    list_filter = ('status',)