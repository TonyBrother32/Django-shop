from functools import partial
from django.contrib.auth.decorators import user_passes_test


superuser_required= partial( user_passes_test(lambda u: u.is_superuser))
