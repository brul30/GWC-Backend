# from rest_framework import serializers
# from products.models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'notes_pdf', 'course_title', 'instructor', 'semester', 'user_id', 'user','year']
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile
