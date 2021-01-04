# [Rest_Framework Serializers](https://www.django-rest-framework.org/api-guide/serializers/#saving-instances)



## [Saving Instances](https://www.django-rest-framework.org/api-guide/serializers/#saving-instances)

The `create()` and the `update()` method are available in the inherited class of `serializers.Serializer`.

When an instance of the class **inherited** from `serializers.Serializer` is created, the `save()` method is available on the instance. 


## [Validation](https://www.django-rest-framework.org/api-guide/serializers/#validation)

If the `serializer.is_valid()` is *invalid*, then `serializer.errors` will contain the **dictionary** of the errors

```py
serializer = CommentSerializer(data={'email': 'foobar', 'content': 'baz'})
if not serializer.is_valid():
	serializer.errors
# {'email': ['Enter a valid e-mail address.'], 'created': ['This field is required.']}
```

#### [Field Level Validation](https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation)

Custom field validation by adding `.validate_<field_name>` methods to the **Serializer** subclass.

#### [Object Level Validation](https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation)

Add the `validate()` method to the **Serializer** subclass.

```py
from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start") # raise a serializers.Validation error here
        return data
```

## [Model Serializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)

```py
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password','updated_at']
        read_only_fields = ['updated_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
```
