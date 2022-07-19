from django.db import models

# Create your models here.

class Tbl_User(models.Model):
	name=models.CharField(max_length=30,default='')
	gender=models.CharField(max_length=30,default='')
	phone=models.CharField(max_length=50,default='')
	dob=models.CharField(max_length=30,default='')
	address=models.CharField(max_length=30,default='')
	email=models.CharField(max_length=30,default='')
	pswd=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')
	user_type=models.CharField(max_length=30,default='')

class Tbl_Question(models.Model):
	question=models.CharField(max_length=300,default='')
	option1=models.CharField(max_length=30,default='')
	option2=models.CharField(max_length=50,default='')
	option3=models.CharField(max_length=30,default='')
	option4=models.CharField(max_length=30,default='')

class Tbl_Feedback(models.Model):
	user_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	feedback=models.CharField(max_length=30,default='')
	date=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=50,default='')

class Tbl_selfcorner(models.Model):
	user_id=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)
	sub=models.CharField(max_length=30,default='')
	journal=models.CharField(max_length=30,default='')
	date=models.CharField(max_length=50,default='')
	tip=models.CharField(max_length=50,default='')
	tip_date=models.CharField(max_length=50,default='')

class Tbl_result(models.Model):
	user_ID=models.ForeignKey(Tbl_User,on_delete=models.CASCADE, blank=True,null=True)		
	answer=models.CharField(max_length=300,default='')
	total=models.CharField(max_length=300,default='')
	status=models.CharField(max_length=300,default='')
	doctor=models.CharField(max_length=50,default='0')
	report_status=models.CharField(max_length=300,default='')
	description=models.CharField(max_length=300,default='')
	
