Requests-Facebook
=================


Requests-Facebook is a Python library to help interface with `Facebook Graph API <https://graph.facebook.com>`_

Features
--------

* Authenticating Users
* Dyanmic Facebook methods
   - Read home feeds/user feeds
   - Post status updates
   - Delete items
   - Like items
   - And many more!!
* Photo Uploading


Installation
------------

Installing Requests-Facebook is simple: ::

    $ pip install requests-facebook


Usage
-----

Authorization URL
~~~~~~~~~~~~~~~~~

::

    f = FacebookAPI(client_id='*your app key*',
                    client_secret='*your app secret*',
                    redirect_uri='http://example.com/callback/')

or

::

    f = FacebookAPI('*your app key*', '*your app secret*', 'http://example.com/callback/')

::

    auth_url = f.get_auth_url(scope=['publish_stream', 'user_photos', 'user_status'])
    
    print 'Connect with Facebook via: %s' % auth_url

Once you click "Allow" be sure that there is a URL set up to handle getting finalized tokens and possibly adding them to your database to use their information at a later date.

Handling the Callback
~~~~~~~~~~~~~~~~~~~~~
::

    # Assume you are using the FacebookAPI object from the Authorization URL code

    # You'll need to obtain `code` from the url query string

    # In Django, you'd do something like
    # code = request.GET.get('code')

    access_token = f.get_access_token(code)
    
    final_access_token = access_token['oauth_token']
    
    # Save that token to the database for a later use?


Dynamic Facebook methods
~~~~~~~~~~~~~~~~~~~~~~~~
Say you have the url ``https://graph.facebook.com/me/friends``
To make a call via this library, you'd do GraphAPI.get('me/friends')

You just take everything in the url *AFTER* ``https://graph.facebook.com/``

Getting some User information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    # Get the final tokens from the database or wherever you have them stored

    graph = GraphAPI(access_token)

    # Print out your information
    try:
        print graph.get('me')
    except FacebookClientError:
        print 'Failed! :('

    # Print out my information
    print graph.get('mikehimself')


Getting your Home Feed
~~~~~~~~~~~~~~~~~~~~~~
::

    # Assume you are using the GraphAPI instance from the previous section
    home_feed = graph.get('me/home')
    print home_feed

Getting a Profile Feed
~~~~~~~~~~~~~~~~~~~~~~
::

    # Assume you are using the GraphAPI instance from the previous section
    your_feed = graph.get('me/feed')
    print your_feed

    # Getting my profile feed
    my_feed = graph.get('mikehimself/feed')
    print my_feed

Creating a Photo Album
~~~~~~~~~~~~~~~~~~~~~~
::

    # Assume you are using the GraphAPI instance from the previous section
    new_album = graph.post('me/albums', params={'name':'Test Album'})
    print new_album

Creating a post with a photo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    # Assume you are using the GraphAPI instance from the previous section
    # Assume you are using the album you just created in the previous section

    # new_album = new_album var from the previous section
    album_id = new_album['id']

    # Files is a list of dicts in the case that you can upload multiple files
    files = [{'source':'/path/to/file/image.png'}]
    new_photo = graph.post('%s/photos' % album_id, params={'message':'My photo caption!'}, files=files)

    print new_photo

Catching errors **(In case you didn't catch it in the first example)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    # Assume you are using the GraphAPI instance from the previous section

    try:
        graph.delete('me/feed')
    except FacebookClientError, e:
        print e.message
        print 'Something bad happened :('


TODO
----
Support for Facebook REST API