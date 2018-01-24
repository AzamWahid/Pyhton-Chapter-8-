def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Muhammad', 'Azam',
                             location='karachi',
                            field='SoftDevelpment',
                             Education='Inter',
                             age=18,
                             Want='AI Developer')
print(user_profile)