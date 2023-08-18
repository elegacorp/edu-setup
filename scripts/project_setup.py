import re
from os import environ
from sys import argv as command_line_arguments

class TrelloCard():
    def __init__(self, subject, description):
        self.subject = subject
        self.description = description

class ProjectSetup():
    def __init__(self, project_plan_path = None):
        print("Project setup initialized...")

        if project_plan_path is None:
            self.project_plan_path = environ["PROJECT_PATH"]
        else:
            self.project_plan_path = project_plan_path

        print("project_plan_path: " + self.project_plan_path)

        if not "PROJECT_PATH" in environ:
            print("ERROR: No project path configured in environment variable.")

    def initialize_setup(self):
        self.file_contents = []
        self.module_names = []
        self.cards = []
        self.module_to_clips = {}
    
    def execute_setup(self):
        self.initialize_setup()
        self.get_plan()
        self.generate_card_set()
        self.board_name = self.file_contents[0].replace("Board Name:", "")

        print("".join(["Board name: ", self.board_name]))
        print("".join(self.module_names))

        for card in self.cards:
            print(card.subject)

    def get_plan(self):
        """ Unpacks the file with the project plan to produce the module and clip names
        needed for creating Trello cards. """

        current_module = 0
        module_pattern = re.compile("[0-9][ \\-][A-z ]*")
        with open(self.project_plan_path, mode="r", encoding="utf8") as file:
            current_module_name = None
            for line in file:
                self.file_contents.append(line)

                if line == self.file_contents[0] or line == "\n" or line == "\r":
                    continue

                current_name = line.strip()
                
                module_match = module_pattern.match(line)
                if module_match != None:
                    current_module_name = current_name
                    self.module_names.append(current_module_name)
                    current_module += 1
                else:
                    if self.module_to_clips.__contains__(current_module_name):
                        self.module_to_clips[current_module_name].append(current_name)
                    else:
                        self.module_to_clips[current_module_name] = [current_name]


    def generate_card_set(self):
        
        default_set_per_clip = ["Script",
                                "Audio",
                                "Video Editing"]

        default_set_per_demo = ["Development",
                        "Screen Capture"]

        default_set_per_module = ["Slides",
                                    "Screen Capture"]
        
        module_number = 0
        for module_name in self.module_names:
            module_number += 1
            if module_name in self.module_to_clips:
                for default_module_clip_name in default_set_per_module:
                    module_clip_name = ''.join(["Module ", str(module_number), " - ", default_module_clip_name])
                    self.cards.append(TrelloCard(subject=module_clip_name, description=""))

                current_clip = 1
                for clip_name in self.module_to_clips[module_name]:
                    card_subject_construction = ["Module ",
                                                module_name,
                                                " ",
                                                "Clip ",
                                                str(current_clip),
                                                " : ",
                                                clip_name,
                                                " - "]

                    card_subject_prefix = ''.join(card_subject_construction)

                    if clip_name.lower().strip().__contains__("demo"):

                        for default_demo_subject in default_set_per_demo:
                            card_subject = "".join([card_subject_prefix, default_demo_subject])
                            self.cards.append(TrelloCard(subject=card_subject, description=""))
                    
                    for default in default_set_per_clip:
                        card_subject = "".join([card_subject_prefix, default])
                        self.cards.append(TrelloCard(subject=card_subject, description=""))

                    current_clip += 1

if __name__ == "__main__":
    project_plan_path = None

    for argument in command_line_arguments:
        if argument.__contains__(".txt"):
            project_plan_path = argument

    print(project_plan_path)
    project_setup = ProjectSetup(project_plan_path)
    project_setup.execute_setup()