from django.db import models
from froala_editor.fields import FroalaField
from .createSlug import generate_slug
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class Post(models.Model):
	title = models.CharField(max_length= 350)
	thumbnail = models.ImageField(upload_to= "blog_images/")
	author = models.CharField(max_length= 50, default= "Codewitgabi")
	date_created = models.DateField(auto_now_add= True)
	content = FroalaField()
	slug = models.SlugField(max_length= 350, null= True, blank= True)
	is_published = models.BooleanField(default= False)
	
	def save(self, *args, **kwargs):
		for post in Post.objects.all():
			if self.slug == post.slug:
				break
		else:
			self.slug = generate_slug(self.title)
			email_message = render_to_string("post/email.html", {"slug": self.slug})
			email = EmailMessage(
				"New Post Update",
				email_message,
				"codewitgabi222@gmail.com",
				[subscriber for subscriber in Subscriber.objects.all()]
			)
			email.fail_silently = False
			email.send()
		super().save(*args, **kwargs)
	
	def __str__(self):
		return self.title		
		
		
class Subscriber(models.Model):
	email = models.EmailField()
	first_name = models.CharField(max_length= 500)
	
	def __str__(self):
		return self.email
		
		
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete= models.CASCADE)
	commenter = models.CharField(max_length= 100)
	content = models.TextField()
	
	def __str__(self):
		return self.content[:50]
		
		