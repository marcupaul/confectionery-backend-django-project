from django.contrib import admin
from .models import Fridge
from .models import Confection
from .models import Rat
from .models import ClaimedCheese

admin.site.register(Fridge)
admin.site.register(Confection)
admin.site.register(Rat)
admin.site.register(ClaimedCheese)
