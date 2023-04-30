from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

# Create your models here.
def dining_img_path(instance, filename):
    return f'images/dining/{instance.title}/{filename}'


def review_img_path(instance, filename):
    return f'images/review/{instance.dining}/{instance.user.username}/{filename}'


class MenuTaggedItem(TaggedItemBase):
    content_object = models.ForeignKey('Dining', on_delete=models.CASCADE, related_name='menu_tagged_items')


class PriceTaggedItem(TaggedItemBase):
    content_object = models.ForeignKey('Dining', on_delete=models.CASCADE, related_name='price_tagged_items')


class PurposeTaggedItem(TaggedItemBase):
    content_object = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='purpose_tagged_items')


class AtmosphereTaggedItem(TaggedItemBase):
    content_object = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='atmosphere_tagged_items')


class FacilityaggedItem(TaggedItemBase):
    content_object = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='facility_tagged_items')


class Dining(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)

    # 이미지는 5개까지 업로드 가능하게
    image1 = models.ImageField(blank=True, upload_to=dining_img_path)
    image2 = models.ImageField(blank=True, upload_to=dining_img_path)
    image3 = models.ImageField(blank=True, upload_to=dining_img_path)
    image4 = models.ImageField(blank=True, upload_to=dining_img_path)
    image5 = models.ImageField(blank=True, upload_to=dining_img_path)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_dinings")
    address_mc_do = models.CharField(max_length=20)
    address_city = models.CharField(max_length=20)
    address_dong = models.CharField(max_length=20)
    address_detail = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True)
    
    tags = TaggableManager(blank=True)
    menu_tags = TaggableManager(blank=True, through=MenuTaggedItem, related_name='menu_tags')
    price_tags = TaggableManager(blank=True, through=PriceTaggedItem, related_name='price_tags')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dining = models.ForeignKey(Dining, on_delete=models.CASCADE)

    content = models.TextField(null=True)

    # 이미지는 5개까지 업로드 가능하게
    image1 = models.ImageField(blank=True, upload_to=review_img_path)
    image2 = models.ImageField(blank=True, upload_to=review_img_path)
    image3 = models.ImageField(blank=True, upload_to=review_img_path)
    image4 = models.ImageField(blank=True, upload_to=review_img_path)
    image5 = models.ImageField(blank=True, upload_to=review_img_path)

    rating = models.FloatField()
    rating_taste = models.FloatField()
    rating_price = models.FloatField()
    rating_kind = models.FloatField()

    def star_rating(self):
        rounded_rating = round(self.rating * 2) / 2
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    def star_rating_taste(self):
        rounded_rating = round(self.rating_taste * 2) / 2
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    def star_rating_price(self):
        rounded_rating = round(self.rating_price * 2) / 2
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    def star_rating_kind(self):
        rounded_rating = round(self.rating_kind * 2) / 2
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    purpose_tags = TaggableManager(blank=True, through=PurposeTaggedItem, related_name='purpose_tags')
    atmosphere_tags = TaggableManager(blank=True, through=AtmosphereTaggedItem, related_name='atmosphere_tags')
    facility_tags = TaggableManager(blank=True, through=FacilityaggedItem, related_name='facility_tags')