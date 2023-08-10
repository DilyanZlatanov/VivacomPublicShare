from django.contrib import admin
from Vivacom.customer_feedback.models import CustomerFeedbackModel


class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'email_for_contact', 'publication_date']
    list_filter = ['is_reviewed']
    actions = ['mark_as_reviewed']

    def mark_as_reviewed(self, request, queryset):
        queryset.update(is_reviewed=True)

    mark_as_reviewed.short_description = "Mark selected feedback as reviewed"


admin.site.register(CustomerFeedbackModel, CustomerFeedbackAdmin)
