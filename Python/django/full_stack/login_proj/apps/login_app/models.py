from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")



class User(models.Model):
    objects = UserManager()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    hashed_pw = models.CharField(max_length=255)
    def __repr__(self):
        return f"<User Object: {self.first_name} {self.last_name}, email: {self.email} hashed password: {self.hashed_pw}"
