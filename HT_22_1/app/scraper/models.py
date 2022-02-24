from django.db import models


class Ask(models.Model):
    story_id = models.IntegerField(default=None, null=True)
    story_type = models.CharField(max_length=200)
    by = models.CharField(max_length=200)
    timestamp = models.IntegerField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    story_id = models.IntegerField(default=None, null=True)
    story_type = models.CharField(max_length=200)
    by = models.CharField(max_length=200)
    timestamp = models.IntegerField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)

    def __str__(self):
        return self.title


class Show(models.Model):
    story_id = models.IntegerField(default=None, null=True)
    story_type = models.CharField(max_length=200)
    by = models.CharField(max_length=200)
    timestamp = models.IntegerField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)

    def __str__(self):
        return self.title


class New(models.Model):
    story_id = models.IntegerField(default=None, null=True)
    story_type = models.CharField(max_length=200)
    by = models.CharField(max_length=200)
    timestamp = models.IntegerField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)

    def __str__(self):
        return self.title
