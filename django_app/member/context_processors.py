from .forms import SignupForm
from .forms import LoginForm


def forms(request):
    context = {
        'login_form' : LoginForm(),
    }
    return context

def forms(request):
    context = {
        'signup_form' : SignupForm(),
    }
    return context