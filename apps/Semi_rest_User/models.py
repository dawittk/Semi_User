from django.db import models
# from __future__ import unicode_literals
import bcrypt   
from django.db import models

class UserManager(models.Manager):
    def validate(self, form_data):
      errors =[]

      if len(form_data['first_name'])<3:
          errors.append("First name must be at least 3 Characters.")
      if len(form_data['last_name'])<3:
          errors.append("Last name must be at least 3 Characters.")
      if len(form_data['email'])<8:
          errors.append("Email must be at least 8 Characters.")

      existing_users = self.filter(email=form_data['email'])
      if existing_users:
            errors.append("email already in use")
   
      return errors
    

    def create_user(self, form_data):
      
        return self.create(
            first_name =form_data['first_name'],
            last_name  =form_data['last_name'],
            email      =form_data['email'],           
            
            
        )
class user(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)      
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
