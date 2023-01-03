#!/usr/bin/env python
import sys
import pandas as pd
import numpy as np
from tabulate import tabulate

# RUN LIKE:
# ./hardrock_prob.py <CSVFILENAME>.csv TOTAL_SLOTS
#
# EXAMPLE w/2023 DATA
# ./hardrock_prob.py hardrock_2023.csv 146
#
INFILE = sys.argv[1]
ttl_race_capacity = int(sys.argv[2])

df = pd.read_csv(INFILE)
GENDER_CAPACITY = (df.GENDER.value_counts(normalize=True) * ttl_race_capacity / 2).round().astype(int).to_dict()


def get_lottery_results(LOTTERY, GENDER, race_capacity):
    race_table = df[(df.GENDER == GENDER)&(df.LOTTERY == LOTTERY)].groupby(['GENDER', 'LOTTERY']).value_counts(['TICKETS'], sort=False).reset_index(name='COUNT')
    applicants = race_table.COUNT.values
    tickets_per_applicant = race_table.TICKETS.values
    num_categories = len(applicants)
    original_tickets = applicants * tickets_per_applicant
    ticket_counts = original_tickets
    #
    for i in range(race_capacity):
        prob_of_selecting_category = ticket_counts / sum(ticket_counts)
        exp_ticket_reduction = prob_of_selecting_category * tickets_per_applicant
        ticket_counts = ticket_counts - exp_ticket_reduction
    #
    tickets_taken = original_tickets - ticket_counts
    odds_of_selection = tickets_taken / original_tickets
    num_people_taken = odds_of_selection * applicants
    #
    table = {
        "tix_category": tickets_per_applicant,
        "applicants": applicants,
        "total_tix": original_tickets,
        "racers": np.round(num_people_taken, decimals=1),
        "odds": np.round(odds_of_selection * 100, decimals=2),
    }
    print(f"{tabulate(table, headers='keys')}\n")


for LOTTERY in df.LOTTERY.unique():
    for GENDER in df.GENDER.unique():
        print(f"LOTTERY: {LOTTERY} — GENDER: {GENDER}")
        get_lottery_results(LOTTERY, GENDER, GENDER_CAPACITY[GENDER])
