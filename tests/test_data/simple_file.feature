Feature: Serve coffee

Scenario: Buy last coffee{!scenario_1_file!}
  Given there are 1 coffees left in the machine
  And I have deposited 1$
  When I press the coffee button
  Then I should be served a coffee

Scenario: Buy first coffee {!scenario_2_file!}
  Given there are 2 coffees left in the machine
  And I have deposited 1$
  When I press the coffee button
  Then I should be served a coffee