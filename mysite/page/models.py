from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Pages(models.Model):
	menu_title = models.CharField(max_length=200)
	page_title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, help_text="Slug will be generated automatically from the title of the post")
	content = RichTextUploadingField()
	pub_date = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	
	class Meta:
		db_table = 'Pages'
		verbose_name = "Page"
		verbose_name_plural = "Pages"

	def __str__(self):
		return self.menu_title