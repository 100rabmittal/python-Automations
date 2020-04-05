from __future__ import print_function

__author__ = 'sourabh.mittal50@google.com (Sourabh Mittal)'

import sys

from oauth2client import client
from googleapiclient import sample_tools
import requests
import json


class blog:

  def svc():
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        sys.argv, 'blogger', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/blogger')
    
    return service

  def getUsers(svc):  
    try:
        users = svc.users()

        # Retrieve this user's profile information
        thisuser = users.get(userId='self').execute()
        print('This user\'s display name is: %s' % thisuser['displayName'])

        blogs = svc.blogs()

        # Retrieve the list of Blogs this user has write privileges on
        thisusersblogs = blogs.listByUser(userId='self').execute()
        data = []
        for blog in thisusersblogs['items']:
          data.append('The blog named \'%s\' is at: %s' % (blog['name'], blog['url']))
        
        return data

    except client.AccessTokenRefreshError:
      return 'The credentials have been revoked or expired, please re-run the application to re-authorize'

  def getPosts(svc, data, idno):
    posts = svc.posts()
    body = {
        "kind": "blogger#post",
        "id": "32237367040152865"+str(idno),
        "title": "new try",
        "content":data
        }
    posts.insert(blogId='322373670401', body=body, isDraft=True).execute()
    return None