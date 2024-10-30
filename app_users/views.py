from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def register_user(request):
    if request.method == 'POST':
        # code to register user
        pass
    else:
        # code to display registration form
        pass
