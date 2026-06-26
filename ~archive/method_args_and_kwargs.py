# Arguments & Key Word Arguments
def example_method(mandatory_parameter, default_parameter="Default", *args, **kwargs):
    print(f""""
        mandatory_parameter = {mandatory_parameter} {type(mandatory_parameter)}
        default_parameter = {default_parameter} {type(default_parameter)}
        args = {args} {type(args)}
        kwargs = {kwargs} {type(kwargs)}
          """)
    
# example_method() # TypeError: example_method() missing 1 required positional argument: 'mandatory_parameter'
# example_method(mandatory_parameter=15) #  example_method(15)
# example_method(25, 45)
# example_method(25, "Some String")
# example_method(25, "String", "String 1", "String 2", "String 3")
# example_method(25, "String", "String 1", "String 2", "String 3", "String 4", "String 5")
# example_method(25, "String", "String 1", "String 2", "String 3", key1='A', key2='B', key3='C')
# example_method(25, "String", key1='A', key2='B', key3='C')
# example_method(key1='A', key2='B', key3='C', "String", 25) # This through an error
example_method(key1='A', key2='B', key3='C', default_parameter="String", mandatory_parameter=25)