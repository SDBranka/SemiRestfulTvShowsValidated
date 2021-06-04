from django.db import models
import datetime

# Create your models here.
class ShowManager(models.Manager):
    def add_validator(self, post_data):
        errors = {}

        if len(post_data["title"]) < 1:
            errors["title"] = "Please enter a title"
        show_in_db = self.filter(title = post_data["title"])        #ensure no duplicate title exists
        if show_in_db:
            errors["title"] = "This show already exists in the database"
        if len(post_data["network"]) < 1:
            errors["network"] = "Please enter a network"
        if len(post_data["release_date"]) < 1:
            errors["release_date"] = "Please enter a date"
        if post_data["release_date"] > str(datetime.date.today()):
            errors["release_date"] = "Please enter a date prior to today's date"
        if len(post_data["desc"]) > 0 and len(post_data["desc"]) < 10:
            errors["desc"] = "Please enter a valid description"
        return errors

    def edit_validator(self, post_data):
        errors = {}

        if len(post_data["title"]) < 1:
            errors["title"] = "Please enter a title"
        if len(post_data["network"]) < 1:
            errors["network"] = "Please enter a network"
        if len(post_data["release_date"]) < 1:
            errors["release_date"] = "Please enter a date"
        if post_data["release_date"] > str(datetime.date.today()):
            errors["release_date"] = "Please enter a date prior to today's date"
        if len(post_data["desc"]) > 0 and len(post_data["desc"]) < 10:
            errors["desc"] = "Please enter a valid description"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()
