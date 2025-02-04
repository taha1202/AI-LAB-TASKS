import random
class Environment:
    def __init__(self):
        self.tasks = ['Failed','Completed','Failed','Completed','Failed']

    def get_percept(self, position):
        return self.tasks[position]

    def Retry_Backup(self, position):   
        random_num = random.randint(0, 1)
        if random_num == 0:    
            self.tasks[position] = 'Failed'
            print ("\u274C\uFE0F\t Backup Failed Again\n") 
        else:
            self.tasks[position] = 'Completed'
            print ("\u2714\uFE0F\tBackup Successfull.\n")
        print (f"\t Status = {self.tasks[position]}\n")

    

class BackupManagementAgent:
    def __init__(self):
        self.position = 0 
        
    def scan(self, percept,environment):

        if percept == 'Failed':
            print ("\u274C\uFE0F\t Backup Failed. Trying Again....\n") 
            environment.Retry_Backup(self.position)
        else:
            print ("\u2714\uFE0F\tBackup Successfull.\n")
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

agent = BackupManagementAgent()
environment = Environment()

run_agent(agent, environment, 5)