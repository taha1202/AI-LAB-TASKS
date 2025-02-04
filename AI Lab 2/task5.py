class Environment:
    def __init__(self):

        self.layout = {
            "Corridors": ['C1','C2','C3','C4', 'C5'],
            "Patient_Room":['R1', 'R2','R3','R4','R5'],
            "Nurse_Stations": ['NS1','NS2','NS3'],
            "Medicine_Storage": ['MS1'] 
        }

        
        self.patient_schedule = {
            "R1":  {"time": "11:00", "medicine": ['Urso', 'Panadol'],"patientID": "P1","Condition":"Mild"}, 
            "R2" : {"time": "12:00", "medicine": ['Aspirin', 'Brufen'],"patientID": "P2","Condition":"Severe"},
            "R3" : {"time": "10:00", "medicine": ['Aspirin', 'Panadol', 'Brufen'],"patientID": "P3","Condition":"Severe"},
            "R4" : {"time": "1:00",  "medicine": ['Panadol','Brufen'],"patientID": "P4","Condition":"Severe"},
            "R5" : {"time": "11:00", "medicine": ['Aspirin', 'Panadol','Urso'],"patientID": "P5","Condition":"Mild"}
        }
        self.medicine_quantity = {
            "Panadol": 3,
            "Brufen": 5,
            "Aspirin": 10,
            "Urso": 4
        }
        self.Staff_Availaibility = {
            "NS1": True,
            "NS2": True,
            "NS3":True,
        }

    def get_schedule(self, room):
        return self.patient_schedule.get(room,{})
    
    def get_medicine(self, medicine):
        return self.medicine_quantity.get(medicine,0)

    def alert_staff(self):
        for key, value in self.Staff_Availaibility.items():
            if value:  
                print(f"\U0001F6A8\t Alerting staff from {key} for assistance!\n")
                self.Staff_Availaibility[key] = False
                return True
        return False
    
    def reduce_medicine(self, medicine):

        if self.medicine_quantity[medicine] > 0:
           self.medicine_quantity[medicine] -= 1
                     
class GoalBasedAgent:
    def __init__(self):
        self.current = "C1" 
        self.carrying_medicine = None

    def move(self,location): 
        print(f"\U0001F6F0\t Moving from {self.current} to {location}...\n")
        self.current = location
        

    def pick_medicine(self,medicine,environment):
        if self.current != "MS1":
            print("\u274C\uFE0F\t Robot is not in Medicine Storage Room. Moving To Room First...\n")
            self.move("MS1")

        self.carrying_medicine = False
        available = environment.get_medicine(medicine)
        if available == 0:
            print(f"\U0001F6AB\t {medicine} is Out of Stock.\n")
        else:
            self.carrying_medicine = True
            environment.reduce_medicine(medicine)
            print(f"\U0001F4E6\t Picked up {medicine}.\n")

    def deliver_medicine(self, room):
        if self.carrying_medicine:
            print(f"\U0001F691\t Delivering Medicines to {room}.\n")
        else:
            print("\u274C\t No medicine to deliver.\n")

    def scanID(self, room, patient_id,environment):
        patient_detail = environment.get_schedule(room)
        if patient_detail.get("patientID") == patient_id:
            print(f"\U0001F510\t Patient ID {patient_id} verified.\n")
            return True
        else:
            print(f"\U0001F510\t Patient ID {patient_id} does not match records.\n")
            return False
    
    def alert_staff(self,room,environment):
       
        patient_detail = environment.get_schedule(room)
        if patient_detail.get("Condition") == "Severe":
            available = environment.alert_staff()
            if available == False:
                print("\u26D4\t No staff available to assist.\n") 


def run_agent(agent, environment):
    
    for key,value in environment.patient_schedule.items():
        print(f"\n--- Scanning Patient In Room {key} ---\n")
        
        scan = agent.scanID(key,value["patientID"],environment)
        if scan :
            agent.move("MS1")
            for medicine in value["medicine"]: 
                agent.pick_medicine(medicine,environment)  
            agent.deliver_medicine(key)
            agent.alert_staff(key,environment)
            agent.move("C2")
        else:
            continue    

agent = GoalBasedAgent()
environment = Environment()

run_agent(agent, environment)