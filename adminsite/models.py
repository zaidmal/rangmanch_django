from django.db import models


# Create your models here.


class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    User_firstname = models.CharField(null=False, max_length=50)
    User_lastname = models.CharField(null=False, max_length=50)
    user_phone = models.BigIntegerField()
    user_email = models.CharField(null=False, max_length=100)
    user_password=models.CharField(null=False,max_length=100)
    is_admin=models.IntegerField()

    class Meta:
        db_table = "users"

class categorys(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(null=False, max_length=50)

    class Meta:
        db_table = "categorys"

class subcategory(models.Model):
    subcat_id = models.AutoField(primary_key=True)
    subcat_name = models.CharField(null=False, max_length=50)
    category_id = models.ForeignKey(categorys, on_delete=models.PROTECT)

    class Meta:
        db_table = "subcategory"


class event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(null=False, max_length=100)
    event_image = models.CharField(null=False, max_length=250)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(null=False, max_length=500)
    subcat_id = models.ForeignKey(subcategory, on_delete=models.PROTECT)

    class Meta:
        db_table = "event"

class package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(null=False, max_length=50)
    package_desc =models.CharField(null=False,max_length=2500)
    package_price=models.IntegerField()
    event_id = models.ForeignKey(event, on_delete=models.PROTECT)


    class Meta:
        db_table = "package"


# class services(models.Model):
#     ser_id = models.AutoField(Primary_key=True)
#     ser_name = models.CharField(null=False, max_length=50)
#
#     class Meta:
#         db_table = "services"
class bookevent(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_date = models.DateTimeField(null=False, max_length=50)
    payment_status = models.IntegerField()
    req_date = models.DateTimeField()
    user_id = models.ForeignKey(users, on_delete=models.PROTECT)

    class Meta:
        db_table = "book_event"







# class feedback(models.Model):
 #    feedack_id = models.AutoField(Primary_key=True)
 #    feedback_name = models.CharField(null=False, max_length=50)
 #

 #    class Meta:
 #        db_table = "feedback"