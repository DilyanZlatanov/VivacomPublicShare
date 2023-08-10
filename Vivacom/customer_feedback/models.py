from django.db import models


class CustomerFeedbackModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(
        max_length=500,
        blank=False,
        null=False,
    )
    email_for_contact = models.EmailField(
        blank=False,
        null=False,
    )
    publication_date = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)
