from django.contrib import admin
from profiles_api import models

# Register the UserProfile model with the admin site
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
