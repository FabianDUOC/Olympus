from .forms import DirecForm, UserLoginForm, UserSignUpForm


def login_form(request):
    login_form = UserLoginForm()
    signup_form = UserSignUpForm()
    direc_form = DirecForm()
    return {
        'loginForm': login_form,
        'signupForm': signup_form,
        'direcForm': direc_form,
    }