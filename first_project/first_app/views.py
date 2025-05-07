from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Users
from first_app import forms

#?LOGIN/LOGOUTS IMPORTS
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required 


# Create your views here.
def index(Request):
    print('here',Request, type(Request))
    return HttpResponse("test onlysssss")


def index2(Request):
    print('here',Request, type(Request))
    return HttpResponse("new test onlysssss")


@login_required
def index3(Request):   
    webpages_list = AccessRecord.objects.order_by('date')
    
    context_sample = {'test_value': webpages_list}
    return render(Request,'first_app/first_app.html',context = context_sample)


@login_required
def users(request):
    users_list = Users.objects.order_by('firstname')
    context_dict = {'users': users_list, 'test_text': 'Filter this text if you can'}
    
    return render(request, 'first_app/users.html', context = context_dict)


def welcome_page(request):
    
    return render(request,'first_app/welcome.html')


def form_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            print('validating checking...')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    
    return render(request, 'first_app/form_page.html', {'form': form})



def form_signup_view(request):
    user_form = forms.UsersForm()
    profile_form = forms.ProfileInfoForm()
    
    registered = False
    if request.method == 'POST':
        user_form = forms.UsersForm(request.POST)
        profile_form = forms.ProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            print('user',user, type(user))
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit = False)
            profile.user = user 
            
            
            if 'profile' in request.FILES:
                profile.profile = request.FILES['profile']
                
            profile.save()
            
            registered = True          
        
        else:
            print('AN ERROR OCCURED')
            # raise forms.ValidationError('An Error Occured!')
        
    return render(request, 'first_app/form_page.html', {'user_form': user_form,
                                                        'profile_form': profile_form,
                                                        'registered': registered}                                                       
                                                        )
    

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('welcome_page'))
            
            else:
                return HttpResponse('ACCOUNT INACTIVE!')
            
            
        else:
            print('LOGIN ERROR')
            
            return HttpResponse('INVALID LOGIN DETAILS!')
    return render(request, 'first_app/login.html', {}) 


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome_page'))
    