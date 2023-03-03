from django.contrib import admin

# import the model Todo
from .models import Todo

# create a class for the admin-model integration
class TodoAdmin(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ("title","description","completed")

admin.site.register(Todo,TodoAdmin)

