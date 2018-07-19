from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from page.models import Pages

class PageCreateForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())

	class Meta:
		model = Pages
		fields = ('menu_title', 'page_title', 'slug', 'content', 'is_active')