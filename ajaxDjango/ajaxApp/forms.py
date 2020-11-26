from .models import Friend
from django import forms
import datetime

from .models import Crawl

class FriendForm(forms.ModelForm):
	dob = forms.DateField(
			label = 'What is your birth date?',
			widget = forms.SelectDateWidget(years = range(1980, datetime.date.today().year - 5))
		)

	def __init__(self, *args, **kwargs):
		super(FriendForm, self).__init__(*args, **kwargs)

		for name in self.fields.keys():
			self.fields[name].widget.attrs.update({
				'class': 'form-controls',
				})

	class Meta:
		model = Friend
		fields = ("__all__")

class CrawlForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CrawlForm, self).__init__(*args, **kwargs)

		for name in self.fields.keys():
			self.fields[name].widget.attrs.update({
				'class': 'form-controls',
				})
	class Meta:
		model = Crawl
		fields = ("__all__")