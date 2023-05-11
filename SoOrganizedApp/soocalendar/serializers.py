from rest_framework import serializers

from soocalendar.models import Calendar, Event


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



class eventSerializer(serializers.ModelSerializer):

    title = serializers.SerializerMethodField("get_title")
    start = serializers.SerializerMethodField("get_start")
    end = serializers.SerializerMethodField("get_end")

    def get_title(self, obj):
        return obj.name
    
    def get_start(self, obj):
        return obj.beggining_time
    
    def get_end(self, obj):
        return obj.end_time

    class Meta:
        model = Event 
        fields = ("title", "start", "end" )
    


