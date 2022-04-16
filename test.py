from instapy import InstaPy
from instapy import smart_run

# login
insta_username = 'username'
insta_password = 'password'

# headless_browser=True = running in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)




with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=510,
                                    min_followers=31,
                                    min_following=29)

    # activities

    """ Joining Engagement Pods...
    """
    photo_comments = ['your feed is aaawesome !',
        'in looove with your photos ! @{}',
        'ur photos are awesoome  :thumbsup:',
       'OMG ❤:open_mouth:',
        'My goodness, how impressive!',
        'OMG how impressive!!!',
        'Keep up the good work',
        'Great doing!!',
        'ur feed is just a piece of art❤' ]
    session.set_do_follow(True, percentage=100)
    session.set_do_comment(enabled = True, percentage = 50)
    session.set_comments(photo_comments, media = 'Photo')
    #session.follow_user_followers(['casabookstore', 'book__taif','zedenya'], amount=10, randomize=False, sleep_delay=130)
    session.like_by_tags(["readers","bookslover","أصدقاء_الكتب","كتاب","moroccanreaders","morocco"], amount = 10)
   #session.interact_user_followers(['casabookstore', 'book__taif'], amount=10, randomize=True)
    #unfollow users who don't follow you back
    #session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
    
    #interact with user likers
    #session.interact_user_likers(usernames=["zedenya", "casabookstore"],
                             #posts_grab_amount=10,
                             #interact_likers_per_post=5,
                             #randomize=True)