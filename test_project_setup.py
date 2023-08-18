import unittest
from os import environ
from scripts.project_setup import ProjectSetup

class ProjectSetupTest(unittest.TestCase):

    def setUp(self):
        environ["PROJECT_PATH"] = "test_file.txt"

    def test_get_plan(self):
        
        # Given:
        project_setup = ProjectSetup()
        project_setup.initialize_setup()
        
        # When:
        project_setup.get_plan()

        # Then:
        assert len(project_setup.module_to_clips) > 0, \
            "Module to clips not populated, its len: {}".format(len(project_setup.module_to_clips))

    def test_demo_clip_creation(self):
        """ Ensures that 'Screen Capture' and 'Development' steps are included in clip creation when demo is present. """

        # Given:
        project_setup = ProjectSetup()
        project_setup.initialize_setup()
        project_setup.module_names = ["1 - Sample Module"]
        project_setup.module_to_clips = {"1 - Sample Module":["Overview", "Demo: This is a Demo", "Conclusion"]}

        # When:
        project_setup.generate_card_set()

        contains_screen_capture = False
        contains_development_card = False

        for card in project_setup.cards:
            if card.subject.lower().__contains__("development"):
                contains_development_card = True

            if card.subject.lower().__contains__("screen capture"):
                contains_screen_capture = True

        assert contains_screen_capture, "Screen capture cards missing"
        assert contains_development_card, "Development cards missing"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()