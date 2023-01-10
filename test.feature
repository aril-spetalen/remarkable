# Note: At the beginning of each scenario the application will start in My files, with library structure:
#
# My files/
# |--- Test
# |--- Quick sheets
# |--- Some folder/ (empty)
# |--- Some other folder/ (empty)

Feature: Move files and folders

    This feature should test the different aspects of moving files and folders

    Scenario: Long press to access move action
        Given the 'Test' document is visible in My Files
        When the user long presses the 'Test' document
        And the user selects move from the drawer
        Then the user should be prompted with the move panel

    Scenario: Move single file to folder
        # Complete this scenario!

    Scenario: Move file and folder to folder
        # Complete this scenario!
