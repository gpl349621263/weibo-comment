# weibo-comment
A little tool which can be used to create comment message without weibo API.

weilogin.py:
include a function:
weilogin('username','password'),it help you login Weibo and return a session.

weicomment.py:
inclue 2 functions:
get_blogid(uid),it will get the top blog of an weibo user who identified by uid.
weicomment(session, commuid, content),with the help of a logged session,it can comment the top blog with the contents of an weibo user(identified by commuid)

config.py:
include some headers
