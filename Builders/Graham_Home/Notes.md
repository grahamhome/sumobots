# Asyncio firmware design

Basic idea is to convert the steps from the current sequential "fight" loop into a set of async tasks.

Will most likely need a more granular state enum e.g. "moving forwards", "backing away from edge". "backing away from opponent", etc so that various tasks will know how to respond to events based on robot state.
* If this was implemented with a stack we would have a history of robot actions. Would this be useful?

## Task/event list
* Check for opponent (read TOF sensors)
  * Detected right
  * Detected left
  * Detected ahead (both R & L)
* Check for arena edge (read IR sensors)
  * Detected right
  * Detected left
  * Detected ahead/behind (both R & L, ahead/behind is direction-dependent)
    * Moving forwards or rotating = detected ahead
    * Moving backwards = detected behind

## Action/state list
* Turn to face opponent (turn radius inv. proportional to opponent distance)
* Charge opponent
* Turn around (e.g. when edge detected with both sensors)
* Turn away (e.g. when edge detected with one sensor)
* Back away from opponent (when stalemate detected)
    * Want to improve this maneuver e.g. back up while turning 45 degrees
    * Maybe back up while turning 90 degrees then rotate back 45 degrees?
    * Randomize delay before stalemate is detected and randomize rotation direction to prevent immediately re-entering stalemate
* Turn to find opponent
  * Randomize direction

## State diagram
![Sumobot state diagram.png](Sumobot%20state%20diagram.png)
