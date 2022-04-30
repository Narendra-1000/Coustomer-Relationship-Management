from django.shortcuts import render
import mysql.connector as sql
jr=''
jd=''
addr=''
num=''

# Create your views here.
def index(request):
    global jr,jd,addr,num
    if request.method == "POST":
        j=sql.connect(host="localhost",user="root",passwd="Nitin@1234",database='website', auth_plugin='mysql_native_password')
        cursor=j.cursor()
        d = request.POST
        for key,value in d.items():
            if(key == "Job"):
                jr = value
            if(key == "JobDescrip"):
                jd = value
            if(key == "inputAddress"):
                addr = value
            if(key == "customerPhone"):
                num = value  
        f = "insert into job Values('{}','{}','{}','{}')".format(jr,jd,addr,num)  
        cursor.execute(f)
        j.commit() 
              
    return render(request,"job_role.html")
