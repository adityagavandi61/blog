from django.db import models
import uuid
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_id = models.CharField(primary_key=True, default=uuid.uuid4,editable=False,max_length=50)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    content = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Advertisment(models.Model):
    post = models.ForeignKey(Post,related_name='post',on_delete=models.CASCADE)
    is_advertisement = models.BooleanField(default=False)
    is_headadvertisment = models.BooleanField(default=False)

    def __str__(self):
        return self.post.title

class Like(models.Model):
    like_id = models.CharField(primary_key=True, default=uuid.uuid4,editable=False,max_length=50)
    like_by = models.ForeignKey(User,on_delete=models.CASCADE)
    like_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    like_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.like_post.title

class Comment(MPTTModel):
    comment_id = models.CharField(primary_key=True, default=uuid.uuid4,editable=False,max_length=50)
    comment_post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',db_index=True, on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    comment_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['date']

    def __str__(self):
        return self.comment_post.title

    
