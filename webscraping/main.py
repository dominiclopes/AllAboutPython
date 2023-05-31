import json
from collections import defaultdict, Counter
import yaml
import csv

yamlFileName = "LoanService.yaml"
csvFileName = "LoanService.csv"

# yamlFileName = "CreditV2Service.yaml"
# csvFileName = "CreditV2Service.csv"

# yamlFileName = "ApplicationService.yaml"
# csvFileName = "ApplicationService.csv"


with open(yamlFileName, "r") as fileObj:
    apiEndpoints = yaml.safe_load(fileObj)
    print(json.dumps(apiEndpoints))

tagEndpointDetailsListDict = defaultdict(list)
for apiEndpoint, apiMethods in apiEndpoints["paths"].items():
    for apiMethod, apiDetails in apiMethods.items():
        if apiMethod == "summary":
            continue
        for tag in apiDetails["tags"]:
            tagEndpointDetailsListDict[tag].append({
                "endpoint": apiEndpoint,
                "method": apiMethod
            })
print(json.dumps(tagEndpointDetailsListDict))

# # Get API tags verses their method counts
# tagEndpointMethodCountDict = {
#     tag: Counter([endpointDetails["method"] for endpointDetails in endpointDetailsList])
#     for tag, endpointDetailsList in tagEndpointDetailsListDict.items()
# }
# print(json.dumps(tagEndpointMethodCountDict))

# with open(csvFileName, "w", newline="") as fileObj:
#     writer = csv.writer(fileObj)
#     writer.writerow(["Tag", "get", "post", "put/patch", "delete"])
#
#     requiredList = []
#     for tag, endpointMethodCount in tagEndpointMethodCountDict.items():
#         requiredList.append(
#             [tag, endpointMethodCount.get("get", 0), endpointMethodCount.get("post", 0),
#              endpointMethodCount.get("put", 0) + endpointMethodCount.get("patch", 0),
#              endpointMethodCount.get("delete", 0)]
#         )
#     writer.writerows(requiredList)

# Get API tag, method, endpoint details
with open(csvFileName, "w", newline="") as fileObj:
    writer = csv.writer(fileObj)
    writer.writerow(["Sr. No.", "Tag", "Method", "Endpoint"])

    requiredList = []
    index = 1
    for tag, endpointDetailsList in tagEndpointDetailsListDict.items():
        for endpointDetails in endpointDetailsList:
            requiredList.append([index, tag, endpointDetails["method"], endpointDetails["endpoint"]])
            index += 1
    writer.writerows(requiredList)
