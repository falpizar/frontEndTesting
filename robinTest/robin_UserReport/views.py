from django.shortcuts import render
from .models import SupportedBank, ApplicationUser
from .SideBarModels import SideBarItem, SideBarItem_Spending, SideBarItem_Savings, SideBarItem_Retirement, SideBarItem_Investing, SideBarItem_PropertyAndDebt
from .HorizontalBarModels import HorizontalBarItem, HorizontalBarItem_Budget, HorizontalBarItem_Goals, HorizontalBarItem_Tools, HorizontalBarItem_UserProfile
from django.http import JsonResponse

def userMain(request):
    # some information about the system:
    #number_of_banks = SupportedBank.objects.all().count()
    #number_of_registered_users = ApplicationUser.objects.all().count()

    currentUserId = "mockUserId239487" # to be replaced with the user session id
    
    mainPageTitle = "My Financials"
    sideBarItemsList = [
        SideBarItem_Spending(),
        SideBarItem_Savings(),
        SideBarItem_Retirement(),
        SideBarItem_Investing(),
        SideBarItem_PropertyAndDebt(),
    ]
    horizontalBarItemsList = [
        HorizontalBarItem_UserProfile(),
        HorizontalBarItem_Goals(),
        HorizontalBarItem_Budget(),
        HorizontalBarItem_Tools(),
    ]
    return render(
        request,
        'user_main_page.html',
        context={
            'sideBarItemsList':sideBarItemsList,
            'horizontalBarItemsList':horizontalBarItemsList,
            'mainPageTitle':mainPageTitle,},
    )

def spendingAjaxSidebar(request):
    data = {
        'userData': SideBarItem_Spending().getUserData(),
    }
    return JsonResponse(data)