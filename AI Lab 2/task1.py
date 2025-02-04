class Environment:
    def __init__(self):

        self.grid = ['Safe', 'Vulnerable', 'Safe',
                    'Safe', 'Vulnerable', 'Vulnerable',
                    'Safe', 'Safe', 'Safe']
        self.Component = ['A', 'B', 'C',
                        'D', 'E','F', 
                        'G', 'H' , 'I']
    def get_percept(self, position):
        return self.grid[position]

    def patch_components(self, position):   
        self.grid[position] = 'Safe'
        print (f"\u2714\uFE0F\t Component {self.Component[position]} has been patched and marked safe\n") 

    

class SimpleReflexAgent:
    def __init__(self):
        self.position = 0 
        # self.patch = []
    def scan(self, percept,component):

        if percept == 'Vulnerable':
            print("\u26A0\uFE0F\t Warning... System is in Vulnerable Condition\n")
            # self.patch.append(component)
            print (f"\u274C\uFE0F\t Component {component[self.position]} was found Vulnerable\n") 
        else:
            print ("\u2714\uFE0F\t No threads found. System is Safe\n")

    def move(self):
        if self.position < 8:
            self.position += 1
            return self.position
    

def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept(agent.position)
        action = agent.scan(percept, environment.Component)
        # print(f"Step {step + 1}: Position {agent.position} -> Percept - {percept}, Action - {action}")
        if percept == 'Vulnerable':
            environment.patch_components(agent.position)
        
        agent.move()

agent = SimpleReflexAgent()
environment = Environment()

run_agent(agent, environment, 9)