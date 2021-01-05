from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class EBooks(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=True)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()

    class Meta:
        verbose_name = (
            "EBook"  # changes the name of the model which appear the admin homepage
        )
        verbose_name_plural = "EBooks"

    def __str__(self):
        return self.name


class Reviews(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    say = models.TextField(blank=True)
    ebook = models.ForeignKey(EBooks, on_delete=models.CASCADE, related_name="reviews")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return str(self.rating)
