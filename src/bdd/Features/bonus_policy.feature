Feature: Bonus Policy
  The company follows a bonus policy, depending on the passenger type and on the mileage

  Scenario Outline: Usual passenger bonus policy
    Given we have a usual passenger with a mileage
    When the usual passenger travels <mileage1> and <mileage2> and <mileage3>
    Then the bonus points of the usual passenger should be <points>

    Examples:
      | mileage1 | mileage2 | mileage3| points |
      |     349 |     319 |    623 |     64 |
      |     312 |     356 |    135 |     40 |
      |     223 |     786 |    503 |     75 |
      |     482 |      98 |    591 |     58 |
      |     128 |     176 |    304 |     30 |

  Scenario Outline: VIP passenger bonus policy
    Given we have a VIP passenger with a mileage
    When the VIP passenger travels <mileage1> and <mileage2> and <mileage3>
    Then the bonus points of the VIP passenger should be <points>

    Examples:
      | mileage1 | mileage2 | mileage3| points  |
      |     349 |     319 |    623 |     129 |
      |     312 |     356 |    135 |      80 |
      |     223 |     786 |    503 |     151 |
      |     482 |      98 |    591 |     117 |
      |     128 |     176 |    304 |      60 |