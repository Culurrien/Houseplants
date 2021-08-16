label silveryann:

    # This is temporary text to help us know where we are when playtesting.
    "SILVERYANN"

    scene bg sun room
    with dissolve

    show mc frown at left
    with dissolve

    M "Let's see... hmm, the leaves are curling up. That's unusual."

    # This text should stay on screen as the player selects the next options.
    "Want to check anything else?"

    menu:
        "Touch the Soil":
            jump touchthesoil
        "Look Under the Leaves":
            jump lookundertheleaves
        "All done here!":
            jump closerlook
