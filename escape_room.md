Escape Room
===========

@createrule <condition> = <action>[, <action>, ...]

Components
==========

- on/off button
- multi-position button
- push button
    CANNOT be a puzzle. Needs rules

- button to turn on a light that cannot be turned off (latch)
    @puzzle onoff, on_button = off_button
    @puzzle offon, off_button = on_button, light_on

- push button to turn on and off a light
    CANNOT be a puzzle. Needs rules

    @createrule
        was_pressed(button)
        = set_state(light, not get_state(light))

- lock with key
    @puzzle unlock, key, lock = key
      and a @lock on the exit based on key.
    Only one player can pass.

    CANNOT be a puzzle. Needs rules

- keypad (NOT a group of buttons because that would have no sequence of presses)
- lock with combination
  @createrule
    keycode_entered(lock)
    = delete @lock on the exit

- connectors (cables: different locations and order doesn't matter)
    CANNOT be a puzzle. Needs rules
    - cable: 2 or more ends

- connected objects (objects that work together disregarding their location)
    CANNOT be a puzzle. Needs rules

- balls as energy tokens when dropped
- parts collected overtime that progressively assembles a whole but
not all parts are available at the same time.
  = Parts appear overtime.
  = Parts are used in any order.
  MAY BE a Puzzle

- container (regular object with contents)

- timed task: task must be completed within a time frame.


Commands on Characters
======================

- move <object>

- takefrom <object with contents>[,<object within>[,...]]

- look under (behind, etc.) box
  @create/drop under box
  @lock under box = view:false()
  @createrule was_moved(box) = @lock under box = view:all()

- unlock (activate, enter)
    == unlock <lock>, <key|code>

- use (put)
    == use ball, hole in the wall
