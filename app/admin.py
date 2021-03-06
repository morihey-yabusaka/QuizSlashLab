from re import search
from django.contrib import admin

from .models import Quiz, Slash, GoodQuiz


class SlashInline(admin.TabularInline):
    model = Slash
    can_delete = False
    fieldsets = (
        (None, {
            'fields': (
                'slash_position',
                'before_just',
                'n_push',
                'n_correct',
                'n_uncorrect'
            ),
        }),
    )
    readonly_fields = (
        'slash_position',
        'before_just',
        'n_push',
        'n_correct',
        'n_uncorrect'
    )
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    list_display = ('is_publish', 'is_draft', 'is_official' , 'answer', 'question', 'author', 'updated_at', 'created_at')
    list_display_links = ('answer', 'question')
    list_editable = ('is_publish', 'is_draft', 'is_official')
    list_filter = ('is_publish', 'is_draft', 'is_todays_question')
    search_fields = ('answer', 'question', 'author')
    inlines = [SlashInline]
    save_on_top = True


admin.site.register(Quiz, QuizAdmin)

class SlashAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slash, SlashAdmin)


class GoodQuizAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'user',
                'quiz',
                'created_at',
            ),
        }),
    )
    readonly_fields = ('user', 'quiz', 'created_at')
    list_display = ('user', 'quiz', 'created_at')

admin.site.register(GoodQuiz, GoodQuizAdmin)