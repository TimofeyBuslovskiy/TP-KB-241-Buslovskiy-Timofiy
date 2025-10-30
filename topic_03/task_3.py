def operation_with_dict () :
    my_dict = {
        'name': 'Timofiy',
        'age' : '19',
        'city' : 'Chernihiv'

    }

    print('default dict: ', my_dict)
    my_dict.update({'city' : "Kiyv", 'job' : 'BackEnd developer'})
    print('Updated dict: ', my_dict)
    del my_dict['job']
    print('Dict after deleted element', my_dict)
    my_dict_copy = my_dict.copy()
    print('copy dict: ', my_dict_copy)
    my_dict.clear()
    print('Cleared dict: ', my_dict)   
    print('Keys from my dict_copy: ', my_dict_copy.keys())    
    print('Values from my dict_copy: ', my_dict_copy.values())
    print('Items from my dict_copy: ', my_dict_copy.items())




operation_with_dict()