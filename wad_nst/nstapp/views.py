import os
import sys

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm,FeedbackForm,UserUpdateForm,ProfileUpdateForm

PACKAGE_PARENT = ".."
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from nstapp.ML.nst_run import run


def home(request):
    return render(request, "home.html")


def signupuser(request):
    """ 
    Signup function to register the user into the website 
    for that We are using django inbuilt model User and added
    extra field email in USerCreationForm and Created a new Form 
    As User RegistrationForm in forms.py.

    When we get a request.POST method we are checking for some
    variables and afterwards we are the form into database. 

    Returns
    -------
        After sucess we are redirection user to the home page.
    """    
    if request.method == "GET":
        return render(request, "signupuser.html", {"forms": UserRegistrationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"],email = request.POST['email']
                )
                user.save()
                # When user signed in redirect to new url.
                login(request, user)
                return redirect("home")

            except IntegrityError:
                return render(
                    request,
                    "signupuser.html",
                    {"forms": UserRegistrationForm(), "error": "Username is already taken try other!"},
                )

        else:
            # Tell the use user password didn't match.
            return render(
                request,
                "signupuser.html",
                {"forms": UserCreationForm(), "error": "Password did not match"},
            )


def about(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")


def logoutuser(request):
    """
    Logging out the user using django inbuil function logout()

    Returns
    -------
        After logging out we are redirectiong user to the home
        page.
    """    
    logout(request)
    return redirect("home")


def loginuser(request):
    """
    Logging in the user into the website for that we are using 
    django form AuthenticationForm() when we get POST method we 
    authenticate the user from data we have in database. If didn't 
    match e return an error. Then redirect it to the home page.

    Parameters
    ----------
    request : 
        Httprequest Django creates an HttpRequest object that 
        contains metadata about the request. Then Django loads
        the appropriate view, passing the HttpRequest as the 
        first argument to the view function. Each view is 
        responsible for returning an HttpResponse object.

    Returns
    -------
    If it's a gett method e return form. Else if a post method 
    and no error if redirect to home page or else we return error.
        
    """    
    if request.method == "GET":
        return render(request, "loginuser.html", {"forms": AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            return render(
                request,
                "loginuser.html",
                {"forms": AuthenticationForm(), "error": "Username and password did not match"},
            )
        else:
            login(request, user)
            return redirect("home")


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES["image"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context["url"] = fs.url(name)
        print(url)
        print(uploaded_file.size)
    return render(request, "upload.html")


def profile(request):
    return render(request,'profile.html')


def feedback(request):
    if request.method == 'GET':
        return render(request,'feedback.html',{'form':FeedbackForm()})
    else :
        try :
            form = FeedbackForm(request.POST)           # Put all the data we get from webpage 
            newtodo = form.save()                             # Saving the value.
            return redirect('home')
        except ValueError :
            return render(request,'feedback.html',{'form':FeedbackForm(),'error':"Bad Data Try Again !"})


def profileUpdate(request):
    if  request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            return redirect('profile')
        else :
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

            context = {
                'u_form':u_form,
                'p_form':p_form
            }
            return render(request,'profileUpdate.html',context,{'error':'Bad Data ! Try Again' })

    else :
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form':u_form,
            'p_form':p_form
        }
        return render(request,'profileUpdate.html',context)