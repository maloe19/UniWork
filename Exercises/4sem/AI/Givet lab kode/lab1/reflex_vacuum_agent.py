A = 'A'
B = 'B'

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}

def REFLEX_VACUUM_AGENT(loc_st):  # Determine action  
    if loc_st[1] == 'Dirty': 
        return 'Suck'  
    if loc_st[0] == A: 
        return 'Right' 
    if loc_st[0] == B: 
        return 'Left'     

def Sensors():
    location = Environment['Current']
    return (location, Environment[location])

def Actuators(action):
    location = Environment['Current']
    if action == 'Suck': 
        Environment[location] = 'Clean'
    elif action == 'Right' and location == A: 
        Environment['Current'] = B
    elif action == 'Left' and location == B: 
        Environment['Curernt'] = A

def run (n): #run the agent through n  steps
    print('    Current          New')
    print('location    status  action  location    status')
    for i in range(1, n):
        (location, status) = Sensors() #Sense Enviroment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = REFLEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors() #Sense Enviroment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))

if __name__ == '__main__':
    run(10)