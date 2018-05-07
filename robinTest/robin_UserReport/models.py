from django.db import models

class ApplicationUser(models.Model):
    email_address = models.EmailField(max_length=30, primary_key=True, help_text="Email address used to register in application. Typically used to sent alerts, account updates and other news.")
    user_name = models.CharField(max_length=15, help_text="User name for login to the application. Replaces need of using long email address.")
    def get_absolute_url(self):
         return reverse('appUser', args=[str(self.id)])
    def __str__(self):
        return self.field_name

class SupportedBank(models.Model):
    bank_name = models.CharField(max_length=15, help_text="The name of an associated bank.")
    # todo: leave as text for now, but should be FileField:
    logo_id = models.CharField(max_length=2000, help_text="Path to the icon to display that corresponds to the respective bank.")
    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return "Supported Bank"

class SideBarItem(models.Model):
    # Does not refencen to other pages
    # This is a standalone object that
    # will be displayed in the user's main page
    id = models.CharField(max_length=15, primary_key=True, help_text="")
    idText = models.CharField(max_length=15, primary_key=False, help_text="")
    text = models.CharField(max_length=15, primary_key=False, help_text="")
    userData = models.CharField(max_length=200,  primary_key=False, help_text="Temporarily stores user data to show it on GUI.")
    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return "sideBarItem"

class HorizontalBarItem(models.Model):
    href = models.CharField(max_length=15, primary_key=True, help_text="")
    name = models.CharField(max_length=15, primary_key=False, help_text="")