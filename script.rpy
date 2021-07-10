﻿#######################
## REDD War: Revenge ##
#######################

##############
# Characters #
##############

define a = Character("Amy", image="amy", what_prefix='"', what_suffix='"')
define b = Character("Ben", image="ben", what_prefix='"', what_suffix='"')
define c = Character("[cName]", image="croy", color="#d00000", what_prefix='"', what_suffix='"')
define d = Character("[dName]", image="derima", color="#d00000", what_prefix='"', what_suffix='"')
define f = Character("Flang", image="flang", color="#d00000", what_prefix='"', what_suffix='"')
define h = Character("Hope", what_italic=True, what_prefix='"', what_suffix='"')
define j = Character("John", image="john", what_prefix='"', what_suffix='"')
define l = Character("Leslie", image="leslie", what_prefix='"', what_suffix='"')
define m = Character("Majiku", image="majiku", color="#d00000", what_prefix='"', what_suffix='"')
define p = Character("[pName]", image="pilli", color="#d00000", what_prefix='"', what_suffix='"')
define s = Character("[sName]", image="slack", color="#d00000", what_prefix='"', what_suffix='"')

define narrate = nvl_narrator

##########
# Images #
##########

# Characters #

image amy = Placeholder("girl")
image ben = Placeholder("boy")
image croy = Placeholder("boy")
image derima = Placeholder("girl")
image flang = Placeholder("boy")
image john = Placeholder("boy")
image leslie = Placeholder("girl")
image majiku = Placeholder("boy")
image pilli = Placeholder("girl")
image slack = Placeholder("boy")

# Backgrounds #

image bg fade = "#000000"
image bg news = "#000fff"
image bg livingroom = "#5f5f5f"
image bg patrolcar = "#2c2c2c"

# Text #

image chapter_name = ParameterizedText(style="chaptername")
image chapter_subtitle = ParameterizedText(style="countdown2")

#########
# Audio #
#########

# Custom Channels #

init python:
    renpy.music.register_channel("loop", mixer="sfx", loop=True)
    renpy.music.register_channel("sound2", mixer="sfx", loop=None)

# Music #

define audio.news = "audio/music/Network.mp3"
define audio.serious = "audio/music/Hong_Kong_Midnight.mp3"
define audio.three_sixty_five_days_intro = "<to 4.822 loop 4.22>audio/music/365 Days.ogg"
define audio.three_sixty_five_days_main = "<from 4.822>audio/music/365 Days.ogg"
define audio.patrol = "audio/music/Safe-Cracking_Looping.mp3"

# Sound Effects #

define audio.car_door = "audio/se/car_door.ogg"
define audio.clock_beep = "audio/se/clock_beep.ogg"
define audio.phone_vibrate = "audio/se/phone_vibrate.ogg"
define audio.siren = "audio/se/siren.ogg"

##############
# Transforms #
##############

# Character Transforms #

transform middle:
    xalign 0.5 yalign 0.5
transform two1:
    xalign 0.25 yalign 0.5
transform two2:
    xalign 0.75 yalign 0.5
transform left:
    xalign 0.2 yalign 0.5
transform right:
    xalign 0.8 yalign 0.5

# Intro Transforms #

transform introzoom:
    zoom 0.85
    linear 5.3 zoom 1.1
transform presents:
    xalign 0.5 yalign 0.75
    alpha 0.0
    pause 4.5
    linear 1.0 alpha 1.0
transform revenge:
    xalign 0.5 yalign 0.5

##########
# Styles #
##########

style countdown:
    color "#b00000"
    font "fonts/EHSMB.TTF"
    size 150
style countdown2:
    color "#b00000"
    font "fonts/EHSMB.TTF"
    size 50
style countdown3:
    color "#b00000"
    font "fonts/EHSMB.TTF"
    size 35
style intro:
    color "#b00000"
    font "fonts/EHSMB.TTF"
    size 125
    outlines [(absolute(5), "#000000", absolute(0), absolute(0))]
style revenge:
    color "#6d6d6d"
    font "fonts/BadSuabiaSwing-Regular.otf"
    size 300
    outlines [(absolute(5), "#464646", absolute(0), absolute(0))]
style chaptername:
    color "#6d6d6d"
    font "fonts/BadSuabiaSwing-Regular.otf"
    size 150
    outlines [(absolute(5), "#464646", absolute(0), absolute(0))]

##################
# Custom Screens #
##################

screen countdownclock():
    vbox:
        xalign 0.5 yalign 0.5
        text "[hoursLeft2]:[minutesLeft2]:[secondsLeft2]" style "countdown" xalign 0.5
        hbox:
            xalign 0.5
            spacing 140
            text "HOURS" style "countdown3"
            text "MINUTES" style "countdown3"
            text "SECONDS" style "countdown3"
        null height 50
        text "until the REDD War [startOrEnd]" style "countdown2" xalign 0.5

screen intro:
    if goodTales:
        text "PRESENTS" style "countdown2" at presents xalign 0.5
    if revengeReveal:
        text "REVENGE" style "revenge" at revenge xalign 0.5
        add "intro_shading.png" xalign 0.5
    hbox at introzoom:
        xalign 0.5 yalign 0.5
        text intro1 style "intro" xalign 0.5 
        text intro2 style "intro" xalign 0.5 
        text intro3 style "intro" xalign 0.5
        text intro4 style "intro" xalign 0.5
        text intro5 style "intro" xalign 0.5
        text intro6 style "intro" xalign 0.5
        text intro7 style "intro" xalign 0.5
        text intro8 style "intro" xalign 0.5
        if goodTales:
            text intro9 style "intro" xalign 0.5
            text intro10 style "intro" xalign 0.5

screen countdowntest():
    vbox:
        xalign 0.0 yalign 0.0
        text "[hoursLeft1] [minutesLeft1] [secondsLeft1]"
        text "[secondsPassed]"

###############
# Transitions #
###############

define news_wipe = ImageDissolve("newswipe.png", 0.5)
define longdissolve = Dissolve(2.0)

#############
# Variables #
#############

define alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
default introList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
default introChange = None

default intro1 = renpy.random.choice(alphabet)
default intro2 = renpy.random.choice(alphabet)
default intro3 = renpy.random.choice(alphabet)
default intro4 = renpy.random.choice(alphabet)
default intro5 = renpy.random.choice(alphabet)
default intro6 = renpy.random.choice(alphabet)
default intro7 = renpy.random.choice(alphabet)
default intro8 = renpy.random.choice(alphabet)
default intro9 = renpy.random.choice(alphabet)
default intro10 = renpy.random.choice(alphabet)

default introShuffle = False
default goodTales = True
default revengeReveal =  False

default hoursLeft1 = 0
default hoursLeft2 = "%02d" % 0
default minutesLeft1 = 0
default minutesLeft2 = "%02d" % 0
default secondsLeft1 = 5
default secondsLeft2 = "%02d" % 5

default secondsPassed = 0.0
default part1 = 0.0
default part2 = 0.0

default startOrEnd = "ends"

default cName = "Geek"
default dName = "Muscles"
default pName = "Slut"
default sName = "Doctor"

######################################################################################################################################################

label timeleft:
    play sound clock_beep
    show screen countdownclock
    #show screen countdowntest
    while secondsPassed <= 5:
        python:
            renpy.pause(1)
            secondsLeft1 -= 1
            secondsLeft2 = "%02d" % secondsLeft1
            if int(secondsLeft2) == 0 and int(minutesLeft2) == 0 and int(hoursLeft2) == 0:
                renpy.music.set_volume(0.25, channel="sound")
                renpy.play("audio/se/clock_beep.ogg", channel="sound2")
                renpy.play("audio/se/siren.ogg", channel="sound")
                renpy.pause(2)
                renpy.hide_screen("countdownclock")
                renpy.with_statement(longdissolve)
                renpy.pause(3)
                renpy.return_statement()
            elif secondsLeft1 == -1:
                if minutesLeft1 > 0 or hoursLeft1 > 0:
                    secondsLeft1 = 59
                    secondsLeft2 = "%02d" % 59
                if minutesLeft1 > 0:
                    minutesLeft2 = "%02d" % (minutesLeft1 - 1)
                elif hoursLeft1 > 0:
                    minutesLeft2 = "%02d" % 59
                    hoursLeft2 = "%02d" % (hoursLeft1 - 1)
            renpy.play("audio/se/clock_beep.ogg", channel="sound")
            secondsPassed += 1
    hide screen countdownclock
    pause 2
    $secondsPassed = 0
    return

label start:
    scene bg fade
    with dissolve
    pause 2
    call timeleft from _call_timeleft
    stop sound
    play music network
    scene bg news with news_wipe
    pause 0.5
    show text "Good Morning, Seattle!\nwith Amy Harrison" at truecenter with dissolve
    pause 2
    hide text with dissolve
    show amy at middle with dissolve
    window show dissolve
    pause 0.1
    a "Good morning, Seattle! The clock has struck 4 AM Pacific Standard Time, which means the 2030 REDD War has officially come to an end!"
    a "As emergency services spread throughout the 5 War Zones to help hurt humans and stop REDD who are still committing crime, statisticians across the globe are reviewing footage and data to calculate the deadliness of this REDD War."
    a "Is it the deadliest?"
    a "Is it on par with last year?"
    a "Or is this the least-violent REDD War to date?"
    a "We'll be sure to let you know the results as soon as we have them."
    a "Let's now talk to our in-house REDD expert Majiku Vanlason for War highlights."
    show amy at two2
    show majiku at two1
    with easeinleft
    pause 0.1
    m "Thanks, Amy."
    a "So tell me, Majiku, what are some of the more notable things that occurred within the past 12 hours?"
    m "Well, of course the biggest REDD War story of the night has to be the bloodshed at the Mr. Sprinkles live show in Atlanta."
    m "While the body count is still being officially tallied up, we're estimating well over 100 casualties based on the broadcast alone."
    m "Of course, with the broadcast being cut several hours ago, it's hard to tell for sure how many more have occurred."
    a "100 casualties within 12 hours? Doesn't sound very dangerous."
    m "Given the systematic nature of the situation, it makes sense why the count would be so low."
    m "But with the mainstream attention the show received, a lot of other REDD War activities have gone relatively unnoticed and are only now being observed via security footage."
    m "Take, for instance, this clip of these small neighborhood homes being destroyed with residents still inside."
    a "Oh my! Is that a bulldozer??"
    m "It is, indeed. Truly a mystery where the REDD got that from."
    m "We also have this clip of 3 REDD chasing a young woman through the streets before another REDD comes out of nowhere and runs her over!"
    a "Ouch! Talk about unlucky for all parties involved!"
    m "Haha~! Well put, Amy!"
    m "We'll be sure to compile a full list of REDD War Highlights and post them to the {i}Good Morning, Seattle{/i} website within the next few hours."
    l "John, what are you doing up?"
    window hide dissolve
    $renpy.music.set_volume(0.5, delay=2.0, channel="music")
    scene bg livingroom with longdissolve
    pause 0.5
    show leslie at middle with dissolve
    window show dissolve
    pause 0.1
    "I turned and saw my wife walk into the room while rubbing her eye."
    show leslie:
        ease 0.5 two1
    show john at two2 with dissolve
    pause 0.1
    j "Couldn't sleep."
    "After she quit rubbing her eye, she took a look at the TV."
    extend " Before sighing and sitting next to me."
    l "John, I told you that watching the REDD War will do nothing but hurt you."
    j "I know, but..."
    "I crossed my arms as I thought about how to word it."
    j "...I just..."
    "Leslie placed her hand on mine."
    l "I know you want to help these people, but you can't."
    l "Even if you were actually in a War Zone, being a hero is suicide."
    j "..."
    stop music fadeout(3.0)
    "She then leaned her head on my shoulder and we sat in silence."
    l "..."
    j "..."
    $renpy.music.set_volume(1.0, channel="music")
    play music hong_kong_midnight fadein(1.0)
    j "That's not it, Leslie."
    j "At least, not completely."
    "I could feel her head move a bit in curiosity."
    j "This fucking night..."
    j "Every year..."
    j "Thousands of innocent people killed..."
    j "And yet the scummiest of humans get off unharmed."
    j "All because they're rich enough to pay off REDD for protection or escape the War Zone borders or even be lucky enough to not be located in a city where the War is being held."
    "Leslie rubbed my hand as I vented."
    j "I was hoping to see at least one, just one, REDD kill some notable gang leader or corrupted businessman or some shit."
    j "But no."
    j "If these damn aliens are gonna go killing people, at least go after the ones that deserve it, not these poor saps who were caught in the wrong place at the wrong time."
    "I then sighed and leaned my head back."
    l "..."
    "My wife remained silent as she continued to comfort me."
    j "Heh."
    j "I guess it's kinda stupid to think those fuckers care about our desires, right?"
    l "Well..."
    "She sat up and turned towards me."
    l "It's never stupid to want the world to be a better place, John."
    l "And you're right; if the REDD are going to do what they're gonna do, they could at least try to do it to help us."
    l "But..."
    j "There's just no reasoning with them."
    "I finished."
    "She gave a small, awkward smile and looked down."
    "I then turned back to the TV."
    "More discussions on the REDD War's events."
    "Apparently a big story that happened in Australia was a small group of REDD hanging a farmer upside-down while removing his limbs with a chainsaw."
    "All while his children watched."
    l "Look, you've still got a few hours left until you need to get ready for work."
    l "Let's just head back to bed and get some rest, hm?"
    j "..."
    "I guess my eyelids were a bit heavy now that she mentioned it."
    "Plus, clearing my mind wouldn't exactly be a bad thing right now."
    j "Alright. I'll be there in a minute."
    "She smiled and gave me a quick kiss on the cheek before getting off the couch and back towards the bedroom."
    stop music fadeout(3.0)
    hide leslie with easeoutleft
    pause 0.5
    show john:
        ease 1.0 middle
    pause 1.5
    j "..."
    "I took one final look at the TV."
    scene bg news
    show amy at middle
    with dissolve
    pause 0.1
    a "The REDD throughout the world who couldn't attend the War surely did seem excited at what they saw."
    a "Although there are the occasional REDD who felt like everything seemed a bit disappointing compared to previous REDD Wars."
    a "These Tweets from Lord Reddington seem to sum up their feelings perfectly:"
    hide amy with dissolve
    pause 0.1
    a "{i}While the 2030 REDD War has some notable events, I feel as if some areas are lacking. Low body counts, less painful deaths, etc.{/i}"
    a "{i}Do not misunderstand: for the most part, I am pleased with the end product. But like with all things, they can be improved upon. Which is why I am working with the Base's greatest minds to create said improvement.{/i}"
    play music three_sixty_five_days_intro fadein(10.0)
    a "{i}By this time next year, we may have the solution to creating the greatest REDD War in history. Until then, I wish safe travels to the REDD returning home and the best of luck to all of humanity.{w} You will need it.{/i}"
    window hide dissolve
    queue music three_sixty_five_days_main noloop

label startintro:
    if renpy.music.get_playing("music") != audio.three_sixty_five_days_main:
        jump startintro

    scene bg fade
    $introShuffle = True
    $secondsPassed = 0.0
    show screen intro
    while introShuffle and goodTales:
        python:
            if 1 in introList:
                intro1 = renpy.random.choice(alphabet)
            if 2 in introList:
                intro2 = renpy.random.choice(alphabet)
            if 3 in introList:
                intro3 = renpy.random.choice(alphabet)
            if 4 in introList:
                intro4 = renpy.random.choice(alphabet)
            if 5 in introList:
                intro5 = renpy.random.choice(alphabet)
            if 6 in introList:
                intro6 = renpy.random.choice(alphabet)
            if 7 in introList:
                intro7 = renpy.random.choice(alphabet)
            if 8 in introList:
                intro8 = renpy.random.choice(alphabet)
            if 9 in introList:
                intro9 = renpy.random.choice(alphabet)
            if 10 in introList:
                intro10 = renpy.random.choice(alphabet)
            secondsPassed += 0.1
            renpy.pause(0.1)
            if secondsPassed > 2:
                if len(introList) > 0:
                    introChange = renpy.random.choice(introList)
                    if introChange == 1:
                        intro1 = "G"
                    elif introChange == 2:
                        intro2 = "O"
                    elif introChange == 3:
                        intro3 = "O"
                    elif introChange == 4:
                        intro4 = "D"
                    elif introChange == 5:
                        intro5 = " "
                    elif introChange == 6:
                        intro6 = "T"
                    elif introChange == 7:
                        intro7 = "A"
                    elif introChange == 8:
                        intro8= "L"
                    elif introChange == 9:
                        intro9= "E"
                    elif introChange == 10:
                        intro10 = "S"
                    introList.remove(introChange)
            if secondsPassed >= 3.5:
                introShuffle = False
    pause 1.5
    hide screen intro
    pause 0.25
    python:
        goodTales = False
        introShuffle = True
        introList = [1, 2, 3, 4, 5, 6, 7, 8]
        secondsPassed = 0.0
    show screen intro
    while introShuffle:
        python:
            if 1 in introList:
                intro1 = renpy.random.choice(alphabet)
            if 2 in introList:
                intro2 = renpy.random.choice(alphabet)
            if 3 in introList:
                intro3 = renpy.random.choice(alphabet)
            if 4 in introList:
                intro4 = renpy.random.choice(alphabet)
            if 5 in introList:
                intro5 = renpy.random.choice(alphabet)
            if 6 in introList:
                intro6 = renpy.random.choice(alphabet)
            if 7 in introList:
                intro7 = renpy.random.choice(alphabet)
            if 8 in introList:
                intro8 = renpy.random.choice(alphabet)
            secondsPassed += 0.1
            renpy.pause(0.1)
            if secondsPassed > 2:
                if len(introList) > 0:
                    introChange = renpy.random.choice(introList)
                    if introChange == 1:
                        intro1 = "R"
                    elif introChange == 2:
                        intro2 = "E"
                    elif introChange == 3:
                        intro3 = "D"
                    elif introChange == 4:
                        intro4 = "D"
                    elif introChange == 5:
                        intro5 = " "
                    elif introChange == 6:
                        intro6 = "W"
                    elif introChange == 7:
                        intro7 = "A"
                    elif introChange == 8:
                        intro8 = "R"
                    introList.remove(introChange)
            if secondsPassed >= 3.5:
                introShuffle = False
    # pause 0.25
    $revengeReveal = True
    pause 4.25
    hide screen intro
    pause 3
    "I wasn't always this way."
    "But 2 years ago, my life changed forever."
    pause 2

    jump chapter_1