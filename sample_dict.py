#DICTIONARY
sample_dict = {
    "AN":"Andaman and Nicobar Islands",
    "AP":"Andhra Pradesh",
    "AR":"Arunachal Pradesh",
    "AS":"Assam",
    "BR":"Bihar",
    "CG":"Chandigarh",
    "CH":"Chhattisgarh",
    "DN":"Dadra and Nagar Haveli",
    "DD":"Daman and Diu",
    "DL":"Delhi",
    "GA":"Goa",
    "GJ":"Gujarat",
    "HR":"Haryana",
    "HP":"Himachal Pradesh",
    "JK":"Jammu and Kashmir",
    "JH":"Jharkhand",
    "KA":"Karnataka",
    "KL":"Kerala",
    "LA":"Ladakh",
    "LD":"Lakshadweep",
    "MP":"Madhya Pradesh",
    "MH":"Maharashtra",
    "MN":"Manipur",
    "ML":"Meghalaya",
    "MZ":"Mizoram",
    "NL":"Nagaland",
    "OR":"Odisha",
    "PY":"Puducherry",
    "PB":"Punjab",
    "RJ":"Rajasthan",
    "SK":"Sikkim",
    "TN":"Tamil Nadu",
    "TS":"Telangana",
    "TR":"Tripura",
    "UP":"Uttar Pradesh",
    "UK":"Uttarakhand",
    "WB":"West Bengal",
    "MN": [{"XN":"XN"}],
    "VN":{"GH":"GH"}
}
print(sample_dict)

print("TN" in sample_dict)
print(sample_dict["TN"])

##
print(sample_dict.get("XN", "Country not present in India"))

copy_dict = sample_dict
print(copy_dict.get("TN"))

import copy
new_dict  = copy.copy(sample_dict)
deep_dict = copy.deepcopy(sample_dict)




##Change value for a key
sample_dict["TN"] = "Madras"
print(sample_dict["TN"])
print(copy_dict.get("TN"))

sample_dict["MN"].append ("Mangalore")
print(new_dict["MN"])
print(deep_dict['MN'])

print(new_dict["TN"])
print(deep_dict["TN"])

sample_dict["MN"] = "Tamil Nadu"
sample_dict["VN"] = "Tamil Nadu"
print(sample_dict)

print(sample_dict.values())
list3 = sample_dict.values()
print(sum(x == 'Tamil Nadu' for x in list3))









