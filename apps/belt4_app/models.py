from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
	def login(self, post):
		email = post['email'].lower().strip()
		password = post['password']

		errors =[]
		if len(email) == 0:
			errors.append('email is required')
		elif not User.objects.filter(email = email).exists():
			errors.append('email is not in the database')

		if not errors:
			user_list = User.objects.filter(email = email)
			user = user_list[0]
			password = password.encode()
			ps_hashed = user.password.encode()
			if bcrypt.hashpw(password, ps_hashed) == ps_hashed:
				return {'status': True, 'user_id': user.id, 'user_name' : user.name}
			else:
				errors.append('email or password does not match')
		return {'status': False, 'errors': errors}

	def register(self, post):
		email = post['email'].lower().strip()
		name = post['name']
		last = post['last']
		password = post['password']
		confirm_password = post['confirm_password']

		errors = []
		if not EMAIL_REGEX.match(email):
			errors.append(' Invalid email ')
		if not NAME_REGEX.match(name):
			errors.append(' Invalid name ')
		if not NAME_REGEX.match(last):
			errors.append(' Invalid last ')
		if len(password) < 8:
			errors.append(' Password must be atleast 8 characters long ')
		elif password != confirm_password:
			errors.append(' Password and confirm password are not matched ')

		if not errors:
			already_user_list = User.objects.filter(email=email)
			if not already_user_list:
				password = password.encode()
				hashed = bcrypt.hashpw(password, bcrypt.gensalt())
				print "this means new user"
				user = User.objects.create(name=name,last=last,email = email,password=hashed,)
				print ('**************')
				return {'status': True, 'user_id': user.id, 'name' : name}
			else:
				errors.append('Please login below. Your email already exists in our DB')
				print 'this means its a returning user but logging in the wrong place'

		return {'status': False, 'errors': errors}

	def addingitem(self, post, id):
		item = post['item']
		if len(item) == 0 or len(item) < 3:
			errors = []
			errors.append('Empty field!')
			return {'status': False, 'errors': errors}
		added_by = id
		user_list= User.objects.filter(id=id)
		user = user_list[0]
		Item.objects.create(item=item, added_by= user)
		item_list = Item.objects.filter(item=item, added_by=user)
		item = item_list[0]
		Wish_list.objects.create(useradding= user, itemsadded=item)
		print item
		print id
		return {
		'status' : True
		}

	def addtomy(self, id, uid):
		itemsfilter = Item.objects.filter(id=id)
		userfilter = User.objects.filter(id=uid)
		Wish_list.objects.create(itemsadded= itemsfilter[0], useradding= userfilter[0])
		return True

	def delete(self, id):
		Item.objects.filter(id=id).delete()
		return True


class User(models.Model):
	name = models.CharField(max_length=45)
	last = models.CharField(max_length=45)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
class Item(models.Model):
	item = models.CharField(max_length=45)
	added_by = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
class Wish_list(models.Model):
	useradding = models.ForeignKey(User)
	itemsadded = models.ForeignKey(Item)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
