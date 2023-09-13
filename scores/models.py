from django.db import models

# Create your models here.
class Features(models.Model):
    # id = models.AutoField(read_only=True)
    file_name = models.CharField(max_length=200, primary_key=True)
    void = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    blobs = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    edges = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    mean_bn = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    mean_bs = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    mean_h = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    mean_l = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    mean_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    stdev_bn = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    stdev_bs = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    stdev_h = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    stdev_l = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    stdev_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    bicyclist_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    bicyclist_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    building_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    building_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    car_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    car_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    fence_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    fence_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    pavement_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    pavement_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    pedestrian_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    pedestrian_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    pole_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    pole_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    road_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    road_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    signSymbol_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    signSymbol_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    sky_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    sky_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    tree_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    tree_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    unlabelled_n = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    unlabelled_s = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_bench = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_bicycle = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_boat = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_bus = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_car = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_chair = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_fire_hydrant = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_motorcycle = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_person = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_potted_plant = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_stop_sign = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_traffic_light = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_train = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_truck = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)
    od_umbrella = models.DecimalField(default=0.0,max_digits=11, decimal_places=8)

    def __str__(self):
            return self.file_name


# class Answers(models.Model):
#     img_1 = 
    # img_2 = 
    # question = 
    # answer = 


# class PerceptionModel(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     id = models.CharField(max_length=200)

#     class Meta:
#         ordering = ['created']

# class PerceptionFormula(models.Model, Features):
#     """
#     Copy all fields from Features
#     """
#     pass


# class Users(models.Model, Features):
#     """
#     Copy all fields from Features
#     """
#     pass
