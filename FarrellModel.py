class FarrellModel:
    def __init__(self, project_name, key_elements):
        self.project_name = project_name
        self.key_elements = key_elements

    def display_model(self):
        print("\nFarrell Model - Modified Waterfall Process")
        print(f"Project: {self.project_name}")
        print("=" * 50)
        print("Flowchart Representation:")
        print("START")
        for i, element in enumerate(self.key_elements, start=1):
            print(f"   |\n   v")
            print(f"[{element}]")
        print("   |\n   v")
        print("END")
        print("=" * 50)

    def get_formatted_output(self):
        return {
            "Project Name": self.project_name,
            "Key Elements": self.key_elements
        }

# User Input
project_name = input("Enter the project name: ")
num_elements = int(input("Enter the number of key elements in the diagram: "))
key_elements = [input(f"Enter key element {i+1}: ") for i in range(num_elements)]

# Create instance and display model
modified_model = FarrellModel(project_name, key_elements)
modified_model.display_model()

# Return well-formatted output
formatted_output = modified_model.get_formatted_output()
print("\nFormatted Output:")
print(formatted_output)
