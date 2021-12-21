from django.db import models
#from embed_video.fields import EmbedVideoField
# from django.utils.translation import ugettext_lazy as _


# Create your models here.
# class Video_model(models.Model):
#     vid_Title = models.CharField(max_length=200)
#     vidl_Body = models.CharField(max_length=600)

#     class Meta:
#         verbose_name_plural = "Video"
#     def __str__(self):
#         return str(self.vid_Title)if self.vid_Title else " "



#should be migration after prefix the modle name

class Permission_manual(models.Model):
    manual_id = models.CharField(primary_key=True, max_length=8)
    language = models.CharField(max_length=20, primary_key=True, null=True)
    superior_null_id = models.CharField(null=True)
    manual_name = models.CharField(null=True)
    url= models.CharField(max_length=100, null=True)
    whether_the_root_node = models.IntegerField(max_length=1, null=True)
    whether_the_leaf_node = models.IntegerField(max_length=1, null=True)
    wether_to_display = models.IntegerField(max_length=1, null=True)
    sort_code = models.CharField(max_length=8, null=True)

    def __str__(self):
        return self.manual_name


class Permission_role(models.Model):
    role_id = models.CharField(primary_key=True, max_length=20)
    role_name = models.CharField(null=True, max_length=32)
    role_instruction = models.CharField(max_length=256, null=True)
    role_property = models.CharField(max_length=2, null=True)
    role_level = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.role_name


class Permission_role_operate(models.Model):
    role_id = models.ForeignKey('model_name',primary_key=True, max_length=20)
    operate_type_id = models.CharField(primary_key=True, max_length=4 ,null=True)


class permission_role_manual(models.Model):
    role_id = models.ForeignKey('model_name',primary_key=True, max_length=20, null=True)
    manual_id = models.ForeignKey('model_name', null=True)
    language = models.CharField('model_name', max_length=20, primary_key=True, null=True)



class permission_role_subscription_information(models.Model):
    role_id = models.ForeignKey('model_name',primary_key=True, max_length=20, null=True)
    information_encode = models.CharField(max_length=20, null=True)


class permission_role_subscription_information(models.Model):
    role_id = models.ForeignKey('model_name', max_length=20, null=True)
    homepage_id = models.ForeignKey(max_length=32, null=True)







