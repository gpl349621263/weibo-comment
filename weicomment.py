#coding=utf-8
import re
import requests
import json
import time
from config import headers_formobile,headers_forweb
from weilogin import weilogin

comment_msg = {
    'act':'post',
    'mid':'',
    'uid':'',
    'forward':'0',
    'isroot':'0',
    'content':'',
    'location':'page_100505_home',
    'module':'scommlist',
    'group_source':None,
    'tranandcomm':'1',
    'pdetail':'',
    '_t':'0'
}

def get_blogid(uid): 
        blog_url = 'https://m.weibo.cn/api/container/getIndex?containerid=230413' + uid \
          + '_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=230283' + uid
        page = requests.get(blog_url, headers=headers_formobile).json()
        blogs = page['data']['cards']
        for blog in blogs:
            try:
                mblog = blog['mblog']
                blogid = (mblog['id'])
                break
            except:
                pass
        return blogid

def weicomment(session, commuid, content):
    url = session.get('https://weibo.com').url
    uid = re.search('/u/(\d{10})', url).group(1)
    comment_msg['uid'] = uid
    comment_msg['mid'] = get_blogid(commuid)
    comment_msg['content'] = content
    comment_msg['pdetail'] = '100505' + commuid
    print '正在评论微博:'
    print comment_msg['mid']
    referurl = 'https://weibo.com/u/' + commuid + '?refer_flag=&is_all=1'
    session.headers.update({'Referer': referurl})
    try:
        resp = session.post("https://weibo.com/aj/v6/comment/add?ajwvr=6&__rnd=%d" % int(time.time() * 1000), data=comment_msg).json
        return True
    except:
        return 'Comment error 100001'
    
    

if __name__ == '__main__':
    if weicomment(weilogin('admin','123456'), '3696115947', 'I wanna see it again!') is True:
        print 'success'
    else:
        print 'fail'
