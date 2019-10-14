from django import forms
from rango.models import Page, Category


# Se podrían quitar los campos views, likes y slug, ya que no se mandan (?)
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please Enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


# Se podría quitar el campo views y excluirlo del envío, ya que el modelo se inicializa a 0 por defecto (?)
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data

    class Meta:
        mode = Page
        exclude = ('category',)
        # fields = ('title', 'url', 'views') equivalente
