# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "narakoi/narakoi.github.io@master"
}

# 站点设置
site_name = "Escape Project"
site_logo = "http://cdn.jsdelivr.net/gh/narakoi/pic/like/koicat.jpg"
site_build_date = "2019-12-18T16:51+08:00"
author = "KOI"
email = "narakyzlily@gmail.com"
author_homepage = "https://koi.cat"
description = "Life kicks in right now."
key_words = ['Maverick', 'koi', 'Galileo', 'blog']
language = 'english'
external_links = [
    
    {
        "name": "老兄de博客",
        "url": "https://www.moec.top/",
        "brief": "杂七杂八的分享"
    }
    ,
    {
        "name": "KLDGodY's Blog",
        "url": "https://www.kldgody.top/",
        "brief": "一个蒟蒻的博客"
    },
    {
        "name": "AnYi's Blog",
        "url": "https://blog.sukiu.net",
        "brief": "可可爱爱的anyi"
    },
    {
        "name": "FRUCTOSE‘S BLOG",
        "url": "https://www.pibonds.com/",
        "brief": "果糖大佬" 
    },
    {
        "name": "INTEL-2333的导航",
        "url": "https://www.cattery.work/",
        "brief": "可爱的臭猫咪" 
    },
    {
        "name": "T1m0R's Blog",
        "url": "https://www.tsnet.net/",
        "brief": "提莫大佬" 
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archive",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/narakoi",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="shortcut icon" href="http://cdn.jsdelivr.net/gh/narakoi/pic/like/koicat.jpg" type="image/x-icon" />
'''

footer_addon = ''

body_addon = ''
