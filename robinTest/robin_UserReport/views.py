from django.shortcuts import render
from .models import SupportedBank, ApplicationUser, HorizontalBarItem
from .SideBarModels import SideBarItem, SideBarItem_Spending, SideBarItem_Savings, SideBarItem_Retirement, SideBarItem_Investing, SideBarItem_PropertyAndDebt

def userMain(request):
    # some information about the system:
    #number_of_banks = SupportedBank.objects.all().count()
    #number_of_registered_users = ApplicationUser.objects.all().count()

    currentUserId = "mockUserId239487" # to be replaced with the user session id
    
    mainPageTitle = "My Financials"
    sideBarItemsList = [
        SideBarItem_Spending(
            id="spendingSideBarItemMock",
            idText="spendingSideBarItemTextMock"),
        SideBarItem_Savings(
            id="savingsSideBarItemMock",
            idText="savingsSideBarItemTextMock"),
        SideBarItem_Retirement(
            id="retirementSideBarItemMock",
            idText="retirementSideBarItemTextMock"),
        SideBarItem_Investing(
            id="investingSideBarItemMock",
            idText="investingSideBarItemTextMock"),
        SideBarItem_PropertyAndDebt(
            id="propertyDebtsSideBarItemMock",
            idText="propertyDebtsSideBarItemTextMock"),
            ]
    horizontalBarItemsList = [
        HorizontalBarItem(name="Profile",   href=""),
        HorizontalBarItem(name="Goals",     href=""),
        HorizontalBarItem(name="Budget",    href=""),
        HorizontalBarItem(name="Tools",     href=""),
    ]
    return render(
        request,
        'user_main_page.html',
        context={
            'sideBarItemsList':sideBarItemsList,
            'horizontalBarItemsList':horizontalBarItemsList,
            'mainPageTitle':mainPageTitle,},
    )