from rest_framework import serializers
from scores.models import Features


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = [
            'file_name','void','blobs','edges','mean_bn','mean_bs','mean_h','mean_l','mean_s'
            ,'stdev_bn','stdev_bs','stdev_h','stdev_l','stdev_s'
            ,'bicyclist_n','bicyclist_s','building_n','building_s','car_n','car_s','fence_n','fence_s'
            ,'pavement_n','pavement_s','pedestrian_n','pedestrian_s','pole_n','pole_s','road_n','road_s'
            ,'signSymbol_n','signSymbol_s','sky_n','sky_s','tree_n','tree_s','unlabelled_n','unlabelled_s'
            ,'od_bench','od_bicycle','od_boat','od_bus','od_car','od_chair','od_fire_hydrant','od_motorcycle'
            ,'od_person','od_potted_plant','od_stop_sign','od_traffic_light','od_train','od_truck','od_umbrella'
        ]