from django import forms

from .models import SearchData
search_data = SearchData.objects.all()
class SearchHistoryForm(forms.Form):
    # search_keywords = [
    #     (search, f'{search} ({len(search_data.filter(search_query=search))} times found)') for search in SearchData.objects.values_list('search_query', flat=True).distinct()
    # ]

    keywords = forms.ModelMultipleChoiceField(
        queryset=SearchData.objects.values_list('search_query', flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple,
    )
    time_range = forms.ChoiceField(
        choices=[
            ('', 'Select time range'),
            ('today', 'See data from today'),
            ('yesterday', 'See data from yesterday'),
            ('week', 'See data from last week'),
            ('month', 'see data from last month'),
        ],
        
    )