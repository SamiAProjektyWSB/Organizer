from rest_framework import serializers

from soocalendar.models import Calendar


class Serializer(serializers.ModelSerializer):
    visible_for = serializers.SerializerMethodField("get_visible_for")
    editable_by = serializers.SerializerMethodField("get_editable_by")

    def get_editable_by(self, obj):
        return "; ".join(obj.visible_for.all().values_list("mail", flat=True))

    def get_visible_for(self, obj):
        return "; ".join(obj.visible_for.all().values_list("mail", flat=True))
    
    class Meta:
        model = Calendar
        exclude = ("owner",)
    


