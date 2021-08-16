# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M = Character('MC')
define P = Character('Pegi')
define A = Character('Ann')

label start:
    # This is temporary text to help us know where we are when playtesting.
    "START"

    scene bg bedroom
    with fade

    # I couldn't figure out how to fit the character in the frame correctly,
    # but I'd like the MC to stand on the left, and other characters to stand
    # on the right :D

    # These display lines of dialogue.

    play music "audio/music/Pleasant Creek Loop - OpenGameArt Matthew Pablo.wav"

    show mc opensmile closedeyes at left
    with dissolve

    M "What a beautiful morning!"

    M "Looks like it's that time of day to water the plants..."


    scene bg sun room
    with dissolve

    "MC made her way to the favorite spot in her house: the Sun Room!"

    show mc opensmile at left

    M "Now then, where's my watering can?"

    show mc frown at left
    with dissolve

    # I'd like the character to "jump" right as she says "Oh no!!"
    M "..."
    M "Oh no!!"
    M "My plants don't look right... Let me get a closer look..."

    hide mc frown
    with dissolve

label closerlook:

    # I want this text to remain on screen while the user selects their option.

    # If possible, after a user selects one option then returns to this screen,
    # I'd like the first one they picked to be "greyed out" to indicate it's
    # been viewed (they can still click the viewed option)

    # This is temporary text to help us know where we are when playtesting.
    "CLOSER LOOK"

    hide mc frown
    with dissolve



    menu:
        "Which plant do you want to look at?"
        "Silvery Ann":
            jump silveryann
        "String of Hearts":
            jump stringofhearts
        "None... they're probably fine!":
            jump badend1
        # In the game, after selecting the first two options, the game should
        # automatically proceed to day2 and the below option should be removed.
        "Temp Option to proceed game":
            jump day2
label day2:
    # This is temporary text to help us know where we are when playtesting.
    "DAY 2"

    scene bg end
    with dissolve

    "The next day..."

    scene bg bedroom
    with dissolve

    show mc smile at left
    with dissolve

    M "What a beautiful morning! Time to check on the plants again..."

    scene bg sun room
    with dissolve

    M "Hello, my beautiful houseplants!"

    "The houseplants were happy. They lived happily everafter!"

# This ends the game.
return
