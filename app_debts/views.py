from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_required(IsAuthenticated)
def debts_view(request):
    pass
