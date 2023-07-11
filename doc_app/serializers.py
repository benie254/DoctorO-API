from rest_framework import serializers 
from doc_app.models import Contact 

# create serializers here 
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')
