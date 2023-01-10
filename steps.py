# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the test.feature
# file is processed.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments to the step are passed via a mandatory
# 'context' parameter:
#
#   @When("the user enters the text")
#   def step(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern. The extracted values are passed as additional arguments, like e.g. num_names below:
#
#   @Then("the user gets |integer| different names")
#   def step(context, num_names):
#      <code here>

import names
import squish
import test
# 3LG-72VNA-22EZQ-PK6

from library_helper import find_visible_document

#### Given statements (preconditions) ####
@Given("the '|any|' document is visible in My Files")
def step(context, document_name):
    document = find_visible_document(document_name)
    test.verify(document != None)

@Given("the |any| folder is  visible in My Files")
def step(context, folder_name):
    folder = find_visible_folder(folder_name)
    test.verify(folder != None)

#### When statements (exercising behaviour) ####
@When("the user long presses the '|any|' document")
def step(context, document_name):
    squish.longMouseClick(find_visible_document(document_name))

@When("the user long presses the '|any|' folder")
def step(context, document_name):
    squish.longMouseClick(find_visible_folder(folder_name))

@When("the user short presses the '|any|' folder")
def step(context, folder_name):
    squish.MouseClick(find_visible_folder(folder_name))

@When("the user selects move from the drawer")
def step(context):
    squish.mouseClick(squish.waitForObject(names.drawer_move))

@When("the user selectes move_here from the panel")
def step(context):
    squish.mouseClick(squish.waitForObject(names.movepanel_move_here))



#### Then statements (verifying outcome) ####
@Then("the user should be prompted with the move panel")
def step(context):
    squish.waitForObject(names.movePanel_label)
    squish.waitForObject(names.movePanel_cancel_move)
    squish.waitForObject(names.movePanel_move)

Then 

@Then("the user should see the file |Test|' in the folder")
def step(context, document_name):
    find_visible_document(document_name):
    


