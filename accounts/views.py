from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .forms import PlayersForm,MembersForm,StaffForm,PrihodForm,RashodForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginPage(request):
    track = Track.objects.filter(datumIzmjene__lte=datetime.now()-timedelta(days=7)).delete()
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,"accounts/index.html")
@login_required(login_url='loginpage')
def home_page(request):
    
    return render(request,"accounts/news.html")

@login_required(login_url='loginpage')
def players(request):
    players = Players.objects.all()
        
    return render(request,"accounts/players.html",{'players':players})

@login_required(login_url='loginpage')
def newPlayer(request):
    username = request.user.username
    form = PlayersForm()
    if request.method == 'POST':
        #print("print post: ",request.Post)
        form = PlayersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('players')
    b = Track(user=username, modul='Players',tipPromjene='Add Player')
    b.save()
    context={'form':form}
    return render(request,"accounts/new_player.html",context)

@login_required(login_url='loginpage')
def updatePlayer(request,pk):
    username = request.user.username
    player = Players.objects.get(id=pk)
    form = PlayersForm(instance=player)
    if request.method == 'POST':
        #print("print post: ",request.Post)
        form = PlayersForm(request.POST,instance=player)
        if form.is_valid():
            form.save()
            return redirect('players')
    b = Track(user=username, modul='Players',tipPromjene='Update Player')
    b.save()
    context={'form':form}
    return render(request,"accounts/new_player.html",context)


def deletePlayer(request,pk):
    username = request.user.username
    player = Players.objects.get(id=pk)
    if request.method == 'POST':
        
        player.delete()
        return redirect('players')
    b = Track(user=username, modul='Players',tipPromjene='Delete Player')
    b.save()
    context={'item':player}
    return render(request,"accounts/delete_player.html",context)

@login_required(login_url='loginpage')
def members(request):
    members = Members.objects.all()
        
    return render(request,"accounts/members.html",{'members':members})

@login_required(login_url='loginpage')
def newMember(request):
    
    username = request.user.username
       
    form = MembersForm()
    if request.method == 'POST':
        #print("print post: ",request.Post)
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('members')
    b = Track(user=username, modul='Members',tipPromjene='Add Member')
    b.save()
    context={'form':form}
    return render(request,"accounts/new_member.html",context)

@login_required(login_url='loginpage')
def updateMember(request,pk):
    username = request.user.username
    member = Members.objects.get(id=pk)
    form = MembersForm(instance=member)
    if request.method == 'POST':
        #print("print post: ",request.Post)
        form = MembersForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect('members')
    b = Track(user=username, modul='Members',tipPromjene='Update Member')
    b.save()
    context={'form':form}
    return render(request,"accounts/new_member.html",context)

@login_required(login_url='loginpage')
def deleteMember(request,pk):
    username = request.user.username
    member = Members.objects.get(id=pk)
    if request.method == 'POST':
        
        member.delete()
        return redirect('members')
    b = Track(user=username, modul='Members',tipPromjene='Delete Member')
    b.save()
    context={'item':member}
    return render(request,"accounts/delete_member.html",context)

@login_required(login_url='loginpage')
def event():
    event = Track.objects.all()
    return event


@login_required(login_url='loginpage')
def signup(request):
    
    username = request.user.username
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password,is_staff=True,is_admin=True)
           

            login(request, user)
            return redirect('adminpage')
    
    else:
        form = UserCreationForm()

    b = Track(user=username, modul='Members',tipPromjene='Add User')
    b.save()
    return render(request, 'accounts/administration.html', {'form': form})

@login_required(login_url='loginpage')
def admin_page(request):
    member = Members.objects.all().count()
    players = Players.objects.all().count()
    user = User.objects.all().count()
    users = User.objects.all()
    staff = Staff.objects.all().count()


    context={
        'member':member,
        'players':players,
        'user':user,
        'users':users,
        'staff':staff
    }
    return render(request,"accounts/adminpanel.html",context)

@login_required(login_url='loginpage')
def tracking(request):
    
    form = Track.objects.all()


    context={
        
        'form':form
    }
    return render(request,"accounts/tracking.html",context)

@login_required(login_url='loginpage')
def staff(request):
    members = Staff.objects.all()
        
    return render(request,"accounts/staff.html",{'members':members})

@login_required(login_url='loginpage')
def newStaff(request):
    
    username = request.user.username
       
    form = StaffForm()
    if request.method == 'POST':
        #print("print post: ",request.Post)
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('staff')
    b = Track(user=username, modul='Staff',tipPromjene='Add Staff')
    b.save()
    context={'form':form}
    return render(request,"accounts/new_staff.html",context)

@login_required(login_url='loginpage')
def updateStaff(request,pk):
    username = request.user.username
    member = Staff.objects.get(id=pk)
    form = StaffForm(instance=member)
    if request.method == 'POST':
        #print("print post: ",request.Post)
        form = StaffForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect('staff')
    b = Track(user=username, modul='Staff',tipPromjene='Update Staff')
    b.save()
    context={'form':form}
    return render(request,"accounts/new_staff.html",context)

@login_required(login_url='loginpage')
def deleteStaff(request,pk):
    username = request.user.username
    member = Staff.objects.get(id=pk)
    if request.method == 'POST':
        
        member.delete()
        return redirect('staff')
    b = Track(user=username, modul='Staff',tipPromjene='Delete Staff')
    b.save()
    context={'item':member}
    return render(request,"accounts/delete_staff.html",context)

@login_required(login_url='loginpage')
def economy(request):
    odrzavanje_terena = 2500
    sponzors = Sponzors.objects.all()
    sa_sponzors = sum(sponzors.values_list('Cijena_sponzorstva', flat=True))
    players = Players.objects.all()
    sa_players = sum(players.values_list('plata', flat=True))    #sum svih plata igraca
    staff = Staff.objects.all()
    sa_staff = sum(staff.values_list('plata', flat=True))
    member = Members.objects.all().count()
    sa_member=member*20
    total=sa_players+sa_staff+sa_member+odrzavanje_terena
    context={
        'sa_players':sa_players,
        'sa_staff':sa_staff,
        'sa_member':sa_member,
        'total':total,
        'sa_sponzors':sa_sponzors,
        'odrzavanje_terena':odrzavanje_terena

    }
    return render(request,"accounts/economy.html",context)

@login_required(login_url='loginpage')
def inout(request):
    
    odrzavanje_terena = 2500
    sponzors = Sponzors.objects.all()
    sa_sponzors = sum(sponzors.values_list('Cijena_sponzorstva', flat=True))
    players = Players.objects.all()
    sa_players = sum(players.values_list('plata', flat=True))    #sum svih plata igraca
    staff = Staff.objects.all()
    sa_staff = sum(staff.values_list('plata', flat=True))
    member = Members.objects.all().count()
    sa_member=member*20
    income= Prihod.objects.all()
    oth_Income = sum(income.values_list('Cijena', flat=True))
    outcome = Rashod.objects.all()
    oth_Outcome = sum(outcome.values_list('Cijena', flat=True))
    total_o=sa_players+sa_staff+odrzavanje_terena+oth_Outcome
    total_i=sa_sponzors+sa_member+oth_Income
   
    label=['Income','Outcome']
    data=[total_i,total_o]

    
    return render(request,"accounts/economy.html",{'label':label,'data':data})

@login_required(login_url='loginpage')
def income(request):
    
    odrzavanje_terena = 2500
    sponzors = Sponzors.objects.all()
    sa_sponzors = sum(sponzors.values_list('Cijena_sponzorstva', flat=True))
    players = Players.objects.all()
    sa_players = sum(players.values_list('plata', flat=True))    #sum svih plata igraca
    staff = Staff.objects.all()
    sa_staff = sum(staff.values_list('plata', flat=True))
    member = Members.objects.all().count()
    sa_member=member*20
    income= Prihod.objects.all()
    oth_Income = sum(income.values_list('Cijena', flat=True))
    
    label=['Sponzors','Members','Other Income']
    data=[sa_sponzors,sa_member,oth_Income]

    
    return render(request,"accounts/economy1.html",{'label':label,'data':data})

@login_required(login_url='loginpage')
def outcome(request):
    
    odrzavanje_terena = 2500
    
    players = Players.objects.all()
    sa_players = sum(players.values_list('plata', flat=True))    #sum svih plata igraca
    staff = Staff.objects.all()
    sa_staff = sum(staff.values_list('plata', flat=True))
    outcome = Rashod.objects.all()
    oth_Outcome = sum(outcome.values_list('Cijena', flat=True))
    
    label=['Players','Staff','Terrain maintenance','Other outcome']
    data=[sa_players,sa_staff,odrzavanje_terena,oth_Outcome]

    
    return render(request,"accounts/economy2.html",{'label':label,'data':data})

@login_required(login_url='loginpage')
def plgraf(request):
    
    
    players = Players.objects.all()
    
    
    return render(request,"accounts/economy3.html",{'players':players})

@login_required(login_url='loginpage')
def stgraf(request):
    
    
    players = Staff.objects.all()
    
    
    return render(request,"accounts/economy4.html",{'players':players})

@login_required(login_url='loginpage')
def spgraf(request):
    
    players = Sponzors.objects.all()
    
    
    return render(request,"accounts/economy5.html",{'players':players})

@login_required(login_url='loginpage')
def sponzori(request):
   
    return render(request,"accounts/sponzori.html")

@login_required(login_url='loginpage')
def stadion(request):
       
    return render(request,"accounts/stadion.html")

@login_required(login_url='loginpage')
def east(request):
       
    return render(request,"accounts/east.html")

@login_required(login_url='loginpage')
def west(request):
       
    return render(request,"accounts/west.html")

@login_required(login_url='loginpage')
def south(request):
       
    return render(request,"accounts/south.html")

@login_required(login_url='loginpage')
def north(request):
       
    return render(request,"accounts/north.html")

@login_required(login_url='loginpage')
def info(request):
       
    return render(request,"accounts/zeljoinfo.html")

@login_required(login_url='loginpage')
def stadioninfo(request):
       
    return render(request,"accounts/stadionInfo.html")

@login_required(login_url='loginpage')
def grbavica(request):
       
    return render(request,"accounts/grbavica.html")

@login_required(login_url='loginpage')
def galerija(request):
       
    return render(request,"accounts/galerija.html")

@login_required(login_url='loginpage')
def logout(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def newPrihod(request):
    
    username = request.user.username
       
    form = PrihodForm()
    if request.method == 'POST':
        #print("print post: ",request.Post)
        form = PrihodForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('inout')
    b = Track(user=username, modul='Income',tipPromjene='Add Income')
    b.save()
    context={'form':form}
    return render(request,"accounts/new_prihod.html",context)

@login_required(login_url='loginpage')
def newRashod(request):
    
    username = request.user.username
       
    form = RashodForm()
    if request.method == 'POST':
        #print("print post: ",request.Post)
        form = RashodForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('inout')
    b = Track(user=username, modul='Outcome',tipPromjene='Add Outcome')
    b.save()
    context={'form':form}
    return render(request,"accounts/new_rashod.html",context)

@login_required(login_url='loginpage')
def other_income(request):
    
    
    players = Prihod.objects.all()
    
    
    return render(request,"accounts/other_income.html",{'players':players})

@login_required(login_url='loginpage')
def other_outcome(request):
    
    
    players = Rashod.objects.all()
    
    
    return render(request,"accounts/other_outcome.html",{'players':players})