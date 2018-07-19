from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from page.models import Pages

class PageForumForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-6'
	helper.field_class = 'col-sm-6'
	helper.layout = Layout(
        Field('menu_title', css_class='input-sm'),
        Field('page_title', css_class='input-sm'),
        Field('slug', css_class='input-sm'),
        Field('content', css_class='input-sm'),
        Field('is_active', css_class='input-sm'),
        FormActions(Submit('page_forum', 'page_forum', css_class='btn-primary'))
    )
	class Meta:
		model = Pages
		fields = ('menu_title', 'page_title', 'slug', 'content', 'is_active')