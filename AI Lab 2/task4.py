class Environment:
    def __init__(self):

        self.grid = ['Safe', 'Low Risk Vulnerable', 'Safe',
                    'Safe', 'Low Risk Vulnerable', 'High Risk Vulnerable',
                    'Safe', 'High Risk Vulnerable', 'Safe']
        self.Component = ['A', 'B', 'C',
                        'D', 'E','F', 
                        'G', 'H' , 'I']
    def get_percept(self, position):
        return self.grid[position]

    def print(self):
        for position in range(0,9):
            if self.grid[position] == 'Safe': 
                print (f"\u2714\uFE0F\t Component {self.Component[position]} is {self.grid[position]}\n" )
            else:
                print (f"\u274C\uFE0F\t Component {self.Component[position]} is {self.grid[position]}\n" )
    
    def patch_components(self, position):   
        self.grid[position] = 'Safe'
        print (f"\u2714\uFE0F\t Component {self.Component[position]} has been patched and marked safe\n") 

    

class UtilityBasedSecurityAgent:
    def __init__(self):
        self.position = 0 
        # self.patch = []
    def scan(self, percept,component):

        if percept == 'Low Risk Vulnerable':
            print (f"\u274C\uFE0F\t Component {component[self.position]} was found Vulnerable\n") 
            print("\u26A0\uFE0F\t Warning... System is in Low Risk Vulnerable State\n")
           
        elif percept == 'High Risk Vulnerable':
            print (f"\u274C\uFE0F\t Component {component[self.position]} was found Vulnerable\n")
            print("\U0001F6A8\t High Risk Vulnerability detected! Premium service required.\n")
        else:    
            print ("\u2714\uFE0F\t No threads found. System is Safe\n")

    def move(self):
        if self.position < 8:
            self.position += 1
            return self.position
    

def run_agent(agent, environment, steps):
    environment.print()
    for step in range(steps):
        percept = environment.get_percept(agent.position)
        action = agent.scan(percept, environment.Component)
        # print(f"Step {step + 1}: Position {agent.position} -> Percept - {percept}, Action - {action}")
        if percept == 'Low Risk Vulnerable':
            environment.patch_components(agent.position)
        agent.move()

agent = UtilityBasedSecurityAgent()
environment = Environment()

run_agent(agent, environment, 9)