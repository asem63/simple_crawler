from django.db import models


class Category(models.Model):
    """
    Category information
    """
    title = models.TextField(blank=True)
    mnemonic_name = models.TextField(blank=True)


class App(models.Model):
    """
    App information
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    app_id = models.CharField(max_length=300)
    title = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    dev_id = models.CharField(max_length=300)
    dev = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
