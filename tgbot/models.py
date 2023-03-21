from django.db import models
from django.core.cache import cache

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)
    

# Create your models here.
class Tgusers(models.Model):
    tguser_id=models.AutoField(primary_key=True, editable=False)
    users_name=models.CharField(max_length=100)
    stupid_btn_counter=models.IntegerField(default=0)
    fat_btn_counter=models.IntegerField(default=0)
    dumb_btn_counter=models.IntegerField(default=0)
    def __str__(self):
        return self.users_name


class Button(SingletonModel):
    stupid_btn_counter=models.IntegerField(default=0)
    dumb_btn_counter=models.IntegerField(default=0)
    fat_btn_counter=models.IntegerField(default=0)

    


