label prologue:
    show chapter_name "Prologue:":
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
        hoursLeft = 168
        minutesLeft = 0
        secondsLeft = 0
        startOrEnd = "begins"
    call timeleft
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

    {nw}

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
    nvl hide
    nvl clear
    play loop phone_vibrate
    pause 2
    show ben at two1
    show john at two2
    with dissolve
    pause 0.1
    j "Ah, excuse me."
    b "Of course."
    hide ben with dissolve
    pause 0.1
    stop loop
    j "Hey, Hope."
    h "Hey, Dad!{w=0.2}\nI'm not bothering you, am I?"
    j "If I ever answer \"Yes\" to that, you have my permission to hate me."
    h "Daaaaad!"
    j "Ahaha!{w=0.2}\nAnyway, did you need something?"
    h "I just wanted to make sure you'll still be home for dinner tonight."
    j "If the day finishes off as uneventful as the rest of today, then yes, I will be.{w=0.2} Why?"
    h "Just making sure, is all.{w=0.2}\nI don't wanna make too much or too little like the last few times."
    j "Hey, now! Don't go blaming me for you misreading the ingredient amount on the box."
    h "Okay, that was {b}one{/b} time, Dad!"
    j "Ahahaha.{w=0.2}\nDon't worry, pumpkin. Expect me to be there with you and Mom."
    h "Alright, sounds good!"
    play sound store_door
    "I then heard a familiar convenience store bell play through the speaker."
    j "What are you doing at Mike's Corner?"
    h "..."
    h "I'm...{w=0.5} just grabbing a soda."
    j "Hope, what have I told you about--?"
    h "Yeah, yeah, I know:{w=0.2}\n\"Caffeine isn't good for you and causes more harm than good.\""
    h "I've just had a long day at school today, and softball practice was tiring, and I need a quick pick-me-up. That's all."
    j "...alright, but don't make a habit out it, Hope."
    h "I won't, Dad. Just a quick soda from the fountain and I'll be out."
    j "Good girl."
    h "I'm not a dog, Dad."
    j "Ahaha.{w=0.2}\nAlright, well, I'll see you at home, Hope."
    h "Sounds good.{w=0.2}\nLove ya, Dad!"
    j "I love you, too."
    "We then hung up."
    show ben at two1 with dissolve
    pause 0.1
    b "Your girl still rebelling against your caffeine ban, eh?"
    j "Well, I can't be too mad.{w=0.2}\nThere are worse things she could be doing."
    b "True that."
    b "So, what's the future chef whipping up tonight?"
    j "Homemade chicken and rice."
    extend "\nOr, you know, as \"homemade\" as a packet from the store can be."
    b "We all gotta start somewhere, man."
    j "Fair enough.{w=0.2}\nAt least she's not setting the house on fire."
    b "Yet."
    j "Don't jinx me like that."
    b "Alright, alright.{w=0.2}\nThough, speaking of jinxes..."
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
    stop music
    dis "Calling all units. We have an active armed robbery at Mike's Corner convenience store at the corner of 7th and Broadband." # Will have to do research on proper Seattle police codes to create realistic dipatch call.
    "I froze for a brief moment.{w=0.2}\nDid I hear that right?"
    b "Mike's Corner?{w=0.2}\nIsn't that...?"
    "Yes, I heard it right."
    play loop police_siren
    show police_siren at middle with Dissolve(0.1)
    "I turned on the siren and started driving over without a second thought."
    play music drama
    $renpy.music.set_volume(0.3, delay=1.0, channel="loop")
    nvl show dissolve
    narrate """
    Ben informed dispatch that we were on our way, but I could barely hear him as I sped down the street.

    {nw}

    I was trying to think of how long Hope could've been in the store before the robbery occurred.

    I wasn't exactly paying attention to what time she called, so I can't say for sure how many minutes have passed.

    Surely it doesn't take long to just grab a soda from the fountain and pay for it, right?

    Of course, other students are just now getting out from school, so the line could be full of them and she was stuck in line!

    Or maybe she was lucky enough to beat them all before they all arrived.
    """
    nvl hide
    nvl clear
    dis "Attention, units. Shots fired at Mike's Corner Mart. Proceed with caution."
    nvl show dissolve
    narrate """
    I could feel my heart beating faster.

    Out of the corner of my eye, I could see Ben staring at me.{w=0.2} It looked like a face of worry.

    I suppose under most circumstances, he'd say something reassuring, like \"She'll be okay\".

    But he knows that I'm not stupid. He knows he can't make a promise like that to me.

    {nw}

    Hope...

    Please be okay...
    """
    nvl hide dissolve
    nvl clear
    $renpy.music.set_volume(1.0, delay=1.0, channel="loop")
    pause 2
    stop loop fadeout(5.0)
    stop music fadeout(5.0)
    scene bg black with scenefade
    pause 2
    "We had finally arrived at Mike's."
    "But when we did..."
    play music shock
    scene bg white
    pause 0.1
    scene cg store_1
    pause 2
    "...we were too late."
    nvl show dissolve
    narrate """
    The thieves managed to get away, leaving only a shot-up store and bodies.

    Thankfully, some of them, including Mike himself, were still alive.{w}
    Critically injured, but alive.

    Ben alerted all officers in the area to be on the lookout for any suspicious individuals who may be responsible for this while I checked for other survivors.

    I was obviously doing my duty to check everyone, but there was one person on my mind that I was searching for.

    {nw}

    I wasn't seeing any sign of her, and she wasn't responding to her name when I called it out.

    That could be a sign that she was out of the store by the time the robbery occurred, but maybe...

    ...
    """
    nvl hide
    nvl clear
    stop music
    "Then, by the soda fountain in the back corner of the store, there was someone lying on the ground."
    scene cg store_2 with longdissolve
    pause 1
    "Lying there with a spilled cup of soda next to her."
    "Wearing a softball jersey."
    "With blood all over her chest."
    j "Hope!"
    "I bolted right over to her and placed my fingers on the side of her neck."
    j "Come on...!{w=1}\n{b}COME ON!!{/b}"
    "..."
    j "No...!{w=1}\nNononononoNONONONONO!!!!"
    "I collapsed to the ground as I involuntarily wrapped my arms tightly around her."
    scene bg black with longdissolve
    pause 1
    j "{cps=*0.5}{b}H O O O O O O O O P E ! ! !{/b}{/cps}"
    pause 3
    play music intruder
    nvl show dissolve
    narrate """
    Due to the personal tie to this particular incident, I was essentially forbidden to have any involvement in it besides my initial statement of what I witnessed.

    And due to the personal loss that had occurred, I was given time off to cope.

    I was told that I could take as much time as I needed before I returned.

    But come on.{w=0.2} No amount of \"time off\" is ever going to make this pain go away.

    {nw}

    When I told Leslie what had happened to our daughter...

    Well, how do you {b}think{/b} she would react to that news?

    Our little girl...{w=0.3} Our superstar softball pitcher...{w=0.3} Our aspiring chef...

    Gone.

    {clear}

    Even though I had no direct involvement with the case, I still soaked up information on the investigation from both the news and Ben.

    Fortunately, the security cameras were operational, and clear footage of the shooters was found.

    According to Ben, they were all REDD.{w} But not just any REDD.

    He said that the culprit was Flang Sormin and two of his crew.

    Just hearing that name caused me to tense up.
    """
    nvl hide dissolve
    nvl clear
    show flang at middle with longdissolve
    pause 0.5
    nvl show dissolve
    narrate """
    Flang Sormin is the most notorious gang leader in all of Seattle.{w=0.2}\nNay, the entire west coast.

    As a REDD, he's naturally intimidating and powerful, so it didn't take long for him to overthrow a lot of the criminals already plaguing the city.

    Though his rise to power is essentially the equivalent of replacing 10 starving wolves with 1 starving bear.

    He's often the example humans turn to as to how the REDD are too dangerous to belong in our society.

    On the inverse, he's often the example REDD turn to as to why the REDD War needs to be more frequent and spacious, since apparently legal crime in only 5 cities for 12 hours a year isn't good enough for them.

    {clear}

    But then Ben told me something.

    He said that despite having clear footage of the culprits, the station is going to just drop the investigation.

    They claim it's because it's a relatively low-profile crime compared to Sormin's other disasters, but Ben and I aren't stupid.

    {nw}

    It's an open secret that the reason Sormin is able to get away with half the shit he does is because he's in cahoots with the force.

    Well, I suppose the proper way to describe it is he's {b}blackmailing{/b} the force.

    After all, Flang Sormin is a pretty big name.{w=0.2} So big, in fact, that even the REDD leader, Lord Reddington, is aware of him and his work.

    If Flang Sormin were to be incarcerated, it might just piss off the most influential REDD on the entire planet.

    And God help the man that does that.
    """
    nvl hide dissolve
    nvl clear
    pause 0.5
    hide flang with longdissolve
    pause 1
    nvl show dissolve
    narrate """
    It's kinda funny and cliché, really.

    {i}\"You never fully realize how bad it is until it happens to you.\"{/i}

    I knew that the force conveniently would put as little effort as possible into stopping Sormin.

    I knew that families wouldn't receive any proper closure as a result.

    But things like this happened even long before the REDD showed up, so I guess it was more or less to be expected.

    {nw}

    But now...

    Well, now it's personal.

    I suppose I was hopeful enough to think they would make an exception for me.

    For one of their fellow brothers.

    {nw}

    But no.

    They feared the REDD more than they cared for one of their own.

    {clear}

    Well, that's their choice.

    So now it's my turn to make mine.

    {nw}

    My \"time off\" had officially gone from temporary to indefinitely.

    Maybe it wasn't the wisest move, since it was still a source of income, and funerals aren't exactly cheap.

    But unlike the higher-ups, I have a soul.

    {clear}

    Some of the stress in my life was reduced a week after the shooting, when it was revealed that Seattle wasn't one of the 5 War Zones.{w=0.2} That honor was given to Reno.

    Honestly, that might be for the best.

    Not only because that means that the city won't collapse on itself in a 12-hour night, but who knows what I might've done to take advantage of it.

    The rules of the REDD War state that humans can only attack a REDD in self-defense, but if my daughter's death has shown anything, it's that rules alone don't do jack shit to stop someone.

    That's why I always wanted to be in law enforcement ever since I was a kid:{w=0.2} someone needs to keep the \"good guys\" safe and the \"bad guys\" locked up.

    Though, sadly, it's not that simple, is it?

    As the old saying goes, \"Everyone is the good guy in their own story.\"

    {clear}

    I wasn't really sure where my life was going to go from there.

    I didn't know when or if I'd get a new job.

    I didn't know when or if the bills would be paid.

    I didn't know when or if we'd get food on the table.

    I didn't know when or if we'd fully accept everything that had happened.

    {nw}

    But there was one thing that I did know for sure.

    If I'm ever given the chance to come face-to-face with Flang Sormin...

    ...I'll serve justice the only way I possibly can.

    {nw}
    """
    stop music
    narrate "By killing him."
    nvl hide
    nvl clear
    pause 3
    jump chapter_1
