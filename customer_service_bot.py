def cs_service_bot():
    user_response = input("Hello! Welcome to the DNS Cable Company's Service Portal. \n \
    Are you a new or existing customer? \n \
    [1] New Customer \n \
    [2] Existing Customer \n \
    Please enter the number coresponding to the appropriate response.")
    
    if user_response == 1:
        new_customer()
    elif user_response == 2:
        existing_customer()
    else:
        print("Sorry, we did not understand your selection.")
        cs_service_bot()
 
 def existing_customer():
    user_support_response = input("What kind of support do you need? \n \
    [1] Television Support \n \
    [2] Internet Support \n \
    [3] Speak to a support representative \n \
    Please enter the number coresponding to the appropriate response.")
    
    if user_support_response == 1:
        television_support()
    elif user_support_response == 2:
        internet_support()
    elif user_support_response == 3:
        live_rep("support")
    else:
        print("Sorry, we did not understand your selection.")
        existing_customer()

def new_customer():
    new_user_response = input("We're excited to have you join the DNS family, how can we help you? \n \
    [1] Sign up for service. \n \
    [2] Schedule a home visit. \n \
    [3] Speak to a sales representative. \n \
    Please enter the number coresponding to the appropriate response.")
    
    if new_user_response == 1:
        sign_up()
    elif new_user_response == 2:
        home_visit()
    elif new_user_response == 3:
        live_rep("sales")
    else:
        print("Sorry, we did not understand your selection.")
        new_customer()

def television_support():
    user_tv_response = input("What is the nature of your problem? \n \
    [1] I can't access certain channels. \n \
    [2] My picture is blurry. \n \
    [3] I keep losing service. \n \
    [4] Other issues. \n \
    Please enter the number coresponding to the appropriate response.")
    
    if user_tv_response == 1:
        print ("Please check the channel lists at DefinitelyNotSinister.com. \n \
        If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif user_tv_response == 2:
        print ("Try adjusting the antenna above your television set.")
        did_that_help()
    elif user_tv_response == 3:
        print ("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif user_tv_response == 4:
        live_rep("support")
    else:
        print("Sorry, we did not understand your selection.")
        television_support()

def internet_support():
    user_net_response = input("What is the nature of your problem? \n \
    [1] I can't connect to the internet. \n \
    [2] My connection is very slow. \n \
    [3] I can't access certain sites. \n \
    [4] Other issues. \n \
    Please enter the number coresponding to the appropriate response.")
    
    if user_net_response == 1:
        print ("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif user_net_response == 2:
        print ("Make sure that all cell phones and other peoples computers \n \
        are not connected to the internet, so that you can have all the bandwidth.")
        did_that_help()
    elif user_net_response == 3:
        print ("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif user_net_response == 4:
        live_rep("support")
    else:
        print("Sorry, we did not understand your selection.")
        internet_support()

def did_that_help():
    user_help_response = input("Did that resolve your problem? \n \
    [1] Yes \n \
    [2] No \n \
    Please enter the number coresponding to the appropriate response.")
    
    if user_help_response == 1:
        print("Thank you and have a nice day!")
    elif user_help_response == 2:
        did_that_help2()
    else:
        print("Sorry, we did not understand your selection.")
        did_that_help()

def did_that_help2 ():
    u_h_p2 = input("Would you like \n \
        [1] To contact a live representative? \n \
        [2] Or schedule a home visit? \n \
        Please enter the number coresponding to the appropriate response.")
    if u_h_r2 == 1:
        live_rep("support")
    elif u_h_r2 == 2:
        home_visit("support")
    else:
        print("Sorry, we did not understand your selection.")
        did_that_help2()

def sign_up():
    new_user_response = input("Great choice, friend! \n \
    We're excited to have you join the DNS family! \n \
    Please select the package you are interested in signing up for. \n \
    [1] Bundle Deal (Internet + Cable) \n \
    [2] Internet \n \
    [3] Cable \n \
    Please enter the number coresponding to the appropriate response.")
    
    if new_user_input == 1:
        print("You've selected the Bundle Package! \n \
        Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif new_user_input == 2:
        print("You've selected the Internet Only Package! \n \
        Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif new_user_input == 3:
        print("You've selected the Cable Only Package! \n \
        Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    else:
        print("Sorry, we did not understand your selection.")
        sign_up()
        
def home_visit(purpose="none"):
    if purpose == "none":
        purpose = input("For what prupose are you requesting a home visit? \n \
        [1] New service installation. \n \
        [2] Exisitng service repair. \n \
        [3] Location scouting for unserviced region. \n \
        Please enter the number coresponding to the appropriate response.")
        if purpose == 1:
            home_visit("new install")
        elif purpose == 2:
            home_visit("support")
        elif purpose == 3:
            home_visit("scouting")
        else:
            print("Sorry, we did not understand your selection.")
            home_visit()
    
    visit_date = input(f"Please enter a date below when you are available for a \n \
    technician to come to your home and provide a {purpose} visit.")
    print(f"Wonderful! A technical will come visit you on {visit_date}. \n \
    Please be available between the hours of 1:00 am and 11:00 pm.")
    return visit_date

def live_rep(purpose):
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. \n \
        The wait time will be between two minutes and six hours. \n \
        We thank you for your patience.")
    elif purpose == "support":
        print("Please hold while we connect you with a live support representative. \n \
        The wait time will be between two minutes and six hours. \n \
        We thank you for your patience")
