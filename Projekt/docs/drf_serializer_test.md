from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


person = Person(name='Adam', miesiac_dodania=1)
person.save()

serializer = PersonSerializer(person)
serializer.data
{'id': 16, 'name': 'Adam', 'shirt_size': ('S', 'Small'), 'miesiac_dodania': 1, 'team': None}

content = JSONRenderer().render(serializer.data)
content
b'{"id":16,"name":"Adam","shirt_size":["S","Small"],"miesiac_dodania":1,"team":null}'

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = PersonSerializer(data=data)
deserializer.is_valid()
deserializer.errors
deserializer.fields
deserialiser.validated_data
deserializer.save()
deserializer.data