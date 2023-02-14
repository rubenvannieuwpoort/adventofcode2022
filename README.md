# Advent of code 2022

Solutions in Python. Obviously not written as code that I would deploy to production. In particular, I use bogus names and global variables.
Some solutions are not portable to every possible input (I can only think of day 22 now, but there might be more).

Most scripts provide an answer more or less immediately, but some are slower:

|     | time  |
|-----|-------|
| 15a | 25s   |
| 15b | 40s   |
| 16b | 80s   |
| 19a | 1880s |
| 19b | 3000s |
| 20b | 5s    |
| 23b | 5s    |
| 24a | 95s   |
| 24b | 265s  |

I probably should have optimized 19 further, but implementing some pruning rule that I couldn't understand feels like cheating, so I just left it run for a long time.

If your computer has less than 64GB of RAM (hah, peasant!) you might want to consider changing the number in this line from both parts of day 19
```
@lru_cache(maxsize=134217728)
```

to some lower number.
