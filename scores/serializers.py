from rest_framework import serializers
from scores.models import Features

from decimal import Decimal

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

class ScoreSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField('calculated_score')

    def calculated_score(self, obj):
        model_safety = {
                'building_n':Decimal( 0.8562951116608104),
                'car_n': Decimal(-1.1197522009115382),
                'fence_n':Decimal( 0.8645738997338348),
                'pavement_n': Decimal(-2.7640446169163604),
                'pole_n': Decimal(-1.3668127746954193),
                'signSymbol_n':Decimal( 1.4307958944168966),
                'sky_n': Decimal(-1.2085413182560176),
                'tree_n':Decimal( 1.2211282113560542),
                'car_s':Decimal( 1.276706722265352),
                'pole_s': Decimal(-2.5495362208622514),
                'road_s':Decimal( 2.3045829372063418),
                'tree_s':Decimal( 1.6128002756122644),
                'edges':Decimal( 9.006852233764103),
                'mean_h': Decimal(-0.0037399702129397674),
                'mean_l':Decimal( 0.005800178254241208),
                'mean_s': Decimal(-0.012353771092260758),
                'stdev_h':Decimal( 0.017482527921174836),
                'stdev_l':Decimal( 0.010386176872871787),
                'stdev_s':Decimal( 0.022151141036568137),
                'delta2':Decimal( 0.9083723073382153),
                'tau1': Decimal(-0.5198865484591118)
            }
        score = 0
        for variable_name in model_safety.keys():
            try:
                score += obj.__getattribute__(variable_name)*model_safety.get(variable_name)
            except:
                pass
        return score

    class Meta:
        model = Features
        fields = ['file_name','score','percentile']
    