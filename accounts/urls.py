from django.contrib import admin
from django.urls import path
from . import views
from klub import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginPage,name="loginpage"),
    path('home/', views.home_page,name="home"),
    path('players/', views.players,name="players"),
    path('create_players/', views.newPlayer,name="create_players"),
    path('update_players/<str:pk>/', views.updatePlayer,name="update_player"),
    path('delete_players/<str:pk>/', views.deletePlayer,name="delete_player"),
    path('members/', views.members,name="members"),
    path('create_member/', views.newMember,name="create_member"),
    path('update_member/<str:pk>/', views.updateMember,name="update_member"),
    path('delete_member/<str:pk>/', views.deleteMember,name="delete_member"),
    path('adminpage/', views.admin_page,name="adminpage"),
    path('administration/', views.signup,name="signup"),
    path('tracking/', views.tracking,name="tracking"),
    path('staff/', views.staff,name="staff"),
    path('create_staff/', views.newStaff,name="create_staff"),
    path('update_staff/<str:pk>/', views.updateStaff,name="update_staff"),
    path('delete_staff/<str:pk>/', views.deleteStaff,name="delete_staff"),
    path('economy/', views.economy,name="economy"),
    path('In-Out/', views.inout,name="inout"),
    path('Income/', views.income,name="income"),
    path('Outcome/', views.outcome,name="outcome"),
    path('Player_graf/', views.plgraf,name="players_graf"),
    path('Staff_graf/', views.stgraf,name="staff_graf"),
    path('Sponzors_graf/', views.spgraf,name="sponzors_graf"),
    path('Sponzors', views.sponzori,name="sponzors"),
    path('Stadion', views.stadion,name="stadion"),
    path('East', views.east,name="east"),
    path('West', views.west,name="west"),
    path('South', views.south,name="south"),
    path('North', views.north,name="north"),
    path('Željeznicar_info', views.info,name="info"),
    path('Stadion_info', views.stadioninfo,name="stadioninfo"),
    path('Grbavica', views.grbavica,name="grbavica"),
    path('Galerija', views.galerija,name="galerija"),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('New_income/', views.newPrihod,name="add_income"),
    path('New_outcome/', views.newRashod,name="add_outcome"),
    path('Other_income/', views.other_income,name="other_income"),
    path('Other_outcome/', views.other_outcome,name="other_outcome"),

    ]