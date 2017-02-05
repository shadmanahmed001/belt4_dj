from django.shortcuts import render, redirect
from .models import User, Item, Wish_list
from django.contrib import messages
from datetime import datetime, date

def index(request):
		return render(request,"belt4_app/main.html")

def dashboard(request):
	mywishlist = Wish_list.objects.filter(useradding= request.session['user_id'])

	usertoshowlist = User.objects.filter(id=request.session['user_id'])
	usertoshow = usertoshowlist[0]

	wishlist = Wish_list.objects.all()
	wishlist_ids = wishlist.values_list('id', flat=True)
	mywishlist_ids = Wish_list.objects.filter(useradding = usertoshow)
	if mywishlist_ids:
		me = mywishlist_ids[0]
	else:
		pass
	# check if this works
# or should i be getting the id of the person logged in
	# notmywishlist = usertoshow.friends.values_list('id', flat=True)
	notmywishlist = Wish_list.objects.exclude(id__in=wishlist_ids)

	otheruserswishlist = Wish_list.objects.exclude(useradding= request.session['user_id'])
	context = {
	'items':mywishlist,
	'otherswishlist' : otheruserswishlist
	}

	return render(request,"belt4_app/dashboard.html", context)

def addtomy(request, id, aid):
	uid = request.session['user_id']
	results = Wish_list.objects.addtomy(id, uid)
	if results:
		return redirect ('/dashboard')

def show(request, id):
	allitemslist = Item.objects.filter(id=id)
	allpplwishlist= Wish_list.objects.filter(itemsadded=id)
	context = {
	'allitems':allitemslist[0],
	'allpplwish':allpplwishlist
	}
	print allpplwishlist
	return render(request,"belt4_app/show.html", context)

def delete(request, id):
	results = Item.objects.delete(id)
	if results:
		return redirect ('/dashboard')

def additem(request):
	return render(request,"belt4_app/additem.html")

def addingitem(request, id):
	if request.method =='POST':
		results = Item.objects.addingitem(request.POST, id)
		if results['status']:
			return redirect ('/dashboard')
		else:
			for errorStr in results['errors']:
				messages.error(request, errorStr)
				return redirect ('/additem')

def login(request):
	if request.method == 'POST':
		result = User.objects.login(request.POST)
		if result['status']:
			request.session['user_id'] = result['user_id']
			request.session['name'] = result['user_name']
			return redirect ('/dashboard')
		else:
			for errorStr in result['errors']:
				messages.error(request, errorStr)
				return redirect ('/')

def register(request):
	if request.method == 'POST':
		result = User.objects.register(request.POST)
		if result['status']:
			request.session['user_id'] = result['user_id']
			request.session['name'] = result['name']
			return redirect ('/dashboard')
		else:
			for errorStr in result['errors']:
				messages.error(request, errorStr)
	return redirect ('/')

def logout(request):
	request.session.clear()
	return redirect ('/')
