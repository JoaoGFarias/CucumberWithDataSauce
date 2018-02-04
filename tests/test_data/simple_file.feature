Feature: Serve coffee

Scenario: Buy last coffee
  Given there are 1 coffees left in the machine
  And I have deposited 1$
  When I press the coffee button
  Then I should be served a coffee

Scenario: Buy first coffee
  Given there are 2 coffees left in the machine
  And I have deposited 1$
  When I press the coffee button
  Then I should be served a coffee