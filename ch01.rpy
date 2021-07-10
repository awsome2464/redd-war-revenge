label chapter_1:
    show chapter_name "Chapter 1":
        xalign 0.5 yalign 0.4
    with dissolve
    pause 1
    show chapter_subtitle "2028":
        xalign 0.5 yalign 0.6
    with longdissolve
    pause 3
    hide chapter_name
    hide chapter_subtitle
    with longdissolve
    pause 2
label on_duty:
    python:
        renpy.music.set_volume(0.5, channel="sound")
        secondsPassed = 0
        hoursLeft1 = 168
        hoursLeft2 = "%02d" % 168
        minutesLeft1 = 0
        minutesLeft2 = "%02d" % 0
        secondsLeft1 = 0
        secondsLeft2 = "%02d" % 0
        startRrEnd = "begins"
    call timeleft
    $renpy.music.set_volume(1.0, channel="sound")
    play music patrol
    scene bg patrolcar
    show john at two2
    with longdissolve
    pause 1
    "I looked outside at the pedestrians walking by the squad car."
    "A lot of them didn't seem to pay it or me any mind."
    "Makes sense.{w=0.2}\nThis was a common police hangout spot, after all."
    play sound car_door
    pause 1.75
    show ben at two1 with easeinleft
    pause 0.1
    b "Alright, then. Here's your decaf."
    j "Thanks."
    "I took a sip from the steaming cup and gave out a sigh."
    j "You know, the worst thing about this job is that everything going right means you're just stuck here bored."
    b "{b}That's{/b} the worst thing about this job?"
    j "Oh, you know what I mean."
    b "Hey, I'm just messin' with ya, man; lighten up."
    b "And I feel ya.{w=0.2}\nBeen a pretty slow week, all things considered."
    b "Of course, with the War coming up pretty quickly..."
    "Ah, yes. \"The War\"."
    hide ben
    hide john
    with dissolve
    pause 0.1
    nvl show dissolve
    narrate """
    The REDD War has been a part of society for nearly 5 years now.

    While I've personally never experienced the War for myself, I {b}have{/b} experienced the REDD.

    The REDD are easily the most soulless and heartless creatures ever to appear on Earth.{w=0.2}
    And that's not just me being cruel; it's inbedded in their DNA.

    Of course, you get your \"good\" ones, but they're the exception, not the norm.

    {clear}

    They've essentially made our lives more hell than usual ever since they arrived to this planet.

    When we received calls during the first few years of their arrival, it seemed that a REDD was always the culprit.

    But to give credit where it's due, I suppose, things seem to have died down a bit as of recent.

    We get our occasional call here or there where a REDD is causing some sort of disturbance, but it's essentially the same as dealing with a human.

    Of course, we have yet to have a REDD War based here in Seattle.{w=0.2}\nI'm sure that would have an inpact on the REDD criminal activity.
    """
    nvl hide dissolve
    nvl clear
    show ben at two1
    show john at two2
    with dissolve
    pause 0.1
    b "What do you think are the odds that we'll get stuck being one of the War Zones this year?"
    j "Slim, if we're lucky."
    b "Hey, it's a big and popular city in America.\nBy default, our chances are not slim."
    j "Fair enough."
    j "Why do you ask, anyway?{w=0.2}\nGot plans for the holiday?"
    b "Boy, I know I got some color on me, but it ain't red, I assure you."
    j "Hey, I never implied what the plans were, my friend."
    "He gave a small grin and chuckle as he took a sip of his coffee."
    b "Nah, realistically, I'd just do what any sane person would do: get the hell out of town."
    j "What, not even attend a protest?"
    b "Ah, c'mon John; you know how REDD treat humans that publicly hate the War."
    j "And yet you've got the balls to walk around in that uniform."
    b "Hey, c'mon, man. I'm serious."
    j "And so am I."
    j "Look, let's stop worrying about the War unless it actually happens here."
    b "...sure."
    play loop phone_vibrate
    pause 2
    j "Ah, excuse me."
    hide ben with dissolve
    pause 0.1
    stop loop
    j "Hey, Hope."
    h "Hey, Dad!\nI'm not bothering you, am I?"
    j "If I ever answer \"Yes\" to that, you have my permission to hate me."
    h "Daaaaad!"
    j "Ahaha!{w=0.2}\nAnyway, did you need something?"

