import json

class InternProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.intern_data = self.load_data()

    def load_data(self):
        with open(self.input_file, "r") as file:
            data = json.load(file)
        return data

    def process_interns(self):
        result_dict = {}
        for intern in self.intern_data['interns']:
            if intern["middle_name"] is None:
                email =(f"{intern['first_name']}.{intern['last_name']}@pvpsit.com")
                name = (f"{ intern['first_name']}{ intern['last_name']}")
            else:
                email = (f"{intern['first_name']}-{intern['middle_name']}.{intern['last_name']}@pvpsit.com")
                name = (f"{intern['first_name']}{intern['middle_name']}{intern['last_name']}")
            
            result_dict[email] = {"id": intern["id"], "fullname": name}

        return result_dict

    def save_output(self, output_data):
        with open(self.output_file, "w") as file:
            json.dump(output_data, file, indent=3)


input_filename = "c&o_interns.json"
output_filename = "c&o_output.json"

intern_processor = InternProcessor(input_filename, output_filename)
processed_data = intern_processor.process_interns()
intern_processor.save_output(processed_data)
