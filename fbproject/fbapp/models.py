from django.db import models

# Create your models here.
class Fb_model(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Add_post(models.Model):
    post_title=models.CharField(max_length=30)
    post_urls=models.CharField(max_length=50)
    post_comment=models.TextField()
    post_image=models.ImageField(null=True,blank=True, upload_to="images/")
    add_comment=models.CharField(max_length=255)

    def __str__(self):
        return '%s' %(self.post_title)

class SignUp(models.Model):
    email = models.EmailField() 
    username=models.CharField(max_length=30)
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)


class Comment(models.Model):
    addpost=models.ForeignKey(Add_post, related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' %(self.name)
    
class comment_reply(models.Model):
    # addpost=models.ForeignKey(Add_post, related_name="comment_reply",on_delete=models.CASCADE)
    text = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    date_added = models.DateTimeField(auto_now_add=True)