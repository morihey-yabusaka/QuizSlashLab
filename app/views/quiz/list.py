from django.db.models import Q
from django.views.generic import ListView

from ...models import Quiz

class QuizListView(ListView):
    model = Quiz
    context_object_name = 'quizes'
    ordering = ['-updated_at']
    template_name = "quiz/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_draft=False, is_publish=True)
        get = self.request.GET # type(self.request.GET) == dict
        question_query = get.get('question')
        question_oa_query = get.get('q')
        is_start_query = get.get('is_start')
        answer_query = get.get('answer')
        answer_oa_query = get.get('a')
        question_answer_oa_query = get.get('qa')

        qq = Q()
        if question_query:
            question_query.strip()
            if is_start_query:
                qq &= Q(question__istartswith=question_query)
            else:
                question_query_list = question_query.replace('　', ' ').split(' ')
                if 'or' == question_oa_query:
                    for i, qq_ in enumerate(question_query_list):
                        if i == 0:
                            qq &= Q(question__icontains=qq_)
                        else:
                            qq |= Q(question__icontains=qq_)
                elif 'and' == question_oa_query:
                    for qq_ in question_query_list:
                        qq &= Q(question__icontains=qq_)

        aq = Q()
        if answer_query:
            answer_query.strip()
            answer_query_list = answer_query.replace('　', ' ').split(' ')
            if 'or' == answer_oa_query:
                for i, aq_ in enumerate(answer_query_list):
                    if i == 0:
                        aq &= Q(answer__icontains=aq_)
                    else:
                        aq |= Q(answer__icontains=aq_)
            elif 'and' == answer_oa_query:
                for aq_ in answer_query_list:
                    aq &= Q(answer__icontains=aq_)

        q = Q()
        if 'or' == question_answer_oa_query:
            q &= qq | aq
        elif 'and' == question_answer_oa_query:
            q &= qq & aq

        queryset = queryset.filter(q)

        return queryset

    def get_context_data(self):
        context = super().get_context_data()

        context['title'] = [
            {'text': '最近更新された', 's': False},
            {'text': 'ク', 's': True},
            {'text': 'イズ', 's': False},
        ]

        get = self.request.GET
        question_oa_query = get.get('q')
        is_start_query = get.get('is_start')
        answer_oa_query = get.get('a')
        question_answer_oa_query = get.get('qa')

        if 'or' == question_oa_query:
            context['q_or'] = 'checked'
            context['q_and'] = ''
        else:
            context['q_or'] = ''
            context['q_and'] = 'checked'
        if 'or' == answer_oa_query:
            context['a_or'] = 'checked'
            context['a_and'] = ''
        else:
            context['a_or'] = ''
            context['a_and'] = 'checked'
        if 'or' == question_answer_oa_query:
            context['qa_or'] = 'checked'
            context['qa_and'] = ''
        else:
            context['qa_or'] = ''
            context['qa_and'] = 'checked'

        context['is_start'] = 'checked' if is_start_query == 'on' else ''

        return context

quiz_list_view = QuizListView.as_view()