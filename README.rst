Requests-Facebook
=================


``Requests-Facebook`` is a Python library to help interface with `Facebook Graph API <https://graph.facebook.com>`_ using the awesome ``requests`` library by `@kennethreitz <https://github.com/kennethreitz>`_

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

Once you click "Allow" be sure that there is a URL set up to handle getting finalized access_token and possibly adding it to your database to access their information at a later date.

Handling the Callback
~~~~~~~~~~~~~~~~~~~~~
::

    # Assume you are using the FacebookAPI object from the Authorization URL code

    # You'll need to obtain `code` from the url query string

    # In Django, you'd do something like
    # code = request.GET.get('code')

    access_token = f.get_access_token(code)
    
    final_access_token = access_token['access_token']
    
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

Posting a Photo
~~~~~~~~~~~~~~~
::

    # Assume you are using the GraphAPI instance from the previous section
    # Assume you are using the album you just created in the previous section

    # new_album = new_album var from the previous section
    album_id = new_album['id']

    photo = open('path/to/file/image.jpg', 'rb')

    # The file key that Facebook expects is 'source', so 'source' will be apart
    # of the params dict.

    # You can pass any object that has a read() function (like a StringIO object)
    # In case you wanted to resize it first or something!

    new_photo = graph.post('%s/photos' % album_id, params={'message':'My photo caption!', 'source': photo})

    print new_photo


Posting an Edited Photo *(This example resizes a photo)*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    # Assume you are using the GraphAPI instance from the previous section
    # Assume you are using the album you just created in the previous sections

    # Like I said in the previous section, you can pass any object that has a
    # read() method

    # Assume you are working with a JPEG

    from PIL import Image
    from StringIO import StringIO

    photo = Image.open('/path/to/file/image.jpg')

    basewidth = 320
    wpercent = (basewidth / float(photo.size[0]))
    height = int((float(photo.size[1]) * float(wpercent)))
    photo = photo.resize((basewidth, height), Image.ANTIALIAS)

    image_io = StringIO.StringIO()
    photo.save(image_io, format='JPEG')
    
    image_io.seek(0)

    try:
        new_photo = graph.post('%s/photos' % album_id, params={'message':'My photo caption!', 'source': photo})
    except FacebookClientError, e:
        # Maybe the file was invalid?
        print e.message


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
