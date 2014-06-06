say_script
==========

A simple Python 2 script to convert a dialogue script into a series of 'say' commands with different voices.

Conveniently, all Macs come with Python 2 preinstalled, so this script can be used by any Mac user.

### Usage

1. Run, e.g., `python SayScript.py foo.txt` in the Terminal. This will produce a shell script called `foo.txt.out` which already has the appropriate permissions.
2. Then just run `./foo.txt.out` to hear the play acted out by the say command.

### Sample input (from demo_script.txt)

The key point is that voice assignments are at the top, separated by a blank line from the dialogue. The name and dialogue must be separated by a `:` and a space. Same with the voices.

```
Vincent: bruce
Jules: fred

Vincent: It's the little differences. I mean, they got the same shit over there that we got here, but it's just...it's just, there it's a little different.
Jules: Example?
Vincent: All right. Well, you can walk into a movie theater in Amsterdam and buy a beer. And I don't mean just like in no paper cup; I'm talking about a glass of beer. And in Paris, you can buy a beer at McDonald's. And you know what they call a Quarter Pounder with Cheese in Paris?
Jules: They don't call it a Quarter Pounder with Cheese?
Vincent: Nah, man, they got the metric system. They wouldn't know what the fuck a Quarter Pounder is.
Jules: What do they call it?
Vincent: They call it a "Royale with Cheese."

```

### Sample output

The above input produces the following output:

```bash
#!/bin/bash 

say -v bruce "Its the little differences. I mean, they got the same shit over there that we got here, but its just...its just, there its a little different."
say -v fred "Example?"
say -v bruce "All right. Well, you can walk into a movie theater in Amsterdam and buy a beer. And I dont mean just like in no paper cup; Im talking about a glass of beer. And in Paris, you can buy a beer at McDonalds. And you know what they call a Quarter Pounder with Cheese in Paris?"
say -v fred "They dont call it a Quarter Pounder with Cheese?"
say -v bruce "Nah, man, they got the metric system. They wouldnt know what the fuck a Quarter Pounder is."
say -v fred "What do they call it?"
say -v bruce "They call it a Royale with Cheese."

```
