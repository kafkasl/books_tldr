# The Mythical Man-Month

Author: Frederick Brooks

## 1. The Tar Pit

### The Woes of the Craft

[Inherent woes of computer programing]

First, one must perform perfectly. [referring to programming language's syntax correction]

Next, other people set one's objectives, provide one's resources, and furnish one's information.

The dependence upon others has a particular case that is especially painful for the system programmer. He depends on other people's programs.

The next woe is that designing grand concepts is fun; finding nitty little bugs is just work.

The product over which one has labored so long appears to be obsolete upon (or before) completion.

## 2. The Mythical Man-Month

More software projects have gone awry for lack of calendar time than for all other causes combined. Why is this cause of disaster so common?

First, our techniques for estimating are poorly developed. More seriously, they reflect an unvoiced assumption which is quite untrue, i.e., that all will go well.

Second, our estimating techniques fallaciously confuse effort with progresss, hiding the assumption that men and months are interchangeable.

[...]

For some years I have been successfully using the following rule of thumb for scheduling a software task:

* 1/3 planning
* 1/6 coding
* 1/4 component test and early system test
* 1/4 system test, all components in hand

This differs from conventional scheduling in several important ways:
The fraction devoted to planning is larger than normal. Even so, it is barely enough to produce a detailed and solid specification, and not enough to include research or exploration of totally new techniques.
The half of the schedule devoted to debugging of completed code is much larger than normal.
The part that is easy to estimate, i.e., coding, is given only one-sixth of the schedule.

In examining conventionally scheduled projects, I have found that few allowed one-half of the projected schedule for testing, but that most did indeed spend half of the actual schedule for that purpose. Many of these were on schedule until and except in system testing.

Failure to allow enough time for system test, in particular, is peculiarly disastrous. Since the delay comes at the end of the schedule, no one is aware of schedule trouble until almost the delivery date. Bad news, late and without warning, is unsettling to customers and to managers.

Furthermore, delay at this point has unusually severe financial, as well as psychological, repercussions. The project is fully staffed, and cost-per-day is maximum. More seriously, the software is to support other business effort (shipping of computers, operation of new facilities, etc.) and the secondary costs of delaying these are very high, for it is almost time for software shipment. Indeed, these secondary costs may far outweigh all others. It is therefore very important to allow enough system test time in the original schedule.

[...]

Oversimplifying outrageously, we state Brook's Law:

*Adding manpower to a late software project makes it later*

This then is the demythologizing of the man-month. The number of months of a project depends upon its sequential constraints. The maximum number of men depends upon the number of independent subtasks. From the two quantities one can derive schedules using fewer men and fewer months. More software projects have gone awry for lack of calendar time than for all other causes combined.


### The telephone log

[When in doubt] It is essential, however, to encourage the puzzled implementer to telephone the responsible architect and ask his question, rather than to guess and proceed. It is just as vital to recognize that the answers to such questions are *ex cathedra* architectural pronouncements that must be told to everyone.

One useful mechanism is a *telephone log* kept by the architect. In it he records every question and every answer. Each week the logs of the several architects are concatenated, reproduced, and distributed to the users and implementers. While this mechanism is quite informal, it is both quick and comprehensive.

## 7. Why Did the Tower of Babel Fail

*Now the whole earth used only one language, with few words. On the occasion of a migration from the east, men discovered a plain in the land of Shinar, and settled there. Then they said to one another, "Come, let us make bricks, burning them well." So they used bricks for stone, and bitumen for mortar. Then they said, "Come, let us build ourselves a city with a tower whose top shall reach the heavens (thus making a name for ourselves), so that we may not be scattered all over the earth." Then the Lord came down to look at the city and tower which human beings had built. The Lord said, "They are just one people, and they all have the same language. If this is what they can do as a beginning, then nothing that they resolve to do will be impossible for them. Come, let us go down, and there make such a babble of their language that they will not understand one another another's speech." Thus the Lord dispersed them from there all over the earth, so that they had to stop building the city.*

Genesis 11:1-8
