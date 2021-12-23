from django.contrib import admin

from .models import Quiz, Slash


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
    list_display = ['answer', 'question']
    list_display_links = ['answer', 'question']
    inlines = [SlashInline]


admin.site.register(Quiz, QuizAdmin)

class SlashAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slash, SlashAdmin)