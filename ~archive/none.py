''' C:\Users\Frank>python
    Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

    >>> None
    >>> type(None)
    <class 'NoneType'>

    >>> def email(subject, content, to, cc=None, bcc=None):
    ...     print(f"{subject}, {content}, {to}, {cc}, {bcc}")
    ...
    >>> email("subject", "great work", "frank@gmail.com")
    subject, great work, frank@gmail.com, None, None


    >>> var = "123"
    >>> if var is None : print ("do something");
    ...
    >>> var = None
    >>> if var is None : print ("do something");
    ...
    do something
    >>> '''