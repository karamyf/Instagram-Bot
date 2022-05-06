from instapy import InstaPy 

print("------------- Welcome To InstaBot --------------")
uname = input("Enter Your Username : ")
passw = input("Enter Your Password : ")

#headless_browser = True if you want to hide your browser
session = InstaPy(username = uname, password = passw ,headless_browser=True,want_check_browser=False)
session.login()

#You can set max and min followers here
session.set_relationship_bounds(enabled = True, max_followers = 290)


selected = input(" 1 - Follow \n 2 - Comment \n 3 - Like by Tags \n 4 - Setup Accounts to avoid \n 5 - Unfollow \n 6 - Exit \n ")


def process(selected):


    # like by tags
    def tags_process():

        list_tags = []

        print("Enter 3 Tags")
        tag_first = input("Tag #1 : ")
        tag_second = input("Tag #2 : ")
        tag_third = input("Tag #3 : ")

        list_tags.append(tag_first)
        list_tags.append(tag_second)
        list_tags.append(tag_third)
        
        session.like_by_tags(list_tags, amount = 3)

    def comment_process():

        comment = []

        print("How many comment do you wanna add ? ")
        nbr_comment = int(input())

        for i in range(nbr_comment):
            print("Comment #",i+1)
            cmnt = input()
            comment.append(cmnt)

        session.set_do_comment(True, percentage=100)
        session.set_comments(comment)
        

    def dontlike_process():
        avoid_acc = []

        print("How many account ?")
        avoid_acc_nbr = int(input())

        for i in range(avoid_acc_nbr):
            avoid_acc_input = input()
            avoid_acc .append(avoid_acc_input)

        session.set_dont_like(avoid_acc)
    



    switcher = {

        1:session.set_do_follow(True, percentage=100),
        2:comment_process(),
        3:tags_process(),
        4:dontlike_process(),
        5:session.unfollow_users(amount=6, allFollowing=True, sleep_delay=60),
        6:quit()
    }
    return switcher.get(selected, "nothing")

process(selected)

session.end()
