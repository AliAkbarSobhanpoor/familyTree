# serializers.py
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()
    rels = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ['id', 'data', 'rels']

    def get_data(self, obj):
        return {
            "fn": obj.first_name or "",
            "ln": obj.last_name or "",
            "desc": obj.description or "",
            "label": obj.get_full_name(),
            "avatar": obj.avatar.url if obj.avatar else None,
            "gender": obj.gender,
        }

    def get_rels(self, obj):
        return {
            "spouses": [{p.id} for p in obj.spouses.all()],
            "parents": [{p.id} for p in obj.parents.all()],
            "children": [{p.id} for p in obj.children_of.all()],
        }
