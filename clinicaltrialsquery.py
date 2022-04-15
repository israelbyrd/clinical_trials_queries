#Goal is to update a spreadsheet showing status of clinical trials

#Python API help
#https://realpython.com/api-integration-in-python/#rest-and-python-consuming-apis

#clinicaltrials.gov API demo
#https://clinicaltrials.gov/api/gui/demo/simple_study_fields

#clinicaltrials.gov API definitions
#https://clinicaltrials.gov/api/gui
import requests
import json

#TODO add variables for multiple NCT IDs into url expression.
#trials="NCT05111613+OR+NCT04795167"

#test for Inari PEERLESS trial for now.
api_url="https://clinicaltrials.gov/api/query/study_fields?expr=NCT05111613&fields=NCTId%2CBriefTitle%2CCondition&min_rnk=1&max_rnk=&fmt=json"

response=requests.get(api_url)

response.json()
