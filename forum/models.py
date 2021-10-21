from django.db import models


class Topic(models.Model):
    topic_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')


class Comment(models.Model):
    comment = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')