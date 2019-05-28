#!/usr/bin/python3
class base():
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        elif len(name) >= 40:
            raise ValueError('name must be < 40 characters')
        elif name in users:
            raise ValueError(name, 'is already a user')
        else:
            self.__name = name



users = {}
class user(base):
    active = None
    def __init__(self, name, password):
        base.__init__(self, name)
        if self.name:
            users[name] = self
        self.votes = {}
        self.parents = {}
        self.permissions = {}
        self.password = password
    @property
    def active(self):
        return self.__active
    @property
    def password(self):
        return self.__password
    @active.setter
    def active(self, active):
        if user.active is not None and not isinstance(user.active, property):
            print('set user.active using login("name", "password")')
        else:
            __active = active
    @password.setter
    def password(self, password):
        if not isinstance(password, str) or password is None:
            print('set user.active using login("name", "password")')
        elif len(password) >= 40:
            print('set user.active using login("name", "password")')
        else:
            self.__password = password



teams = {}
class team(base):
    def __init__(self, name, parents=None, ):
        base.__init__(self, name)
        if self.name:
            teams[name] = self
        self.members = {}
        self.open_actions = {}
        self.quorum = 1/2
        self.size = 1



def logout():
    if user.active is None:
        print('Already logged out.')
    else:
        user.active = None



def login(name, password):
    if user.active is not None and not isinstance(user.active, property):
        raise TypeError(user.active.name, 'is already logged in.')
    elif not isinstance(name, str):
        raise TypeError('name must be a string')
    elif not name in users:
        raise ValueError(name, 'is not a user.')
    elif not isinstance(password, str):
        raise TypeError('password must be a string')
    elif len(password) >= 40:
        raise ValueError('password must be < 40 characters')
    elif password != users[name].password:
        raise ValueError('Incorrect password for', users[name].name)
    else:
        user.active = users[name]



class check():
    def valid_vote(action, teamname, member):
        """
        Checks the following:
        (handle exceptions in the function calling valid_vote() for those not relevant)
        1. that a user is logged in
        2. the team exists
        3. the team member to perform action upon exists
        4. the team member is in fact a member of the team
        5. the user hasn't already voted
        Then valid_vote() performs the following:
        1. if the action doesn't already exist in open_actions, create with a count of 1
        2. if the action DOES already exist in open_actions, add 1 to it's count
        3. create a record of the vote in the user object
        4. print the current status of the vote
        5. check if the vote passes
        """
        if user.active is None:
            print('Can not', action, 'Please log in.')
        elif not teamname in teams:
            print(teamname, 'does not exist.')
        elif not teamname in user.active.parents:
            print(user.active.name, 'is not a member of', teamname)
        elif not member in users:
            print(member, 'is not a user.')
        elif 'add' in action and member in teams[teamname].members:
            print(member, 'is already a member of', teamname)
        elif 'remove' in action and member not in teams[teamname].members:
            print(member, 'is not a member of', teamname)
        else:
            #check if active user has already voted
            if action in user.active.votes:
                print(user.active.name, 'has already voted to', action + '!')
                return False
            else:
                if not action in teams[teamname].open_actions:
                    #create action key in team open actions
                    teams[teamname].open_actions[action] = 1                    
                    print('Proposal created:')
                else:
                    #add 1 to action if already exists
                    teams[teamname].open_actions[action] += 1
                #add action to dictionary of actions by active user
                user.active.votes[action] = True
                print("    [" + action + "]" + ' + 1 vote.\n    Yays:', str(teams[teamname].open_actions[action]) + '/' + str(teams[teamname].size))
                if teams[teamname].quorum == 1:
                    if not teams[teamname].open_actions[action] >= int(teams[teamname].size * teams[teamname].quorum):
                        print('    There are not yet enough votes to', action)
                        return False
                elif not teams[teamname].open_actions[action] >= int((teams[teamname].size * teams[teamname].quorum) + 1):
                    print('    There are not yet enough votes to', action)
                    return False
                return True
        return False



class propose():
    #proposal object, methods are actions that users can vote to execute
    def create_new_team(new, *members):
        if user.active is None:
            print('Can not create new team. Please log in.')
        elif new in teams or new in user.active.parents:
            print(new, 'already exists. Please Choose another name.')
        else:
            print('Success!')
            print('The team', new, 'has been created.')
            teams[new] = team(new)
            teams[new].members[user.active.name] = user.active
            user.active.parents[new] = teams[new]
            propose.member('add', new, *members)
    def dissolve_team(name):
        vote = 'Dissolve ' + name + ' (PERMANENTLY!)'
        try:
            if check.valid_vote(vote, name, user.active.name):
                #the vote to dissolve passes
                #dissolve the team from users.parents and the pending votes from users.votes, then team itself
                for mem in teams[name].members:
                    del users[mem].parents[name]
                    if vote in users[mem].votes:
                        del users[mem].votes[vote]
                del teams[name]
                print(name, 'has been dissolved.')
        except NameError:
            pass      
    def member(action, name, *members):
        new_or_removed_members = 0
        if not action == 'add' and not action == 'remove':
            print('Usage: propose.member([add/remove], [to/from this team], [this/these member(s)]')
            return None
        for member in members:
            vote = action + ' ' + member + ' ' + name
            if check.valid_vote(vote, name, member):
                #the vote to add/remove member passes:
                for mem in teams[name].members:
                    if vote in users[mem].votes:
                        #delete vote in each user's votes dictionary
                        del users[mem].votes[vote]
                #delete vote from teams open votes
                del teams[name].open_actions[vote]
                if action == 'add':
                    #add the new member to the team :)
                    teams[name].members[member] = users[member]
                    #add the team to the new members parents dictionary
                    users[member].parents[name] = teams[name]
                    print('    ' + member, 'added to', name)
                    new_or_removed_members += 1
                elif action == 'remove':
                    
                    #remove the member from the team :(
                    del teams[name].members[member]
                    del users[member].parents[name]
                    print('    ' + member, 'removed from', name)
                    new_or_removed_members -= 1
        #increase/decrease the size of the team by number of newremoved members
        if new_or_removed_members != 0:
            teams[name].size += new_or_removed_members



def create_test_users():
    user('aaa', '')
    user('bbb', '')
    user('ccc', '')
    user('a', '')
    user('b', '')
    user('c', '')


create_test_users()
login('aaa', users['aaa'].password)
propose.create_new_team('teamname', 'bbb', 'ccc')
teams['teamname'].size
propose.create_new_team('new')
propose.member('add', 'new', 'bbb', 'ccc')
teams['new'].size
propose.member('add', 'new', 'a')
propose.member('badCommand', 'new', 'c')
propose.member('remove', 'new', 'bbb')
logout()
login('ccc', users['ccc'].password)
propose.member('remove', 'new', 'bbb', 'aaa')
propose.create_new_team('x', 'badName')

