def my_function():
    print('Hello you.')
	
def my_function2(name):
    print(f"Hello {name}, is it me you're looking for?")

def my_function3(name):
    print(f"Hello {name.capitalize()}, is it me you're looking for?")

def my_function4(name='alex'):
    if isinstance(name,str):
        print(f"Hello {name.capitalize()}, is it me you're looking for?")
    else:
        print('Inputs must be strings')	