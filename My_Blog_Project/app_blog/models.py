from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name='Put a title')
    slug = models.SlugField(max_length=265,unique=True)
    blog_content = models.TextField( verbose_name='wWhat is in your mind')
    blog_image = models.ImageField( upload_to='blog_images', verbose_name='Images')
    publish_date = models.DateTimeField( auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='blog_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(Blog, related_name='user_comment', on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    blog = models.ForeignKey(Blog, related_name='liked_blog', on_delete=models.CASCADE)
    user = models.ForeignKey(Blog, related_name='liker_user', on_delete=models.CASCADE)
    