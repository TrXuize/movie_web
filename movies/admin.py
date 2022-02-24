from django.contrib import admin
from .models import Movie
from .models import Cinema
from .models import Cinema_session
from .models import Seat
from .models import Ticket
# Register your models here.

admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Cinema_session)
admin.site.register(Seat)
admin.site.register(Ticket)