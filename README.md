# Lottery Probability
Used to calculate race entry probabilities for lottery entrants based on the number of total available SLOTS in the race, number of ENTRANTS for each YEAR, and POWER, which is generally 1 (1 ticket per year in the lottery: Wasatch, etc), or 2 (2^N tickets per year in the lottery: WSER, etc).

## Usage
```
./race_prob.py SLOTS POWER ENTRANTS_Y1 ENTs_Y2 ENTs_Y3 ...
```

## Examples
An example with 2020 WSER data (2^n tickets / year):
```
./race_prob.py 314 2 3290 1438 901 543 312 126 53 9
```
An example with 2020 Wasatch data (1 ticket / year):
```
./race_prob.py 371 1 487 65 14
```
### Explained:
```
371 = total slots in the race
  1 = 1 ticket per year in the lottery (first year = 1 ticket, etc)
487 = number of 1-ticket entrants
 65 = number of 2-ticket entrants
 14 = number of 3-ticket entrants
```
### Result:
```
$ ./race_prob.py 371 1 487 65 14

  year    applicants    racers    odds
------  ------------  --------  ------
     1           487     302.1   62.03
     2            65      55.7   85.63
     3            14      13.2   94.57

```
