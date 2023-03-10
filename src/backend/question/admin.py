from django.contrib import admin
from .models import Question, Keypoint, UserKeypointScore, UserSubmission, Solution, Category

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')

class KeypointAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')

class SolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Keypoint, KeypointAdmin)
admin.site.register(UserKeypointScore)
admin.site.register(UserSubmission)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Category, CategoryAdmin)
