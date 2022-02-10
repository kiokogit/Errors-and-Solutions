#create a fresh file

#made: views and api urls;
#working on response errors; 
# have known how to extract 
def userDetails(request):
    
    authhead = request.headers['Authorization']
    #and also the data
    rawJsonData = request.data