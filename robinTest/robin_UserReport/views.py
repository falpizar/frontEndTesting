from django.shortcuts import render
from .models import SupportedBank, ApplicationUser, SideBarItem, HorizontalBarItem

def index(request):
    # some information about the system:
    #number_of_banks = SupportedBank.objects.all().count()
    #number_of_registered_users = ApplicationUser.objects.all().count()

    currentUserId = "mockUserId" # to be replaced with the user session id
    
    mainPageTitle = "My Financials"
    sideBarItemsList = [
        SideBarItem(
            id="spendingSideBarItemMock",
            idText="spendingSideBarItemTextMock",
            text="Spending",
            userData="Mock Message for spending"),
        SideBarItem(
            id="savingsSideBarItemMock",
            idText="savingsSideBarItemTextMock",
            text="Savings",
            userData="Mock Message for savings; with additional stuff.."),
        SideBarItem(
            id="retirementSideBarItemMock",
            idText="retirementSideBarItemTextMock",
            text="Retirement",
            userData="Mock Message for retirement; with additional stuff too.."),
        SideBarItem(
            id="investingSideBarItemMock",
            idText="investingSideBarItemTextMock",
            text="Investing",
            userData="Mock Message for investing; with less stuff.."),
        SideBarItem(
            id="propertyDebtsSideBarItemMock",
            idText="propertyDebtsSideBarItemTextMock",
            text="Property & Debt",
            userData="Mock Message for propertyDebts;.."),
            ]
    horizontalBarItemsList = [
        HorizontalBarItem(name="Profile",   href=""),
        HorizontalBarItem(name="Goals",     href=""),
        HorizontalBarItem(name="Budget",    href=""),
        HorizontalBarItem(name="Tools",     href=""),
    ]
    return render(
        request,
        'index.html',
        context={
            'sideBarItemsList':sideBarItemsList,
            'horizontalBarItemsList':horizontalBarItemsList,
            'mainPageTitle':mainPageTitle,},
    )