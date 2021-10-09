# DigiTerminal
DigiTerminal is both a testing framework for the Digibutter 3.0 website and a prototype of sorts for NerrBot: Rehatched. DigiTerminal does not interact with the Nerr 3.0 API directly, it just emulates a web browser clicking around on the webpage. As such, DigiTerminal is clunky, and it isn't realy intended to be used for anything more than a proof of concept. If digibutter ever manages to become popular again one day (one can dream, can't he?), then I may consider reriting this to interact with the API directly. This could be useful for embedding into the Bitlands game if it were to ever come into existance again.

**Check out help.md for both the required dependencies AND _simple_ info on how to setup the Chrome webdriver.**

## Features
- Logging registered users into digibutter.nerr.biz
- Switching channels between both "All Posts" and "The Dump"
- Listing the topics and replies on the most recent page of the current channel
- Posting new topics to both "All Posts" and "The Dump" channels
- Replying to specific topics in the current channel

### What's NOT Supported
- Access to the chatbox
- Listing topics and replies separately
- Replying to replies
- Liking/Disliking

## Footnotes
- DigiTerminal is my first ever actual coding project. I wrote it entirely in Python and used the Selenium Python library for interaction with the website.
- NerrBot: Rehatched will be almost **entirely** different from DigiTerminal. The reason why I wrote all of this was just to find a sort of starting point for writing code.
- To my knowledge, most current users on Digibutter are mainly mobile users, so I doubt that anyone other than myself will ever actually use this. Again, it's just for me to get a foothold for writing NerrBot: ReHatched.
- To anyone who missed out on my announcement, Just a Normal Question Mark Block Who Likes to Post "Test" was me using DigiTerminal. He's going to hatch out of his ? Block one day and become NerrBot: Rehatched.
- Last thing: To anyone who's randomly stumbled upon this project and has no idea what this is all about: Come check out http://digibutter.nerr.biz. It's Hi-Technicaaal!
