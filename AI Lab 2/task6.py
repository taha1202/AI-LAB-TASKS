class Environment:
    def __init__(self):

        self.grid = ['Safe', 'Safe', 'Fire',
                    'Safe', 'Fire', 'Safe',
                    'Safe', 'Safe', 'Fire']
        self.rooms = ['A', 'B', 'C',
                        'D', 'E','F', 
                        'G', 'H' , 'J']
    def get_percept(self, position):
        return self.grid[position]

    def print(self):
        for position in range(0,9):
            if self.grid[position] == 'Safe': 
                print (f"\u2714\uFE0F\t Room {self.rooms[position]} is {self.grid[position]}\n" )
            else:
                print (f"\U0001F525\t Room {self.rooms[position]} is on {self.grid[position]}\n" )

        print("-------------------------------------------------------------------------------\n")        
    def Use_Fire_Extinguisher(self, position):   
        self.grid[position] = 'Safe'
        print (f"\u2714\uFE0F\t Room {self.rooms[position]} has Been set off from Fire\n") 

    

class Agent:
    def __init__(self):
        self.position = 0 
      
    def scan(self, percept,environment):

        if percept == 'Fire':
            print("\U0001F525\t Fire Detected! Using Fire Extinguisher \U0001F9EF\n")
            environment.Use_Fire_Extinguisher(agent.position)
            
        else:
            print ("\u2714\uFE0F\t No Fire Detected. Room is Safe\n")

    def move(self):
        if self.position < 8:
            self.position += 1
            return self.position
    

def run_agent(agent, environment, steps):
    
    for step in range(steps):
        print(f"\nStatus Of Room After {step+1} Steps:\n")
        environment.print()
        percept = environment.get_percept(agent.position)
        action = agent.scan(percept, environment)
        agent.move()

agent = Agent()
environment = Environment()

run_agent(agent, environment, 9)