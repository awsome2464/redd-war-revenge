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
label three_years_later:
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
    k "Until then, we will be speculating what cities Lord Reddington will select, discuss prior REDD Wars, and estimate what this War will bring to the table overall."
    $renpy.music.set_volume(0.5, delay=0.5, channel="music")
    scene bg livingroom
    show john at two1
    with dissolve
    pause 0.1
    "It's hard to believe it's already that time of the year again."
    "Another year of senseless and legal bloodshed from extraterrestrial creatures."
    l "Hey, you."
    show leslie at two2 with dissolve
    pause 0.5
    l "Any word on what to expect this year?"
    j "Not yet."
    "She sighed and grabbed my hand."
    l "I really hate this time of year..."
    j "I know, Les.{w=0.2}\nI hate it, too."
    j "The stress of whether or not we'll be caught in a War Zone, the pain of knowing thousands of innocent people are going to die..."
    j "But...{w=0.2}\nWe'll be fine."
    l "You don't know that."
    j "But I believe it."
    "A small smile grew on her, though the look of fear still coated her face."
    "We both sat in silence and listened to the TV."
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    scene bg news
    show kramie at middle
    with dissolve
    pause 0.1
    k "While the REDD War has been a part of Earth culture for 8 years now, some people, mainly humans, are still doing their best to prevent it from happening in the future."
    k "The most obvious and mainstream of these humans, of course, is Senator Peter Carson, who announced his run for president last month."
    k "While Senator Carson has always been vocal of his anti-War stance, his campaign promise to end the REDD War in the United States should he be elected has gotten the entire world talking."
    k "Is such a feat even possible?"
    k "Here to discuss this topic is our in-house REDD War expert, Majiku Vanlason."
    show kramie at two1 with easeinright
    show majiku at two2 with dissolve
    pause 0.1
    k "Thank you for coming on, Majiku."
    m "Thank you for having me, Kramie."
    k "Now, Majiku, many are asking themselves how likely it would be for a non-American REDD War to ever happen, no matter who is president.{w=0.2} What are your thoughts on this?"
    "Majiku gave a small chuckle before replying:"
    m "Well, to put it bluntly, Kramie, I don't believe that will ever happen."
    m "The reason America is always chosen for a War is because of how large of a country it is in both a geographic and population sense."
    m "With just one city having {i}millions{/i} of potential targets, it's an obvious candidate for a REDD War, creating enough for REDD to work with for a full 12 hours."
    m "It just doesn't make any sense for Lord Reddington to exclude such a concept and risk making REDD unhappy."
    k "That makes sense."
    k "However, Senator Carson claims that here are alternate methods.{w=0.2}\nHave a listen to this statement he made during a press conference last week."
    pause 1
    $renpy.music.set_pause(True, channel="music")
    scene cg carson with news_wipe
    play loop cameras
    pause 0.5
    car "The REDD War is doing nothing but causing irreversible harm to this country and its people."
    car "While I can't do anything about the War as a whole, I {b}can{/b} do something about it in my own country."
    car "When I'm president, I'll do anything I can to convince Congress and, more importantly, Lord Reddington to take the War somewhere else.{w=0.5} There are hundreds of other countries to pick from; leave ours out!"
    play sound applause
    pause 4
    stop loop fadeout(1.0)
    stop sound fadeout(1.0)
    scene bg news
    show kramie at two1
    show majiku at two2
    with news_wipe
    pause 0.5
    $renpy.music.set_pause(False, channel="music")
    k "{i}\"Convincing Congress and Lord Reddington\"{/i}.{w=0.2}\nYour thoughts, Majiku?"
    m "How?{w=0.2} How is he going to convince them?{w=0.5}\nCarson has yet to answer this simple question when asked."
    m "Until that question is answered in a convincing way, he has nothing but empty promises."
    m "If he truly wants to be president, especially as an anti-War one, he'll need more than that."
    $renpy.music.set_volume(0.5, channel="music", delay=0.5)
    scene bg livingroom
    show john at two1
    show leslie at two2
    with dissolve
    pause 0.5
    hide john with easeoutleft
    pause 0.1
    "I got off the couch and walked over towards the kitchen."
    l "You okay, hon?"
    j "Yeah, I just..."
    j "I just need to stop thinking about the War for now."
    l "..."
    play sound tv
    stop music
    $renpy.music.set_volume(1.0, channel="music")
    "She shut the TV off and walked over to me."
    scene bg kitchen
    show john at two2 zorder 1
    with dissolve
    pause 0.5
    show leslie at two1 zorder 2 with easeinleft
    pause 0.1
    "When she was next to me, she started rubbing my back with a grimace."
    l "Come on.{w=0.2}\nWhat's {b}really{/b} bothering you?"
    "She knows me well."
    play music serious
    j "Even if the REDD War magically goes away overnight, that ain't gonna stop shit."
    j "We have 364 days of no REDD Wars, yet those...{w=0.2} {b}things{/b} still hurt and kill people!"
    j "But sure.{w=0.2}\nMaking it a full 365 will fix {b}everything{/b}!"
    "I took a deep breath, but I could sense how shaky it was."
    "My throat began to tighten as I found my eyes moving towards the photo hanging on the wall between the living room and kitchen."
    "A photo of the two of us surrounding Hope after she had won the finals in her freshman-year softball tournament."
    show leslie:
        ease 1.0 xalign 0.6
    "Knowing exactly where I was looking, Leslie approached me and hugged me tightly."
    "I tightly hugged back as the tears flowed out."
    j "I just miss her so fucking much."
    l "I know, John.{w=0.2} I miss her, too."
    "It was clear in her voice that she was crying, as well."
    j "If I had just told her to--"
    l "Stop, John.{w=0.2}\nIt was not your fault. Nothing you did or didn't do was responsible for her death."
    "I knew she was right, but that doesn't make it easy to stop having those thoughts."
    "What if I had told her to forget the soda and leave?{w=0.2}\nWhat if I had arrived to the store sooner?"
    "I know asking \"What if...?\" won't change the past, but..."
    "...even after 3 years, I just can't stop thinking about what could've been done to save my little girl.{w} Or at the very least, serve justice to her killer."
    j "It doesn't matter if there's no REDD War in this country.{w=0.2}\nAs long as those damn aliens are {b}anywhere{/b}, nobody is ever safe."
    l "Maybe, but we can't just get rid of them all, John.{w=0.2} Not at this point, anyway."
    j "I know, but..."
    j "...I just wish they could use those evil desires for good."
    show leslie:
        ease 0.1 ypos 0.51
        ease 0.1 ypos 0.5
        repeat
    "I then felt her lightly shake as I heard laughter come out of her."
    j "What's so funny about that?"
    show leslie:
        ease 0.05 ypos 0.5
    l "Sorry, sorry; it's not you."
    l "I just caught a glimpse of that old Halloween picture."
    "Knowing which one she meant, I smiled and turned towards it, myself."
    scene cg halloween with dissolve
    pause 1
    j "Hope really thought a family of rednecks would be funny."
    l "And she was right, based on everyone's reactions."
    l "To think it was our last Halloween together..."
    j "Yeah..."
    j "I'm still impressed by the masks you made.{w=0.2} And in such a short time, too."
    l "Please.{w=0.2}\nI've dealt with more stressful deadlines from stingy producers."
    j "Fair enough."
    j "Though I remember the molding process certainly being a bit unpleasant."
    l "That's the price you pay to get a mask that fits your face perfectly."
    j "Whatever happened to those masks, anyway?"
    l "I think they're still in the attic, probably buried somewhere under the Christmas decorations."
    j "I see."
    "We then stood against each other in silence, staring at the picture."
    "I looked down at Leslie, who had a grin on her tear-stained face."
    "I smiled, myself, at the sight of seeing her happy."
    "After everything, it was nice to have a moment to feel something that wasn't depression or stress, if only for a brief second."
    "She turned up to face me when she noticed I was looking at her."
    scene bg kitchen
    show john at two2 zorder 1
    show leslie zorder 2:
        xalign 0.6 yalign 0.5
    with dissolve
    pause 0.1
    l "What?"
    "I felt my smile grow a bit as I cupped her cheek in my hand."
    j "Nothing."
    "We looked at each other with smiles before fully locking back into a hug."
    call scene_end

label new_zones:
    python:
        hoursLeft = 24
        minutesLeft = 1
        secondsLeft = 0
    call timeleft
    scene bg livingroom with longdissolve
    pause 1
    nvl show dissolve
    narrate """
    When it got closer to the big announcement, we turned the TV back on.

    Our hands were locked tightly together in anticipation.

    The fact that Seattle has gone this long without being chosen is oddly enough what scares us the most.

    {nw}

    The first 4 REDD Wars were set in your more obvious cities: New York, LA, Chicago, and Detroit.

    Reno and Springfield were admittedly a bit of a curveball, probably because a pattern was being detected, but things went back to \"predictable\" last year with Atlanta.

    Sure, we're far from the only \"remaining\" famous city in the country, but we're still a famous city, nonetheless.

    {nw}

    And now we wait in anticipation as the timer quickly counts down to zero, with our fate being revealed to us.
    """
    nvl hide dissolve
    nvl clear
    show john at two1
    show leslie at two2
    with dissolve
    pause 0.5
    "The screen went black for a brief moment."
    "It then showed the REDD of hour sitting behind his desk at the REDD Base."
    play music reddington
    r "Greetings, Earth."
    r "At exactly this time tomorrow, the 8th annual REDD War will commence."
    r "I will now reveal the locations of the 5 dedicated War Zones."
    r "These zones are the only locations on the planet where REDD War activity will be held, so if you do not live in any of these cities and wish to participate in the War, you will have 24 hours to find your way over there."
    "He gives the same exact speech every time, yet it's still intimidating to hear."
    "Leslie squeezed my hand even tighter."
    r "Let us begin."
    r "The locations for the 2031 REDD War are as follows:"
    r "Adelaide, Australia."
    r "Hamburg, Germany."
    r "Osaka, Japan."
    "I could feel my heart beating faster and faster."
    "I noticed that both mine and Leslie's hands were really sweaty."
    r "Porto Alegre, Brazil."
    "This is it."
    "One final city, and it's undoubtedly going to be in America."
    "I held my breath."
    "Leslie and I stayed completely still."
    "..."
    r "Seattle, United States."
    "Almost immediately, I heard Leslie scream as she quickly covered her mouth with her other hand."
    "My heart dropped straight down into my gut."
    "Seattle...{w=0.5}\nAfter all this time..."
    "Surely we didn't mishear him, right?"
    r "These 5 cities are the official War Zones for tomorrow's REDD War."
    "The screen then showed a list of the 5 cities he had just stated."
    "And sure enough, at Number 5, was \"Seattle, United States\"."
    r "Very shortly, official members of the REDD Base will be at these locations to place the proper barriers around the Zones."
    r "Everyone living in these zones will have exactly 24 hours to either evacuate the city or prepare for the War."
    l "Nonononono!!!"
    "I side-hugged Leslie as she began to cry and breathe heavily."
    r "To those whose cities were not chosen for the REDD War--"
    play sound tv
    "I turned the TV off and hugged my wife even tighter."
