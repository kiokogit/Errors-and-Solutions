#1. Django logout function
"""Logout() takes onlly one arg, two provided"""
#import logout from django.contrib.auth,
#import redirect from django.shortcuts
def logoutFunct(request):
    logout(request);
    return redirect('home');

#2. REQUIRE AUTH FOR DASHBOARD, by using decorators
#import login_required from django.contrib.auth.decorators
@login_required(login_url='login')     #before a view function declaration

#decorators start with the '@' sign
#3. APPEND_SLASH
#while building the API, A runtime error is thrown indicating that for POST requests, urls must have a trailing slash at the end
#be default. Else, set, in Django settings:
APPEND_SLASH=False
#in the end, instead of append_slash=False, I decided to add the trailing sklashes

#4. REQUEST DATA TYPE - BYTES
#apparently, the request data received through an api is in type bytes - not the normal XML form data
#so we cannot just take form = someForm(request.POST);

#so to extract it:
" get the raw data from request.data, rather than req.body. Req.body extracts pure raw strings and bytes";
def signup(request):
    rawData=request.data   #this set data into dictionary format, and can fetch using keys
    #eg
    email=rawData['email']
    password=rawData['password']
    #then match the data with the form fields
    formdata = {'email':email, 'password':password}
    #with this object, map to form model, and validate. if fine, save
    form=regForm(formdata);
    if form.is_valid():
        form.save(commit=True); #can do more of cleaning etc