# -*-coding:utf-8 -*-
from django.db import models
from datetime import datetime
from tagging.fields import TagField

class User(models.Model):
    name = models.CharField(max_length=30)
    reg_date = models.DateTimeField(default=datetime.now())
    email = models.EmailField()
    intro = models.TextField(max_length=4096)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='题目')
    url = models.URLField(verbose_name='优酷网址')
    flash_url = models.URLField(verbose_name='Flash地址')
    posted_by = models.ForeignKey(User, verbose_name='发布人')
    post_date = models.DateTimeField(default=datetime.now(), verbose_name='发布时间')
 #   tag = models.CharField(max_length=100, verbose_name='标签')
    CATEGORY_CHOICES = (
	('animal', '动物世界'),
	('funny', '轻松搞笑'),
	('animation', '动画短片'),
	('amazing', '不可思议'),
	('emotional', '真情感人'),
	('other', '其它'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name='分类')
    tags = TagField()

    def get_vid(self):
        from datetime import datetime
        dt_string = datetime.strftime(self.post_date, "%Y%m%d%H%M%S")
        return dt_string[0:4] + "/" + dt_string[4:6] + "/" + dt_string[6:8] + "/" + dt_string[8:14]
    vid = property(get_vid)

    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-post_date']

class Log(models.Model):
    log_title = models.CharField(max_length=100)
    log_content = models.TextField(max_length=4096)
    log_time = models.DateTimeField(default=datetime.now())
    
    def __unicode__(self):
		return self.log_title
    class Meta:
		ordering = ['-log_time']

class PostedVideo(models.Model):
	title = models.CharField(max_length=100, verbose_name='题目')
	url = models.URLField(verbose_name='优酷网址')
	post_date = models.DateTimeField(default=datetime.now(), verbose_name='发布时间')
	tags = models.CharField(max_length=100, verbose_name='标签')
	reason = models.TextField(verbose_name='推荐语')
	
	def __unicode__(self):
		return self.title