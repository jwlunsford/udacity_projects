class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


class TreeSearch(object):
    '''Searches through a tree hierarchy of account groups and user names.  It relies on the Group class above'''
    def __init__(self):
        self.found = False              # initialize found to False

    def search_users(self, username, group):
        '''iterates through each group searching for a username'''
        # for each group search its users, then search its subgroups
        # search in top-level group users
        for user in group.get_users():
            # print(f'------ {user}') ---- used only for debugging the directory structure
            if user == username:
                self.found = True

        for group in group.get_groups():
            # print(f'- {group.name}')  ---- used only for debugging the directory structure
            self.search_users(username, group)

        return self.found


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    search = TreeSearch()
    return search.search_users(user, group)


parent = Group("parent")

# create child groups
child1 = Group("child1")
child2 = Group("child2")
sub_child1 = Group("child1_subchild1")
sub_child2 = Group("child1_subchild2")
sub_child3 = Group("child1_subchild3")
sub_child4 = Group('child2_subchild1')
sub_child5 = Group('child2_subchild2')

# add subchildren to child groups
child1.add_group(sub_child1)
child1.add_group(sub_child2)
child1.add_group(sub_child3)
child2.add_group(sub_child4)
child2.add_group(sub_child5)

# add children to parent
parent.add_group(child1)
parent.add_group(child2)

# add users
parent.add_user('parent_user')
child1.add_user('child1_user1')
child1.add_user('child1_user2')
child2.add_user('child2_user1')
child2.add_user('child2_user2')
sub_child1.add_user('subchild1_user1')
sub_child2.add_user('subchild2_user1')
sub_child3.add_user('subchild3_user1')
sub_child4.add_user('subchild4_user1')
sub_child5.add_user('subchild5_user1')



# TESTING CODE
user = 'parent_user'                        # USER AT THE HIGHEST LEVEL
was_found = is_user_in_group(user, parent)  # SHOULD RETURN TRUE
print(was_found)

user = ''                                   # INVALID USER
was_found = is_user_in_group(user, parent)  # SHOULD RETURN FALSE
print(was_found)

user = 'username_does_not_compute'          # INVALID USER
was_found = is_user_in_group(user, parent)  # SHOULD RETURN FALSE
print(was_found)

user = 'subchild5_user1'                    # USER AT DEEPEST LEVEL
was_found = is_user_in_group(user, parent)  # SHOULD RETURN TRUE
print(was_found)

