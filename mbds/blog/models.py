

# Create your models here.
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class CustomManger(models.Manager):#custmize the model .Display to end user and db only published posts
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

from taggit.managers import TaggableManager
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))#gives drop down list
    title=models.CharField(max_length=264)
    slug=models.SlugField(max_length=264,unique_for_date='publish')#seo frindly urls, per date unique slug
    author=models.ForeignKey(User,related_name='blog_posts')#who are valid person in user table that person is author
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)#here we get publishing date
    created=models.DateTimeField(auto_now_add=True)#datetime of create() action .at what time post is created
    updated=models.DateTimeField(auto_now=True)#datetme of save() action
    documenturl=models.URLField(max_length=250)
    #i got post object i.e post.title='mohan'
                                           # post.save()
                                            # auto_now=True means when object is saved that time will be consided

    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')#end user which droped list selected .if not select any dropdown list defsult one is draft
    objects=CustomManger()
    tags=TaggableManager()# create the tags assoicated for posts using TaggableManager it is third party application


    class Meta:
        ordering=('-publish',)#posts in decending order
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
#model related to comments
class comments(models.Model):
    post=models.ForeignKey(Post,related_name='comments')#this comment related which post and to acces all comments related this post we use related_name='comments'  use post.comments to get all comments
    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)#at what time comment is added
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)#for deactive comments like vulgar comments

    class Meta:# dispplay comments order wise latest comment display as first
        ordering=('-created',)#ordering single value tuple
    def __str__(self):#display the who commented on post eg: commented By mohan on Indian armay
        return 'Commented By {}  on  {}'.format(self.name, self.post)

from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    Sendamessage=models.TextField()
