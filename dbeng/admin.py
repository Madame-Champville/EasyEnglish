from django.contrib import admin
from .models import Student, Teacher, Course, Attendance, Grade, Material, Schedule, Payment, Assessment
from datetime import datetime


@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ['get_row_number', 'first_name', 'last_name', 'phone', 'email', 'course', 'course_level', 'reg_date']
    search_fields = ['name',]
    list_filter = ['course',]

    def get_row_number(self, obj):
        queryset = Student.objects.all().order_by('-id')
        row_number = list(queryset).index(obj) + 1
        return row_number

    get_row_number.short_description = '№'

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'course']
    search_fields = ['name', ]
    list_filter = ['course', ]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_level', 'course_duration', 'fee']
    search_fields = ['course_name', 'course_level']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'course_level', 'attendance_day', 'attendance_status']
    search_fields = ['student', 'course']

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'course_level', 'assessment_date', 'file']
    search_fields = ['student', ]

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'course_level', 'assessment', 'grade_day']
    search_fields = ['student', 'course', 'assessment']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['course', 'material_name', 'material_description']
    search_fields = ['course', 'material_name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['course', 'day_per_week', 'start_time', 'end_time', 'location']
    search_fields = ['course', 'start_time', 'location']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['get_row_number', 'student', 'course', 'course_level', 'payment_date', 'payment_amount']
    search_fields = ['student', 'payment_date']
    list_filter = ['course', 'payment_date'
                             '' ]

    def get_row_number(self, obj):
        queryset = Payment.objects.all().order_by('-id')
        row_number = list(queryset).index(obj) + 1
        return row_number

    get_row_number.short_description = '№'