from rest_framework import serializers

from goods.models import SPUSpecification, SPU


class SPUSpecificationSerializer(serializers.ModelSerializer):
    # 指定关联外键返回形式
    # 返回关联表的str指定名称
    spu = serializers.StringRelatedField(read_only=True)
    # 返回id
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification  # 商品规格表关联了spu表的外键spu
        fields = '__all__'



class SPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPU
        fields = ('id', 'name')