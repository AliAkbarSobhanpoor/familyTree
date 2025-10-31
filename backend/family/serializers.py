# serializers.py
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()
    rels = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()  # Override to use Q-prefixed ID

    class Meta:
        model = Person
        fields = ['id', 'data', 'rels']

    def get_id(self, obj):
        """
        Return the person's ID prefixed with 'Q', for example: Q12
        """
        return f"Q{obj.id}"

    def get_data(self, obj):
        """
        Build the 'data' dict with key person attributes.
        """
        return {
            "fn": obj.first_name or "",
            "ln": obj.last_name or "",
            "desc": obj.description or "",
            "label": obj.get_full_name(),
            "avatar": obj.avatar.url if obj.avatar else None,
            "gender": obj.gender,
        }

    def get_rels(self, obj):
        """
        Build relationships using Q-prefixed IDs.
        """
        return {
            "spouses": [f"Q{p.id}" for p in obj.spouses.all()],
            "parents": [f"Q{p.id}" for p in obj.parents.all()],
            "children": [f"Q{p.id}" for p in obj.children_of.all()],
        }
