
from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    politicalLeader = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    sovereignty_date = models.DateField(verbose_name='Sovereignty Year')
    unPartcipation = models.BooleanField()
    essay = models.TextField(default='essay text')
    image = models.ImageField(upload_to='images/', default='country image', null=True, blank=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CountryLanguage(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    percentage = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.country.name + "-" + self.language.name

class Religion(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CountryReligion(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    percentage = models.FloatField()

    def __str__(self):
        return self.country.name + '-' + self.religion.name

class Article(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Question(models.Model):
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text

class QuestionAnswer(models.Model):
    text = models.TextField(null=True, blank=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.country.name + '-' + self.text

