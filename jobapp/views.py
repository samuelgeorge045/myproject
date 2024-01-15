from django.shortcuts import render, redirect
from .models import regimodel
from .forms import *
from .models import *
from jobportal.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import *
from django.contrib.auth import authenticate
import uuid
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html')


def regis(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pas=request.POST.get('password')
        if User.objects.filter(username=uname).first():
            messages.success(request,'username already taken')
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already taken')
            return redirect(regis)

        user_obj = User(username=uname,email=email)
        user_obj.set_password(pas)
        user_obj.save()

        auth_token=str(uuid.uuid4())
        profile_obj=profile1.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)
        return redirect(success)
    return render(request,'register.html')


def send_mail_regis(email,token):
    subject='your account has been verified'
    message=f'pass the link to verify your account http://127.0.0.1:8000/verify/{token}'


    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def success(request):
    return render(request,'success.html')


def login(request):
    global User
    if request.method=='POST':
        username=request.POST.get('uname')
        pas=request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return redirect(login)
        profile_obj=profile1.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check mail')
            return redirect(login)
        user=authenticate(username=username,password=pas)

        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(login)
        obj=profile1.objects.filter(user=user)
        return render(request,'chome.html',{'obj':obj})
    return render(request,'login.html')

def verify(request,auth_token):
    profile_obj=profile1.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            profile_obj.save()
            messages.success(request,'your account already verified')
            redirect(login)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account verified')
        return redirect(login)
    else:
        return redirect(error)

def error(request):
    return render(request,'error.html')


def usrregister(request):
    if request.method == 'POST':
        a=registerform(request.POST)
        if a.is_valid():
            usr=a.cleaned_data['usrnm']
            eml=a.cleaned_data['email']
            ph=a.cleaned_data['mob']
            birth=a.cleaned_data['dob']
            quali=a.cleaned_data['qual']
            pwd=a.cleaned_data['pas']
            cpwd = a.cleaned_data['cpas']
            if pwd == cpwd:
                b=regimodel(musr=usr,memail=eml,mmob=ph,mdob=birth,mqual=quali,mpas=pwd)
                b.save()
                #return HttpResponse('successfull')
                return redirect(usrlogin)
            else:
                return HttpResponse('password doesnt match')
        else:
            return HttpResponse('enter valid data')
    return render(request,'usrregister.html')

def usrlogin(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['usrname']
            pw=a.cleaned_data['pwd']
            b=regimodel.objects.all()
            for i in b:
                if un==i.musr and pw==i.mpas:
                    id=i.id
                    unm = i.musr
                    eml = i.memail
                    mob = i.mmob
                    dob = i.mdob
                    qua = i.mqual
                    # return HttpResponse('login success')
                    return render(request,'success.html',{'id':id,'unm':unm,'eml':eml,'mob':mob,'dob':dob,'qua':qua})
            else:
                return HttpResponse('incorrect credentials')
        else:
            return HttpResponse('enter valid data')
    else:
        return render(request,'usrlogin.html')

def edit_user(request,id):
    user=regimodel.objects.get(id=id)
    if request.method == 'POST':
        user.musr = request.POST.get('usn')
        user.memail = request.POST.get('em')
        user.mmob = request.POST.get('mo')
        # user.mdob = request.POST.get('do')
        user.mqual = request.POST.get('qua')
        user.save()
        return redirect(usrlogin)
    return render(request,'edituser.html',{'id':user})

def postjob(request,id):
    com=profile1.objects.get(id=id)
    if request.method == 'POST':
        a = jpostform(request.POST)
        if a.is_valid():
            cname = a.cleaned_data['cname']
            cmail = a.cleaned_data['cmail']
            jtitle = a.cleaned_data['jtitle']
            wtype = a.cleaned_data['wtype']
            exp = a.cleaned_data['exp']
            jtype = a.cleaned_data['jtype']

            b = jpostmodel(cname=cname, cemail=cmail, ctitle=jtitle, cwtyp=wtype, cjtyp=jtype, cjexp=exp)
            b.save()
            return HttpResponse('job successfully posted')
                # return redirect(usrlogin)
        else:
            return HttpResponse('enter valid data')

    return render(request,'jobform.html',{'com':com})

def viewjob(request,id):
    uid=id
    job=jpostmodel.objects.all()
    com = []
    mail= []
    title = []
    wtyp = []
    jtyp = []
    xp = []
    idi=[]
    for i in job:
        com.append(i.cname)
        mail.append(i.cemail)
        title.append(i.ctitle)
        wtyp.append(i.cwtyp)
        jtyp.append(i.cjtyp)
        xp.append(i.cjexp)
        idi.append(i.id)
    job_list = zip(com,idi,mail,title,wtyp,jtyp,xp)
    return render(request,'viewjobs.html',{'job':job_list,'user':uid})

def jobdet(request,id1,id2):
    uuid=id2
    job=jpostmodel.objects.get(id=id1)
    cnm=job.cname
    mail=job.cemail
    ttl=job.ctitle
    wtyp=job.cwtyp
    jtyp=job.cjtyp
    exp=job.cjexp
    cid=job.id
    return render(request,'jobdetail.html',{'uuid':uuid,'cnm':cnm,'mail':mail,'ttl':ttl,'wtyp':wtyp,'jtyp':jtyp,'exp':exp,'cid':cid})

def jobapply(request,comid,userid):
    uid=userid
    cd=comid
    job=jpostmodel.objects.get(id=comid)
    usr=regimodel.objects.get(id=userid)
    cnm=job.cname
    ttl=job.ctitle
    name=usr.musr
    mail=usr.memail
    qual=usr.mqual
    ph=usr.mmob
    xp=job.cjexp
    if request.method == 'POST':
        a = japp()#model

        a.ecom = request.POST.get('comname')
        a.edsgn = request.POST.get('dsgn')
        a.ename = request.POST.get('name')
        a.eemail = request.POST.get('mail')
        a.equal = request.POST.get('qual')
        a.eph = request.POST.get('phone')
        a.eexp = request.POST.get('exp')
        a.fil = request.FILES['cv']
        a.save()

        return HttpResponse('file uploaded')
    else :
        return render(request, 'jobapply.html',
                      {'uid': uid, 'cd': cd, 'cnm': cnm, 'ttl': ttl, 'name': name, 'mail': mail, 'qual': qual, 'ph': ph,
                       'xp': xp})

def applied(request,id):
    com = profile1.objects.get(id=id)
    com_name=com.user.username
    app=japp.objects.all()
    cname=[]
    dsgn=[]
    ename=[]
    eemail=[]
    equal=[]
    eph=[]
    exp=[]
    resume=[]
    apid=[]
    for i in app:
        if i.ecom==com_name:
                cname.append(i.ecom)
                dsgn.append(i.edsgn)
                ename.append(i.ename)
                eemail.append(i.eemail)
                equal.append(i.equal)
                eph.append(i.eph)
                exp.append(i.eexp)
                resume.append(str(i.resume).split('/')[-1])
                apid.append(i.id)
    app_list=zip(cname,dsgn,ename,eemail,equal,eph,exp,resume)
    return render(request, 'applications.html', {'app': app_list})

def viewcompany(request):
    obj=profile1.objects.all()
    company=[]
    ceml=[]
    cd=[]
    for i in obj:
        company.append(i.user.username)
        ceml.append(i.user.email)
        cd.append(i.user.id)

    com_list=zip(company,ceml,cd)
    return render(request,'viewcompany.html',{'com':com_list})

def japplied(request,id):
    comname=[]
    designation=[]
    usrid=id
    emp=regimodel.objects.get(id=usrid)
    ajob=japp.objects.all()
    for i in ajob:
        if emp.musr==i.ename:
            comname.append(i.ename)
            designation.append(i.edsgn)
        japp_list=zip(comname,designation)
    return render(request,'japplication.html',{'japp1':japp_list})

def sendmail(request,id):
    coid=id
    com=profile1.objects.get(id=coid)
    eml=com.user.email
    comm=com.user.username
    if request.method=='POST':
        sub=mailform(request.POST)
        if sub.is_valid():
            uname=sub.cleaned_data['username']
            email=sub.cleaned_data['email']
            subject=sub.cleaned_data['subject']
            msg=sub.cleaned_data['message']
            send_mail((str(uname))+'||'+str(subject),msg,EMAIL_HOST_USER,[email],fail_silently=False)
            return HttpResponse('send')
        else:
            return HttpResponse('not valid')
    return render(request, 'sendmail.html',{'eml': eml, 'comm': comm})

