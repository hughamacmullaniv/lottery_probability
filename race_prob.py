#!/usr/bin/env python
import sys
import numpy as np
from tabulate import tabulate

# RUN LIKE:
# ./race_prob.py SEATS POWER ENTRANTS_Y1 ENTs_Y2 ENTs_Y3 ...
#
# EXAMPLE w/2020 WSER DATA (2^n tickets / year):
# ./race_prob.py 314 2 3290 1438 901 543 312 126 53 9
#
# EXAMPLE w/2020 Wasatch DATA (1 ticket / year):
# ./race_prob.py 371 1 487 65 14

race_capacity = int(sys.argv[1])
power = int(sys.argv[2])
applicants = np.array([int(r) for r in sys.argv[3:]])
if power > 1:
    tickets_per_applicant = np.array(
        [power ** (t) for t in list(range(len(applicants)))]
    )
else:
    tickets_per_applicant = np.array(list(range(1, len(applicants) + 1)))
num_categories = len(applicants)
original_tickets = applicants * tickets_per_applicant
ticket_counts = original_tickets

for i in range(race_capacity):
    prob_of_selecting_category = ticket_counts / sum(ticket_counts)
    exp_ticket_reduction = prob_of_selecting_category * tickets_per_applicant
    ticket_counts = ticket_counts - exp_ticket_reduction

tickets_taken = original_tickets - ticket_counts
odds_of_selection = tickets_taken / original_tickets
num_people_taken = odds_of_selection * applicants

table = {
    "year": range(1, num_categories + 1),
    "applicants": applicants,
    "racers": np.round(num_people_taken, decimals=1),
    "odds": np.round(odds_of_selection * 100, decimals=2),
}
print(f"\n{tabulate(table, headers='keys')}\n")
