import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

		if action == "1": 
			score += run_mission() 
		elif action == "2": 
			repair_system() 
		elif action == "3": 
			add_crew_member() 
		elif action == "4": 
			print(f"Simulation ended. Final score: {score}") break 
		else: 
			print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
	print("systems")
	for system, status in ship ['systems'].items():
		print(f"{system()}:{status}")
	print("resources")
	for resource, status in ship ['resources'].items():
		print(f"{resource()}:{status}")
	print("crew")
	for add_crew_member, status in ship ['crew'].items():
		print(f"{add_crew_member()}:{status}")

def get_user_action():
	print("Please choose an action")
	print("1: Run a mission")
	print("2: Repair a system")
	print("3: Add a crew mwmber")
	print("4:Quit simulation.")
	return input("Enter your choice")

def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	if mission_type=="Exploration":
		ship['resources']['energy']-= 
		result=random.choice([True, False])
		if result:
			print("Exploration successful! You got + points!!")
			return 
		else:
			print("Exploration failed. You got - energy.")
			return -
	elif mission_type== 'Diplomacy':
		ship['resources']['energy']-=
		result=random.choice([True, False])
		if result:
			print("Diplomacy successful! You got + points!!")
			return 
		else:
			print("Diplomacy failed. You got - points.")
			return-
	elif mission_type== 'Combat':
		ship['resources']['energy']-=
		result=random.choice([True, False])
		if result:
			print("Combat successful! You got + points!!")
			return 
		else:
			print("Combat failed. You got - points.")
			return-
	elif mission_type== 'Rescue':
		ship['resources']['energy']-=
		result=random.choice([True, False])
		if result:
			print("Rescue successful! You got + points!!")
			return 
		else:
			print("Rescue failed. You got - points.")
			return-
	elif mission_type== 'Scientific Research':
		ship['resources']['energy']-=
		result=random.choice([True, False])
		if result:
			print("Scientific Research successful! You got + points!!")
			return 
		else:
			print("Scientific Research failed. You got - points.")
			return-

def repair_system():
	print("Please choose a system to repair")
	for system in ship ['systems']:
		print(f"{system()}")
	y= input("Enter system name").lower()

	if y in ship ['systems']:
		if ship['systems'][y]<number:
			ship['resources']['energy']-=number
			ship['systems'][y] =number
			print(f"{systems()} repaired to full strengh.")
		else:
			print(f"{choice()} is already at full stregth.")
	else:
		 print("Invalid system name.")
 
def add_crew_member():
	name=input("Please enter the new crew mwmber's name.")
	role=input("Please enter the role(Command/Operations/Sciences)")

	if role in ["Command", "Operations", "Sciences"]:
		ship['crew'][name]=role
		print(f"Crew new member {name} added to {role}.")
	else:
		print("Invalid role. New crew member not added.")

def handle_random_event():
	event= random.choice(["none", "damage", "resource deplention", "crew injury"])

	if event=="damage":
		system=ramdom.choice(list(ship['systems'].keys()))
		ship['systems']['system']-= 
		print(f"Random event: {system()}system took damage!")
	elif event=="resource depletion":
		resource==ramdom.choice(list(ship['resources'].keys()))
		ship['resources']['resource']-=
		print(f"Random event: {resource()} depleted by 100!")
	elif event== "crew injury":
		add_crew_member==ramdom.choice(list(ship['crew'].keys()))
		print(f"Random event: {add_crew_member()} was  injured and is unavailable!")
		del ship['crew'][add_crew_member]
	else:
		print("Random event: All is calm.")
	

		


def use_resource(resource, amount): 
# TODO: Implement resource usage logic 

def replenish_resources():
	ship['resources']['energy']+=
	ship['resources']['torpedoes']+=
	print("")

main()
