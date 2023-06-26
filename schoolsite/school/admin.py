from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse, path
from django.utils.html import format_html
from users.views import students_courses_report

from users.models import *
from .models import *

admin.site.register(Teacher)
# admin.site.register(Lesson)
admin.site.register(School)
admin.site.register(Course)
admin.site.register(CourseRegistration)
# admin.site.register(CustomUser)
# admin.site.unregister(Attendance_of_classes)
# admin.site.register(Student_performance)

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    # fieldsets = ()
    fieldsets = (
            (None, {'fields': ('wishes', 'phone_number', 'grade')}),
    ) + UserAdmin.fieldsets


admin.site.register(CustomUser, MyUserAdmin)

class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'teacher', 'get_student_first_name', 'get_student_last_name')

    def get_student_first_name(self, obj):
        return obj.student.first_name

    def get_student_last_name(self, obj):
        return obj.student.last_name




admin.site.register(Attendance)


# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'view_courses_report')
#
#     def view_courses_report(self, obj):
#         url = reverse('students-courses-report-excel')
#         return format_html('<a href="{}?student_id={}">Download Courses Report</a>', url, obj.id)
#
# class ReportAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/report_change_list.html'
#
#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             path('generate_report/', self.generate_report),
#         ]
#         return my_urls + urls
#
#     def generate_report(self, request):
#         students_courses_report()
#         url = reverse('admin:%s_%s_changelist' % (self.model._meta.app_label, self.model._meta.model_name))
#         return HttpResponseRedirect(url)
#
#     def changelist_view(self, request, extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['generate_report_url'] = reverse('admin:%s_%s_generate_report' % (self.model._meta.app_label, self.model._meta.model_name))
#         return super().changelist_view(request, extra_context=extra_context)

