from django.shortcuts import render
from .models import Tgusers,Button
from scripts import hexa
from django.db import connection
print(connection.queries)
# Create your views here.

def home(request):

    # loading values of singleton Model 
    upd=Button.load()
    psbc=upd.stupid_btn_counter
    pfbc=upd.fat_btn_counter
    pdbc=upd.dumb_btn_counter
    f = open("tempdatastorage.txt", "r")
    bvalues=f.read()
    sbc=int(bvalues[1])
    fbc=int(bvalues[4])
    dbc=int(bvalues[7])
    sbc=sbc+psbc
    fbc=fbc+pfbc
    dbc=dbc+pdbc
    #saving updated value to singleton model 
    #loading the single object with id 1
    ypd=Button.objects.get(id=1)
    #updating new values to fields
    ypd.stupid_btn_counter=sbc
    ypd.fat_btn_counter=fbc
    ypd.dumb_btn_counter=dbc
    ypd.save()
   


    #loading and updating user fields

    user_details=[]
    with open('tempuserstorage.txt', 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]

            # add current item to the list
            user_details.append(x)
        
   # print(user_details[1])
    user_id=user_details[0]
    username=user_details[1]
    stupidbtn=user_details[2]
    fatbtn=user_details[3]
    dumbbtn=user_details[4]
    checker=Tgusers.objects.filter(tguser_id=user_id).exists()
    if checker:
        usd=Tgusers.objects.get(tguser_id=user_id)
        usd.users_name=username
        usd.stupid_btn_counter=stupidbtn
        usd.fat_btn_counter=fatbtn
        usd.dumb_btn_counter=dumbbtn
        usd.save()
    if not checker:
        usdn=Tgusers(tguser_id=user_id,users_name=username,stupid_btn_counter=stupidbtn,fat_btn_counter=fatbtn,dumb_btn_counter=dumbbtn)
        usdn.save()
         
   



    

    return render(request,'index.html')

def features(request):
    return render(request,'features.html')
def userdetails(request):

    tgusers_dict={
        'mdv':Tgusers.objects.all()

    }

    
    return render(request,'userdetails.html',tgusers_dict)


