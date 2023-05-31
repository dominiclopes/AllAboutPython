import json
# a = {
#     "Content-Type": "application/json; charset=utf-8"
# }
# print(json.dumps(a))
#

b = {
    "resCode": 400,
    "resMessage": ""
}
print(json.dumps(b))


# {"username": "automationUser"}
# {"Content-Type": "text/plain"}

m = {'rejectionReasonCreationPayload': {"country_code": "MY", "name": "Automation", "name_eng": "Automation", "name_ind": "Automation", "name_may": "Automation", "name_zh": "Automation"}}
print(json.dumps(m))


n = {
    "product_id": "invalid"
}

print(json.dumps(n))


a = [
{"code":400,"message":"Validation errors:\nid => Invalid value\nusername => Username cannot be empty","meta":{}},
{"code":400,"message":"Validation error:\nid => Invalid value","meta":{}},
{"code":404,"message":"Loan id: 32493434 is not found","meta":{}},
{"code":400,"message":"Validation error:\nundefined => undefined","meta":{}}
]

import json
for v in a :
    print(json.dumps({"resCode": v["code"], "resMessage": v["message"]}))

# import uuid
#
# print(uuid.uuid1())
