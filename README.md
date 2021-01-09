# Lottery Probability
Used to calculate race entry probabilities for lottery entrants based on the number of total available SEATS in the race, number of ENTRANTS for each YEAR, and POWER, which is generally 1 (1 ticket per year in the lottery: Wasatch, etc), or 2 (2^N tickets per year in the lottery: WSER, etc).

## Usage
```
./race_prob.py SEATS POWER ENTRANTS_Y1 ENTs_Y2 ENTs_Y3 ...
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
