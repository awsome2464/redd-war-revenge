label chapter_1:
    show chapter_name "Chapter 1:":
        xalign 0.5 yalign 0.4
    with dissolve
    pause 1
    show chapter_subtitle "War Prep":
        xalign 0.5 yalign 0.6
    with longdissolve
    pause 3
    hide chapter_name
    hide chapter_subtitle
    with longdissolve
    pause 2
label new_zones:
    python:
        hoursLeft = 24
        minutesLeft = 30
        secondsLeft = 2
    call timeleft
    play music news
    scene bg news
    show kramie at middle
    with longdissolve
    pause 1
    k "Good afternoon, Seattle.{w=0.2}\nI'm Kramie Damerson."
    k "It is now 3:30 pm on March 30th, which means we're half an hour away from learning the 5 War Zones that will host the 2031 REDD War."
    k "Until then, we will be speculating what cities Lord Reddington will select, discuss prior REDD Wars, and overall speculate what this War will bring."
    $renpy.music.set_volume(0.5, delay=0.5, channel="music")
    scene bg livingroom
    show john at middle
    with dissolve
    pause 0.1

