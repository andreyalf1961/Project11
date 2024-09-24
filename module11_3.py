
def introspection_info(obj):
    # тип объекта
    obj_type = type(obj).__name__

    # атрибуты объекта
    attributes = [attributes for attributes in dir(obj) if
                  not callable(getattr(obj, attributes))]

    # методы объекта
    methods = [methods for methods in dir(obj) if
               callable(getattr(obj, methods))]

    # Получаем модуль, к которому принадлежит объект
    module = introspection_info.__module__

    # Собираем информацию в словарь

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }
    return info


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('my_string')
print(string_info)


