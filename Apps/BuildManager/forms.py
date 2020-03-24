from django import forms
from .models import BuildData


class BuildDataForm(forms.Form):
    commitId = forms.CharField()
    devName = forms.CharField()

# NOTE: This is an example of form validation on the site itself


class BuildDattaModelForm(forms.ModelForm):
    class Meta:
        model = BuildData
        fields = ['commitID', 'devName']

    def clean_commitID(self, *args, **kwargs):
        commit = self.cleaned_data.get('commitID')
        qs = BuildData.objects.filter(commitID__iexact=commit)
        if qs.exists():
            raise forms.ValidationError(
                "This is your error if duplicate commitID's exist")
        return commit
