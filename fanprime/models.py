from django.db import models


class Competence(models.Model):
    title = models.CharField(max_length=100)


class Offer(models.Model):
    EXPERIENCE_CHOICES = [
        ("junior", "Junior"),
        ("mid_level", "Mid Level"),
        ("senior", "Senior"),
    ]
    TYPE_CHOICES = [
        ("part_time", "Part Time"),
        ("full_time", "Full Time"),
    ]
    title = models.CharField(max_length=100)
    competences = models.ManyToManyField(Competence, related_name="competences")
    description = models.TextField()
    experience = models.CharField(choices=EXPERIENCE_CHOICES, max_length=20)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
