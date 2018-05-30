#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# poi = 0
# for person in enron_data:
#     if enron_data[person]['poi'] == True:
#         poi += 1

# poi_name_record = open("../final_project/poi_names.txt").read().split("\n")
# poi_name_total = [record for record in poi_name_record if "(y)" in record or "(n)" in record]
# print len(poi_name_total)

exercised_stock_options = []
for person in enron_data:
    # if enron_data[person]['poi'] == True:
    #     persons += 1
    if not math.isnan(float(enron_data[person]['salary'])) and person != 'TOTAL':
        exercised_stock_options.append(enron_data[person]['salary'])

print min(exercised_stock_options)
print max(exercised_stock_options)
# print persons
# print no_pay
# print len(enron_data)
# diff = len(enron_data) - persons
# out_of =  diff / len(enron_data)
# print out_of * 100