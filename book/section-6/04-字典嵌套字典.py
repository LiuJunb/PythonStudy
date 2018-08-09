users = {
    'user1': {
        'name': 'jack1',
        'age': 1
    },
    'user2': {
        'name': 'jack2',
        'age': 2
    },
    'user3': {
        'name': 'jack3',
        'age': 3
    }
}

for key, value in users.items():
    print(key, value)
    for v in value.values():
        print(v)





