My solutions to the Advent of Code (2015).

I am using python as a "warm-up" language, to do two things:

1. Get a feel for what the Advent of Code puzzles are like, and what is needed to solve them.
2. Practice refactoring old solutions when I have new ideas.

Explanation:

Any puzzle series (especially one made by a single individual) has a unique feel, a set of internal design choices and recurring themes. So when you first begin them you're solving everything blind, but once you've done a few, you know what to expect and what tool sets you are likely to need.
Since I find python to be such a straight forward language that's easy to play around with, I decided it'd be a good first foray into the AoC. Once I'm comfortable that I can actually solve the whole calendar, I intend to switch languages around to experiment with the various languages I've programmed in and maybe try out some new ones.

I believe that this is a good place to do some refactoring as the individual code chunks are very small, usually a few dozen lines in a self contained question, solution, answer environment with easily testability. So I'm altering things as I go with 2 main goals, the first (and more focused) is unifying my testing, as I think of better ways to ensure that my code is rigorous and can stand up to edge cases (which I often know don't exist in the actual problems, and can be discounted with a quick Ctrl-f on the input file) I want to implement them, and if this means altering the testing suite of previous solutions, then I will take the time to do that. The second method of refactoring is when I realise I used a "silly" design paradigm in an older problem, if I think I can change it in a reasonable time frame, then I will. Or if I think the new idea is fun and/or interesting enough for me to put the time in, then I will.


<details>

    <summary>Initialisation</summary>

    ## Ensure Conda or miniconda is installed

    ## clone and init with ssh:

```bash
git clone git@github.com:mathematicalninja/AoC_2015.git
cd AoC_2015
bash setup.sh
```

</details>
