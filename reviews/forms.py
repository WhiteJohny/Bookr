from django import forms

TITLE_OR_CONTRIBUTOR = (
    ("title", "Title"),
    ("contributor", "Contributor")
)


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=TITLE_OR_CONTRIBUTOR)
