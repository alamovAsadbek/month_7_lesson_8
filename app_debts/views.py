from django.contrib.auth.decorators import permission_required
from rest_framework.permissions import IsAuthenticated


@permission_required(IsAuthenticated)
def create_debt_view(request):
    pass
