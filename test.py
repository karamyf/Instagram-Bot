from instapy import InstaPy 

print("------------- Welcome To InstaBot --------------")
uname = input("Enter Your Username : ")
passw = input("Enter Your Password : ")

#headless_browser = True if you want to hide your browser
session = InstaPy(username = uname, password = passw ,headless_browser=True,want_check_browser=False)
session.login()

#You can set max and min followers here
session.set_relationship_bounds(enabled = True, max_followers = 290)


selected = input("Select : 1 2 3 4 5 : ")


def process(selected):

    session.set_comments(['your feed is aweeesome','loove it ❤❤','(͡° ͜ʖ ͡°)','In love with this❤❤❤❤❤'])

    def tags_process():

        list_tags = []

        print("Enter 3 Tags")
        list_tags[0] = input("Tag #1 : ")
        list_tags[1] = input("Tag #2 : ")
        list_tags[2] = input("Tag #3 : ")
        
        session.like_by_tags(list_tags, amount = 3)

    switcher = {

        1:session.set_do_follow(True, percentage=100),
        2:session.set_do_comment(True, percentage=40),
        3:tags_process(),
        4:session.set_dont_like(["nsfw"]),
        5:session.unfollow_users(amount=6, allFollowing=True, sleep_delay=60)
    }
    return switcher.get(selected, "nothing")

  
process(selected)
session.end()
