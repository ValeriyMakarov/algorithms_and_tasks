input_data = [
    {
        'id': 1,
        'name': 'default',
        'sub_id': 20,
        'sub_name': 'default default'
    },
    {
        'id': 1,
        'name': 'default',
        'sub_id': 21,
        'sub_name': 'default default'
    },
    {
        'id': 1,
        'name': 'default',
        'sub_id': 22,
        'sub_name': 'default default'
    },
    {
        'id': 2,
        'name': 'default',
        'sub_id': 30,
        'sub_name': 'default default'
    },
    {
        'id': 2,
        'name': 'default',
        'sub_id': 31,
        'sub_name': 'default default'
    },
    {
        'id': 2,
        'name': 'default',
        'sub_id': 32,
        'sub_name': 'default default'
    }
]
output_data = [
    {
        'id': 1,
        'name': 'default',
        'sub_elem': [
            {
                'sub_id': 20,
                'sub_name': 'default default'
            },
            {
                'sub_id': 21,
                'sub_name': 'default default'
            },
            {
                'sub_id': 22,
                'sub_name': 'default default'
            }
        ]
    },
    {
        'id': 2,
        'name': 'default',
        'sub_elem': [
            {
                'sub_id': 30,
                'sub_name': 'default default'
            },
            {
                'sub_id': 31,
                'sub_name': 'default default'
            },
            {
                'sub_id': 32,
                'sub_name': 'default default'
            }
        ]
    }
]

print(input_data)
print(output_data)


def compare(a, b):
    if a != b:
        return False
    if isinstance(a, list):
        return compare_list(a, b)
    elif isinstance(a, dict):
        return compare_dict(a, b)
    return True


def compare_list(a: list, b: list):
    for a_item, b_item in zip(a, b):
        return compare(a_item, b_item)


def compare_dict(a: dict, b: dict):
    for a_item, b_item in zip(
            a.values(),
            sorted(b.values(), key=lambda x: list(a.values()).index(x))):
        return compare(a_item, b_item)


def get_id_index(id: int, lst: list[dict]):
    for i, value in enumerate(lst):
        if value['id'] == id:
            return i
    return None


def pack(lst: list) -> list:
    result = []
    for i in lst:
        index = get_id_index(i['id'], result)
        sub_elem_item = {
            'sub_id': i['sub_id'],
            'sub_name': i['sub_name']
        }
        if index is None:
            temp = {
                'id': i['id'],
                'name': i['name'],
                'sub_elem': [sub_elem_item]
            }
            result.append(temp)
        else:
            result[index]['sub_elem'].append(sub_elem_item)
    return result


compare_data = pack(input_data)
print(compare(output_data, compare_data), compare_data, sep='\n')
