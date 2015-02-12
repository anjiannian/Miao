# -*- encoding:utf-8 -*-
from django.db import models
from django.template.defaultfilters import title
from datetime import date
from django.test.client import CONTENT_TYPE_RE

# Create your models here.

# class files(models.Model):
#     title = models.CharField(u"标题", max_length=50, null=True, blank=True)
#     datetime = models.TimeField(u'发布时间', null=True, blank=True)
#     author = models.CharField(u"作者", max_length=20, null=True, blank=True)
#     content = models.FilePathField(u"内容")
#     summary = models.TextField(u"摘要", max_length=320)
#     
#     def __unicode__(self):
#         return self.name