from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Article category options
CATEGORY_CHOICES = [
    ('World', 'World News'),
    ('Politics', 'Politics'),
    ('Economics', 'Economics'),
    ('Entertainment', 'Entertainment'),
	('Science', 'Science & Technology'),
	('Sports', 'Sports'),
	('Health', 'Health & Medicine')
]


# Create your forms here.
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class SubmitHeadlineForm(forms.Form):
	headline = forms.CharField(label="Enter a headline", max_length=150)
	category = forms.CharField(label='Select a category', widget=forms.Select(choices=CATEGORY_CHOICES))

	def save(self, commit=True):
		article = super(NewUserForm, self).save(commit=False)
		if commit:
			article.save()
		return article
