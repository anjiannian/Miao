# -*- encoding:utf-8 -*-
from django.db import models

SEX_CHOICE = (
    ("M", "male"),
    ("F", "female")
)

USER_LEVEL = (
    (0, "admin"),
    (1, "ordinary user")
)


class BaseModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # 0-false, 1-true, ...
    status = models.CharField(max_length=1)


class Volunteers(BaseModel):
    #id = models.AutoField(primary_key=True)
    account = models.CharField(u"用户名", max_length=50, unique=True)
    password = models.CharField(u"用户名", max_length=50)
    name = models.CharField(u"真实名称", max_length=50, null=True)
    nick_name = models.CharField(u"昵称", max_length=50, null=True)
    en_name = models.CharField(u"英文名称", max_length=50, null=True)
    sex = models.CharField(u"性别", max_length=1, choices=SEX_CHOICE)
    age = models.IntegerField(u"年龄", null=True)
    phone_number = models.CharField(u"联系方式", max_length=50)

    level = models.CharField(u"性别", max_length=1, choices=USER_LEVEL)


class Classes(BaseModel):
    #id = models.AutoField(primary_key=True)
    class_name = models.CharField(u"班级", max_length=50, null=True)
    grade = models.CharField(u"年级", max_length=50, null=True)
    contact = models.CharField(u"联系人", max_length=50, null=True)
    school_name = models.CharField(u"学校名称", max_length=50, null=True)


class Courses(BaseModel):
    #id = models.AutoField(primary_key=True)
    course_name = models.CharField(u"课程名称", max_length=50, null=True)


class ClassBegin(BaseModel):
    #id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Courses)
    course_name = models.CharField(u"课程名称", max_length=50, null=True)
