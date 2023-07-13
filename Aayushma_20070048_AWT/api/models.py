from django.db import models

class Location(models.Model):
    Title = models.CharField(max_length=25, unique= True, default=('Enter the Task Title:'))
    Description = models.CharField(max_length=200, default=('Enter your Task Description:'))
    Status = models.CharField(max_length=5, default=('Yes/No'))
    def __str__(self):
     return self.Title
    

class Item(models.Model):
   Name = models.CharField(max_length=100)
   date_added = models.DateField(auto_now_add=True)
   Task = models.ForeignKey(Location, on_delete= models.CASCADE)

def __str__(self):
     return self.Name


class File(models.Model):
   def nameFile(instance, FolderName):
       return '/'.join(['files', str(instance.FolderName), FolderName])
   FolderName = models.CharField(max_length=100)
   #date_added = models.DateField(auto_now_add=True)
   Task = models.ForeignKey(Location, on_delete= models.CASCADE)
   files = models.FileField(upload_to=nameFile,blank=True)


def __str__(self):
     return self.FolderName
