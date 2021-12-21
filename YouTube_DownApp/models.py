# from django.db import models
# from django.db.models.base import Model
# from django.core.validators import FileExtensionValidator

# # Create your models here.

# class Upload_video(models.Model):
#     vid_title = models.CharField(max_length=260)
#     vid_des = models.TextField()
#     vid_thumbnail = models.ImageField()
#     video = models.FileField(upload_to='videos_uploaded',null=True, validators=[
#         FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])
#         ])

#     def __str__(self):
#         return str(self.vid_title)if self.vid_Title else " "
