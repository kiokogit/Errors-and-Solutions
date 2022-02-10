#AUTH ERRORS
'FORBIDDEN ACCESS'
"""Do not use SETTINGS.PY settings for authentication(default auth)
It blocks all views from being accessed
Still, can use AllowAny if the site is to be freely accessed
"""
"ERROR CODES"
"""in an axios request, all errors are at the catch level.
if view response returns a status code recognized by browser as an error, 
it wil only be accessible through catch(e) block"""

"for reactjs: "
try{
    #some await action....
    #if successful, default code is 200
}catch(e){
    #use e.response.status
    if (e.response.status === 400) return #some alert or message
    #etc
}

"for python: "
try:
    #some action...
    await fetch(...)
except:
    #the error
    return #