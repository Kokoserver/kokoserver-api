from rest_framework import serializers

from .models import Article as ArticleModel

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = "__all__" #  or fields = ["id", "title", "author", "email"]
        extra_kwargs = {"author": {"read_only":True}}
        
    
    #    title = serializers.CharField(max_length=100)
    #    author = serializers.CharField(max_length=100)
    #    email = serializers.EmailField()
    #    data  = serializers.DateField()
       
    #    def create(self, validated_data):
    #        return ArticleModel.objects.create(validated_data)
    #     #    new_article.save()
        
    #    def update(self,  instance, validated_data):
    #        instance.title = validated_data.get("title", instance.title)
    #        instance.author = validated_data.get("author", instance.author)
    #        instance.email = validated_data.get("email", instance.email)
    #        instance.data = validated_data.get("date", instance.date)
    #        instance.save()
    #        return instance
       
          