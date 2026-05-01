# Arguments & Key Word Arguments
def example_method(mandatory_parameter, default_parameter="Default", *args, **kwargs):
    print(f""""
        mandatory_parameter = {mandatory_parameter} {type(mandatory_parameter)}
        default_parameter = {default_parameter} {type(default_parameter)}
        args = {args} {type(args)}
        kwargs = {kwargs} {type(kwargs)}
          """)

# Unpacking
example_list = [1, 2, 3, 4, 5]
# example_method(1, 2, 3, 4, 5)
# example_method(example_list[0], example_list[1], example_list[2], example_list[3], example_list[4])
# example_method(*example_list)

example_dict =  {'A':'0', 'B':'1', 'C':'2', 'D':'3', 'E':'4'}
example_method(*example_list, **example_dict)