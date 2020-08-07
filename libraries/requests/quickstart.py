# [Quickstart — Requests 2.24.0 documentation](https://requests.readthedocs.io/en/master/user/quickstart/)

import requests

# get GitHub’s public timeline (r means response)
r = requests.get('https://api.github.com/events')
# Now, we have a Response object called r. We can get all the information we need from this object.

print('r object:', r) # 200 means success, and you know what 404 means
print('type of r:', type(r))
print('status code:', r.status_code)

# 200 is equals to True and vice versa, you can do this:
if r:
    print('Success!')
else:
    print('An error has occurred.')

print()

##### Response Content

# read the content of the server's response
print(r.text)
print(">>> type(r.text):", type(r.text))
print(r.content)
print(">>> type(r.content):", type(r.content))

# to create an image from binary data returned by a request, you can use the following code
# from PIL import Image
# from io import BytesIO
#
# i = Image.open(BytesIO(r.content))