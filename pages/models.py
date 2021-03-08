from django.db import models



class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

# Create model --> makemigrate --> migrate --> register in admin.py

# this creates the form and fields in Django
# model name should be singular (Team not Teams)
# Create your models here. (model is like creating table in coding, add fields to it)
# to use a table we need to create a model
# model is like a programatice table
#install the package pillow whn using image or media fields
#pip install pillow


# then makemigrattion - it getting ready ro migradt the fields (python manage.py makemigrations) 
# this converts and creates a structured temp file - that will be moved to the backend 
# for each model modification we need to migrate  
# then migrate ()
# this will create a structure
# now register the model in admin.py

# If you just want to rename the model name in the admin panel, you can use the verbose_name_plural on it. Something like this:

# class Teams(models.Model):
#     class Meta:
#         verbose_name = "teams"
#         verbose_name_plural = "team"
# Don't delete the complete database, it's not a good practice, 
# you will lose your data when you have a lot of data in your database especially on the production database. 
# You can delete the table if you want and create a new one, or you just delete the migration file and run the migration again. That will fix such issues.