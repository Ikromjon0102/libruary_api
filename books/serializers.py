from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','title','sub_name','content','author','isbn','price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title is alpha
        if not title.isalpha():
            raise ValidationError(
                {
                    'status' : False,
                    'message' : "Kitob sarlavhasi matn bo'lishi kerak"
                }

            )
        if Book.objects.all().filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Muallifning bu kitobi bazada mavjud"
                }
            )
        return data

    def validate_price(self, price):
        if price>0 or price < 9999999:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Narx noto'g'ri kiritilgan"
                }
            )

