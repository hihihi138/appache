# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from youku.models import Video, Log, User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from datetime import datetime
from django.views.generic.list_detail import object_list
from django.template import RequestContext
from django.contrib.comments.models import Comment
from tagging.views import tagged_object_list

def video_list_page(request):
    videos = Video.objects.all()
    comments = Comment.objects.order_by("-submit_date")[0:5]
    categories = Video.CATEGORY_CHOICES
    return object_list(request, template_name = 'index.html', queryset = videos, paginate_by=5, extra_context={'comments': comments, 'categories': categories})

def video_page(request, year, month, day, time):
    dt = datetime.strptime(year+month+day+time, "%Y%m%d%H%M%S")
    video = Video.objects.get(post_date=dt)
    return render_to_response('video_page.html', {'video': video}, context_instance=RequestContext(request))

def category_page(request, category):
    videos = Video.objects.filter(category=category)
    comments = Comment.objects.order_by("-submit_date")[0:5]
    categories = Video.CATEGORY_CHOICES
    return object_list(request, template_name = 'index.html', queryset = videos, paginate_by=5, extra_context={'comments': comments, 'categories': categories})

def tag_page(request, tag):
    queryset = Video.objects.all()
    return tagged_object_list(request, queryset, tag, paginate_by=5, template_name='index.html')

def log_page(request):
    logs = Log.objects.all()
    return object_list(request, template_name='upgrade_log.html', queryset=logs, paginate_by=10)