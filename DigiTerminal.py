print("===================================================DigiTerminal v1.0.0==================================================")

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Sets Up the Chrome Webdriver to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=chrome_options)

#List Urls
login_url = "http://digibutter.nerr.biz/login"
all_posts_url = "http://digibutter.nerr.biz/posts"
the_dump_url = "http://digibutter.nerr.biz/posts/room/sidebar"

def login():
    #Go to /login Page
    driver.get(login_url)

    #Define Credentials
    email = input("\nEnter Email: ")
    password = input("\nEnter Password: ")

    #Perform Login
    print("\nLogging in...")
    email_textbox = driver.find_element_by_id("email")
    email_textbox.send_keys(email)

    password_textbox = driver.find_element_by_id("password")
    password_textbox.send_keys(password)

    login_button = driver.find_element_by_class_name("btn-primary")
    login_button.submit()
    print("\nDone.")

    username = driver.find_element_by_id("name")
    username = username.get_attribute("value")
    print("\nWelcome, %s." % username)

    driver.get(all_posts_url)

def all_posts():
    #Changes the current channel to All Posts
    driver.get(all_posts_url)

def the_dump():
    #Changes the current channel to The Dump
    driver.get(the_dump_url)

def list_topics():
    #Lists the topics and replies on the most recent page of the current channel
    print("\nListing recent topics and replies...")

    #Finds all show more buttons and clicks them
    show_replies_buttons = driver.find_elements_by_css_selector(".btn-showreplies")
    for show_replies_button in show_replies_buttons:
        if show_replies_button.text == "...":
            show_replies_button.click()
    
    #Lists the topics and replies on the most recent page of the current channel
    topics = driver.find_elements_by_class_name("postcontent")
    current_topics = topics[21:]
    for topic in current_topics:
        print("\n")
        print(topic.text)
    print("\n\nDone.")

def post():
    #Posts a new topic to the current channel. The default channel is All Posts.
    post_text = input("\nEnter the text of your post here: ")
    post_textbox = driver.find_element_by_id("textarea-message")
    post_textbox.send_keys(post_text)
    confirm = input("\nAre you sure you want to submit your post?: (Y/N): ")
    if confirm == "Y":
        print("\nPosting...")
        send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
        send_button.click()
        print("\nDone.")
        confirm_again = False
    elif confirm == "y":
        print("\nPosting...")
        send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
        send_button.click()
        print("\nDone.")
        confirm_again = False
    elif confirm == "Yes":
        print("\nPosting...")
        send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
        send_button.click()
        print("\nDone.")
        confirm_again = False
    elif confirm == "yes":
        print("\nPosting...")
        send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
        send_button.click()
        print("\nDone.")
        confirm_again = False
    elif confirm == "N":
        post_textbox.clear()
        print("\nPost was not sent because confirmation was declined.")
        confirm_again = False
    elif confirm == "n":
        post_textbox.clear()
        print("\nPost was not sent because confirmation was declined.")
        confirm_again = False
    elif confirm == "No":
        post_textbox.clear()
        print("\nPost was not sent because confirmation was declined.")
        confirm_again = False
    elif confirm == "no":
        post_textbox.clear()
        print("\nPost was not sent because confirmation was declined.")
        confirm_again = False
    else:
        print("\nSorry, that is not a valid input. Please try again:")
        confirm_again = True
    
    while confirm_again == True:
        confirm_redo = input("\nAre you sure you want to submit your post?: (Y/N): ")
        if confirm_redo == "Y":
            print("\nPosting...")
            send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
            send_button.click()
            print("\nDone.")
            confirm_again = False
        elif confirm_redo == "y":
            print("\nPosting...")
            send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
            send_button.click()
            print("\nDone.")
            confirm_again = False
        elif confirm_redo == "Yes":
            print("\nPosting...")
            send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
            send_button.click()
            print("\nDone.")
            confirm_again = False
        elif confirm_redo == "yes":
            print("\nPosting...")
            send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
            send_button.click()
            print("\nDone.")
            confirm_again = False
        elif confirm_redo == "N":
            post_textbox.clear()
            print("\nPost was not sent because confirmation was declined.")
            confirm_again = False
        elif confirm_redo == "n":
            post_textbox.clear()
            print("\nPost was not sent because confirmation was declined.")
            confirm_again = False
        elif confirm_redo == "No":
            post_textbox.clear()
            print("\nPost was not sent because confirmation was declined.")
            confirm_again = False
        elif confirm_redo == "no":
            post_textbox.clear()
            print("\nPost was not sent because confirmation was declined.")
            confirm_again = False
        else:
            print("\nSorry, that is not a valid input. Please try again:")
            confirm_again = True

def reply():
    #Posts a reply to a specific topic in the current channel
    topic_number = input("\nEnter a number from 1-50 which corresponds to the topic you'd like to reply to.\n\n(1 = The most recent topic, 50 = The 50th topic going up from the bottom of the page)\n\nNOTE, In most cases a page will only hold ~15 topics. 50 is the absolute highest the count can reach.\nIf you enter a number more than 15 which corresponds to a post that doesn't exist, you will get an exception and crash.\n\nPlease type carefully: ")
    if topic_number.isdigit():
        reply_buttons = driver.find_elements_by_xpath("//*[@title='OPEN']")
        reply_buttons[int(topic_number) * -1 - 1].click()
        reply_text = input("\nEnter the text of your reply here: ")
        reply_textbox = driver.find_element_by_id("textarea-message")
        reply_textbox.send_keys(reply_text)
        confirm = input("\nAre you sure you want to submit your reply?: (Y/N): ")
        if confirm == "Y":
            print("\nReplying...")
            send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
            send_button.click()
            print("\nDone.")
            confirm_again = False
            ask_topic_number_again = False
        elif confirm == "y":
            print("\nReplying...")
            send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
            send_button.click()
            print("\nDone.")
            confirm_again = False
            ask_topic_number_again = False
        elif confirm == "Yes":
            print("\nReplying...")
            send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
            send_button.click()
            print("\nDone.")
            confirm_again = False
            ask_topic_number_again = False
        elif confirm == "yes":
            print("\nReplying...")
            send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
            send_button.click()
            print("\nDone.")
            confirm_again = False
            ask_topic_number_again = False
        elif confirm == "N":
            reply_textbox.clear()
            print("\nReply was not sent because confirmation was declined.")
            confirm_again = False
            ask_topic_number_again = False
        elif confirm == "n":
            reply_textbox.clear()
            print("\nReply was not sent because confirmation was declined.")
            confirm_again = False
            ask_topic_number_again = False
        elif confirm == "No":
            reply_textbox.clear()
            print("\nReply was not sent because confirmation was declined.")
            confirm_again = False
            ask_topic_number_again = False
        elif confirm == "no":
            reply_textbox.clear()
            print("\nReply was not sent because confirmation was declined.")
            confirm_again = False
            ask_topic_number_again = False
        else:
            print("\nSorry, that is not a valid input. Please try again:")
            confirm_again = True
            ask_topic_number_again = False
        
        while confirm_again == True:
            confirm_redo = input("\nAre you sure you want to submit your reply?: (Y/N): ")
            if confirm_redo == "Y":
                print("\nReplying...")
                send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                send_button.click()
                print("\nDone.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm_redo == "y":
                print("\nReplying...")
                send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                send_button.click()
                print("\nDone.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm_redo == "Yes":
                print("\nReplying...")
                send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                send_button.click()
                print("\nDone.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm_redo == "yes":
                print("\nReplying...")
                send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                send_button.click()
                print("\nDone.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm_redo == "N":
                reply_textbox.clear()
                print("\nReply was not sent because confirmation was declined.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm_redo == "n":
                reply_textbox.clear()
                print("\nReply was not sent because confirmation was declined.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm_redo == "No":
                reply_textbox.clear()
                print("\nReply was not sent because confirmation was declined.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm_redo == "no":
                reply_textbox.clear()
                print("\nReply was not sent because confirmation was declined.")
                confirm_again = False
                ask_topic_number_again = False
            else:
                print("\nSorry, that is not a valid input. Please try again:")
                confirm_again = True
                ask_topic_number_again = False
    else:
        print("\nSorry, that is not a number. Please try again")
        ask_topic_number_again = True

    while ask_topic_number_again == True:
        topic_number = input("\nEnter a number from 1-50 which corresponds to the topic you'd like to reply to.\n\n(1 = The most recent topic, 50 = The 50th topic going up from the bottom of the page)\n\nNOTE, In most cases a page will only hold ~15 topics. 50 is the absolute highest the count can reach.\nIf you enter a number less than 50 for a post that doesn't exist, you will get an exception and crash.\n\nPlease type carefully: ")
        if topic_number.isdigit():
            reply_buttons = driver.find_elements_by_xpath("//*[@title='OPEN']")
            reply_buttons[int(topic_number) * -1 - 1].click()
            reply_text = input("\nEnter the text of your reply here: ")
            reply_textbox = driver.find_element_by_id("textarea-message")
            reply_textbox.send_keys(reply_text)
            confirm = input("\nAre you sure you want to submit your reply?: (Y/N): ")
            if confirm == "Y":
                print("\nReplying...")
                send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                send_button.click()
                print("\nDone.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm == "y":
                print("\nReplying...")
                send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                send_button.click()
                print("\nDone.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm == "Yes":
                print("\nReplying...")
                send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                send_button.click()
                print("\nDone.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm == "yes":
                print("\nReplying...")
                send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                send_button.click()
                print("\nDone.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm == "N":
                reply_textbox.clear()
                print("\nReply was not sent because confirmation was declined.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm == "n":
                reply_textbox.clear()
                print("\nReply was not sent because confirmation was declined.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm == "No":
                reply_textbox.clear()
                print("\nReply was not sent because confirmation was declined.")
                confirm_again = False
                ask_topic_number_again = False
            elif confirm == "no":
                reply_textbox.clear()
                print("\nReply was not sent because confirmation was declined.")
                confirm_again = False
                ask_topic_number_again = False
            else:
                print("\nSorry, that is not a valid input. Please try again:")
                confirm_again = True
            
            while confirm_again == True:
                confirm_redo = input("\nAre you sure you want to submit your reply?: (Y/N): ")
                if confirm_redo == "Y":
                    print("\nReplying...")
                    send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                    send_button.click()
                    print("\nDone.")
                    confirm_again = False
                    ask_topic_number_again = False
                elif confirm_redo == "y":
                    print("\nReplying...")
                    send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                    send_button.click()
                    print("\nDone.")
                    confirm_again = False
                    ask_topic_number_again = False
                elif confirm_redo == "Yes":
                    print("\nReplying...")
                    send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                    send_button.click()
                    print("\nDone.")
                    confirm_again = False
                    ask_topic_number_again = False
                elif confirm_redo == "yes":
                    print("\nReplying...")
                    send_button = driver.find_element_by_xpath("//*[@id='mdl-content']/div/div/main/div/div/div/div[2]/div/div[3]/button")
                    send_button.click()
                    print("\nDone.")
                    confirm_again = False
                    ask_topic_number_again = False
                elif confirm_redo == "N":
                    reply_textbox.clear()
                    print("\nReply was not sent because confirmation was declined.")
                    confirm_again = False
                    ask_topic_number_again = False
                elif confirm_redo == "n":
                    reply_textbox.clear()
                    print("\nReply was not sent because confirmation was declined.")
                    confirm_again = False
                    ask_topic_number_again = False
                elif confirm_redo == "No":
                    reply_textbox.clear()
                    print("\nReply was not sent because confirmation was declined.")
                    confirm_again = False
                    ask_topic_number_again = False
                elif confirm_redo == "no":
                    reply_textbox.clear()
                    print("\nReply was not sent because confirmation was declined.")
                    confirm_again = False
                    ask_topic_number_again = False
                else:
                    print("\nSorry, that is not a valid input. Please try again:")
                    confirm_again = True
        else:
            print("\nSorry, that is not a number. Please try again")
            ask_topic_number_again = True

    driver.back()

#The main program code which asks for and handles user inputs
choice_1 = input("\nWhat would you like to do?\n  login             Logs user into Digibutter.nerr.biz\n  all_posts         Changes the current channel to All Posts\n  the_dump          Changes the current channel to The Dump\n  list_topics       Lists the topics and replies on the most recent page of the current channel\n  post              Posts a new topic to the current channel. The default channel is All Posts.\n  reply             Posts a reply to a specific topic in the current channel\n  exit              Exits the program\n\nYou can currently use commands:\n  login\n  exit\n\n")
if choice_1 == "login":
    login()
    choice_2 = input("\nWhat would you like to do now?\n  login             Logs user into Digibutter.nerr.biz\n  all_posts         Changes the current channel to All Posts\n  the_dump          Changes the current channel to The Dump\n  list_topics       Lists the topics and replies on the most recent page of the current channel\n  post              Posts a new topic to the current channel. The default channel is All Posts.\n  reply             Posts a reply to a specific topic in the current channel\n  exit              Exits the program\n\nYou can currently use commands:\n  all_posts\n  the_dump\n  list_topics\n  post\n  reply\n  exit\n\n")
    if choice_2 == "login":
        print("\nYou are already logged into Digibutter. Please select another option:")
        ask_choice_2_again = True
    elif choice_2 == "all_posts":
        print("\nChanging channel to All Posts...")
        all_posts()
        print("\nDone.")
        ask_choice_2_again = True
    elif choice_2 == "the_dump":
        print("\nChanging channel to The Dump...")
        the_dump()
        print("\nDone.")
        ask_choice_2_again = True
    elif choice_2 == "list_topics":
        list_topics()
        ask_choice_2_again = True
    elif choice_2 == "post":
        post()
        ask_choice_2_again = True
    elif choice_2 == "reply":
        reply()
        ask_choice_2_again = True
    elif choice_2 == "exit":
        print("\nExiting...")
        driver.quit()
        ask_choice_2_again = False
    else:
        print("\nSorry, that is not a valid command. Please try again:")
        ask_choice_2_again = True
    ask_choice_1_again = False
elif choice_1 == "all_posts":
    print("\nYou need to login first to use that command. Please select another option:")
    ask_choice_1_again = True
elif choice_1 == "the_dump":
    print("\nYou need to login first to use that command. Please select another option:")
    ask_choice_1_again = True
elif choice_1 == "list_topics":
    print("\nYou need to login first to use that command. Please select another option:")
    ask_choice_1_again = True
elif choice_1 == "post":
    print("\nYou need to login first to use that command. Please select another option:")
    ask_choice_1_again = True
elif choice_1 == "reply":
    print("\nYou need to login first to use that command. Please select another option.")
    ask_choice_1_again = True
elif choice_1 == "exit":
    print("\nExiting...")
    driver.quit()
    ask_choice_1_again = False
else:
    print("\nSorry, that is not a valid command. Please try again:")
    ask_choice_1_again = True

while ask_choice_1_again == True:
    choice_1_redo = input("\nWhat would you like to do?\n  login             Logs user into Digibutter.nerr.biz\n  all_posts         Changes the current channel to All Posts\n  the_dump          Changes the current channel to The Dump\n  list_topics       Lists the topics and replies on the most recent page of the current channel\n  post              Posts a new topic to the current channel. The default channel is All Posts.\n  reply             Posts a reply to a specific topic in the current channel\n  exit              Exits the program\n\nYou can currently use commands:\n  login\n  exit\n\n")
    if choice_1_redo == "login":
        login()
        choice_2 = input("\nWhat would you like to do now?\n  login             Logs user into Digibutter.nerr.biz\n  all_posts         Changes the current channel to All Posts\n  the_dump          Changes the current channel to The Dump\n  list_topics       Lists the topics and replies on the most recent page of the current channel\n  post              Posts a new topic to the current channel. The default channel is All Posts.\n  reply             Posts a reply to a specific topic in the current channel\n  exit              Exits the program\n\nYou can currently use commands:\n  all_posts\n  the_dump\n  list_topics\n  post\n  reply\n  exit\n\n")
        if choice_2 == "login":
            print("\nYou are already logged into Digibutter. Please select another option:")
            ask_choice_2_again = True
        elif choice_2 == "all_posts":
            print("\nChanging channel to All Posts...")
            all_posts()
            print("\nDone.")
            ask_choice_2_again = True
        elif choice_2 == "the_dump":
            print("\nChanging channel to The Dump...")
            the_dump()
            print("\nDone.")
            ask_choice_2_again = True
        elif choice_2 == "list_topics":
            list_topics()
            ask_choice_2_again = True
        elif choice_2 == "post":
            post()
            ask_choice_2_again = True
        elif choice_2 == "reply":
            reply()
            ask_choice_2_again = True
        elif choice_2 == "exit":
            print("\nExiting...")
            driver.quit()
            ask_choice_2_again = False
        else:
            print("\nSorry, that is not a valid command. Please try again:")
            ask_choice_2_again = True
        ask_choice_1_again = False
    elif choice_1_redo == "all_posts":
        print("\nYou need to login first to use that command. Please select another option:")
        ask_choice_1_again = True
    elif choice_1_redo == "the_dump":
        print("\nYou need to login first to use that command. Please select another option:")
        ask_choice_1_again = True
    elif choice_1_redo == "list_topics":
        print("\nYou need to login first to use that command. Please select another option:")
        ask_choice_1_again = True
    elif choice_1_redo == "post":
        print("\nYou need to login first to use that command. Please select another option.")
        ask_choice_1_again = True
    elif choice_1_redo == "reply":
        print("\nYou need to login first to use that command. Please select another option.")
        ask_choice_1_again = True
    elif choice_1_redo == "exit":
        print("\nExiting...")
        driver.quit()
        ask_choice_1_again = False
    else:
        print("\nSorry, that is not a valid command. Please try again:")
        ask_choice_1_again = True

while ask_choice_2_again == True:
    choice_2_redo = input("\nWhat would you like to do now?\n  login             Logs user into Digibutter.nerr.biz\n  all_posts         Changes the current channel to All Posts\n  the_dump          Changes the current channel to The Dump\n  list_topics       Lists the topics and replies on the most recent page of the current channel\n  post              Posts a new topic to the current channel. The default channel is All Posts.\n  reply             Posts a reply to a specific topic in the current channel\n  exit              Exits the program\n\nYou can currently use commands:\n  all_posts\n  the_dump\n  list_topics\n  post\n  reply\n  exit\n\n")
    if choice_2_redo == "login":
        print("\nYou are already logged into Digibutter. Please select another option:")
        ask_choice_2_again = True
    elif choice_2_redo == "all_posts":
        print("\nChanging channel to All Posts...")
        all_posts()
        print("\nDone.")
        ask_choice_2_again = True
    elif choice_2_redo == "the_dump":
        print("\nChanging channel to The Dump...")
        the_dump()
        print("\nDone.")
        ask_choice_2_again = True
    elif choice_2_redo == "list_topics":
        list_topics()
        ask_choice_2_again = True
    elif choice_2_redo == "post":
        post()
        ask_choice_2_again = True
    elif choice_2_redo == "reply":
        reply()
        ask_choice_2_again = True
    elif choice_2_redo == "exit":
        print("\nExiting...")
        driver.quit()
        ask_choice_2_again = False
    else:
        print("\nSorry, that is not a valid command. Please try again:")
        ask_choice_2_again = True