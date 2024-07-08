from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import DBA

class EMPLOYEE:
    def __init__(self,EmpID=None,EmpName=None,DOJ=None,Salary=None,DID=None,Age=None,Country=None,Contact=None):
        self.id=EmpID
        self.name=EmpName
        self.doj=DOJ
        self.sal=Salary
        self.did=DID
        self.age=Age
        self.coun=Country
        self.con=Contact
    def fetch(self):
        f=DBA.fetchData()
        return f
    def insert(self):
        i=DBA.insertdata(self)
        return i
    def delete(self):
        d=DBA.deletedata(self)
        return d
    def update(self,a,b,c):
        u=DBA.updatedata(a,b,c)
        return u


app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")
temp = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def root(request:Request):
    return temp.TemplateResponse("home.html",{"request":request, "data":data})
 

@app.get('/data', response_class=HTMLResponse)
def data (request:Request):
   objfet=EMPLOYEE()
   data=objfet.fetch()
   print(data)
   return temp.TemplateResponse("data.html",{"request":request, "data":data})
               
@app.get('/insert', response_class=HTMLResponse)
@app.post('/insert', response_class=HTMLResponse)
async def Insert(request: Request):
   if request.method == 'POST':
       form_data = await request.form()
       a = form_data.get('EmpID')
       b = form_data.get('EmpName')
       c = form_data.get('DOJ')
       d = form_data.get('Salary')
       e = form_data.get('DID')
       f = form_data.get('Age')
       g = form_data.get('Country')
       h = form_data.get('Contact')
      
       objins=EMPLOYEE(a,b,c,d,e,f,g,h)
       objins.insert()
   return temp.TemplateResponse("Insert.html",{"request":request})

@app.get('/delete', response_class=HTMLResponse)
@app.post('/delete', response_class=HTMLResponse)
async def Delete(request:Request):
   if request.method == 'POST':
       del_data = await request.form()
       z = del_data.get('ID')
       objdel=EMPLOYEE(z)
       objdel.delete()

   return temp.TemplateResponse("delete.html",{"request":request})

@app.get('/update', response_class=HTMLResponse)
@app.post('/update', response_class=HTMLResponse)
async def Update(request:Request):
    if request.method == 'POST':
        up_data = await request.form()
        a = up_data.get('ask')
        b = up_data.get('newvalue')
        c = up_data.get('id')
        print(a,b,c)

        objup = EMPLOYEE()
        objup.update(a, b, c)
    return temp.TemplateResponse("update.html",{"request":request})

    



        



    


#------------------------------------------------------------------------------------------
#--------EMS Without FastApi---------------------------------------------------------------
# user=input("Enter F to fetch data or I to insert data:")
# if user == 'F':
#      objfet=EMPLOYEE()
#      data=objfet.fetch()
#      for i in data:
#          print('EmpID:',i[0],'EmpName:',i[1],'DOJ:',i[2],'Salary:',i[3],'DID:',i[4],'Age:',i[5],'Country:',i[6],'Contact:',i[7])
# elif user == 'I':
#      a=input("Enter ID:")
#      b=input("Enter Name:")
#      c=input("Enter Date of Joining:")
#      d=input("Enter Salary:")
#      e=input("Enter DID:")
#      f=input("Enter Age:")
#      g=input("Enter Country:")
#      h=input("Enter Contact:")
#      objins=EMPLOYEE(a,b,c,d,e,f,g,h)
#      objins.insert()
#      rows=objins.fetch()
#      print(rows)
# elif user == 'D':
#      z=int(input("Enter EmpID to delete your data:"))
#      objdel=EMPLOYEE(z)
#      objdel.delete()
# elif user == 'U':
#      ask=input("What you want to update?")
#      if ask == 'EmpID':
#          newv=int(input("Enter your id to update:"))
#          id1=int(input("Enter column id:"))
#          objup=EMPLOYEE()
#          objup.update(ask,newv,id1)
#      elif ask == 'EmpName':
#          name1=input("Enter your name to update:")
#          id1=int(input("Enter column id:"))
#          objup=EMPLOYEE()
#          objup.update(ask,name1,id1)
#      elif ask == 'Age':
#          age1=int(input("Enter your Age to update:"))
#          id1=int(input("Enter column id:"))
#          objup=EMPLOYEE()
#          objup.update(ask,age1,id1)
#      elif ask == 'DID':
#          did1=int(input("Enter your DID to update:"))
#          id1=int(input("Enter column id:"))
#          objup=EMPLOYEE()
#          objup.update(ask,did1,id1)
#      elif ask == 'DOJ':
#          doj1=input("Enter your DOJ to update:")
#          id1=int(input("Enter column id:"))
#          objup=EMPLOYEE()
#          objup.update(ask,doj1,id1)
#      elif ask == 'Salary':
#          sal1=int(input("Enter your Salary to update:"))
#          id1=int(input("Enter column id:"))
#          objup=EMPLOYEE()
#          objup.update(ask,sal1,id1)
#      elif ask == 'Country':
#          coun1=input("Enter your Country to update:")
#          id1=int(input("Enter column id:"))
#          objup=EMPLOYEE()
#          objup.update(ask,coun1,id1)
#      elif ask == 'Contact':
#          con1=int(input("Enter your Contact to update:"))
#          id1=int(input("Enter column id:"))
#          objup=EMPLOYEE()
#          objup.update(ask,con1,id1)
     










    

                                                    
