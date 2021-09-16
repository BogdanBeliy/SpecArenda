from enum import auto
from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()






class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default='Беларусь')
    unp = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    registration_on_dashborad = models.DateTimeField(auto_now_add=True)   
    regions = models.ManyToManyField('Region', related_name='ads_by_region')

    email = models.EmailField(blank=True, null=True, unique=True)
    web = models.URLField(blank=True, null=True)
    banks = models.CharField(max_length=255)
    adres = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("organisation_detail", kwargs={"slug": self.slug, "pk": self.pk})

class OrganisationContacts(models.Model):
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True, unique=True)
    organisation = models.ForeignKey(Organization, on_delete=models.CASCADE)
    adres = models.CharField(max_length=300)
    def __str__(self):
        return self.phone
    


   
class OrganizationPhones(models.Model):
    phone = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)



class PaprentCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("parent_category_detail", kwargs={"slug": self.slug})  



class ChildCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='')
    category = models.ForeignKey(PaprentCategory, on_delete=models.CASCADE, related_name='child_category', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ad_by_category", kwargs={"slug": self.slug})



class Region(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name
    


class Ad(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    description = models.TextField()
    category = models.ForeignKey(ChildCategory, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=True)
    organizsation = models.ForeignKey(Organization, on_delete=models.CASCADE,blank=True, null=True, related_name='org_ads')
    
    
    def get_absolute_url(self):
        return reverse("ad_detail", kwargs={"slug": self.slug, "pk": self.pk})





    
