class Environment:
    def __init__(self):
        self.servers = ['Underload','Balanced','Overload','Underload','Overload']

    def get_percept(self, position):
        return self.servers[position]

    def balance_task(self, position):   
        self.servers[position] = 'Underload'
        print ("""\u2714\uFE0F\t Task status changed to "Underload".\n""") 

    

class LoadBalancerAgent:
    def __init__(self):
        self.position = 0 
        
    def scan(self, percept,environment):

        if percept == 'Overload':
            print ("\u274C\uFE0F\t Task is Overloaded. Balancing it....\n") 
            environment.balance_task(self.position)
        else:
            print ("\u2714\uFE0F\t Task is already Balanced.\n")
            print (f"\t Status = {percept}\n")
    def move(self):
        if self.position < 4:
            self.position += 1
            return self.position
    

def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept(agent.position)
        action = agent.scan(percept, environment)
        # print(f"Step {step + 1}: Position {agent.position} -> Percept - {percept}, Action - {action}")
        agent.move()

agent = LoadBalancerAgent()
environment = Environment()

run_agent(agent, environment, 5)