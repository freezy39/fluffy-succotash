class Actor:
    def __init__(self, name, use_cases):
        self.name = name
        self.use_cases = use_cases

    def display_info(self):
        print(f"\n{self.name} Use Cases:")
        for use_case in self.use_cases:
            print(f"  - {use_case}")

# Define system actors and their use cases
actors = [
    Actor("Citizen", ["Report Pothole", "Track Report", "Submit Damage Claim"]),
    Actor("Public Works Administrator", ["Review Reports", "Assign Work Orders", "Monitor Progress"]),
    Actor("Repair Crew", ["Update Repair Status", "Log Materials Used", "Complete Work Order"])
]

# Display system breakdown
print("PATCH System Overview\n")
print("Actors Involved:")
for actor in actors:
    print(f"- {actor.name}")

for actor in actors:
    actor.display_info()
