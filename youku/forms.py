# -*- coding: utf-8 -*-

from django import forms

class PostVideoForm(forms.Form):
	title = forms.CharField(max_length=100, label='视频名称')
	url = forms.URLField(label='优酷地址')
	tags = forms.CharField(max_length=100, label='标签')
	reason = forms.CharField(widget=forms.Textarea, label='视频看点')