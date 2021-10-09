"""Demonstration of dictionary capabilities"""

# DEclaring type of dict
schools: dict[str,int]

#Initializing to empty dictionary
schools = dict()


schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)

#Access value by its key
print(f"UNC has {schools['UNC']} students")

schools.pop("Duke")


# Tets for existence of a key
is_duke_present: bool = "Duke" in schools
print(is_duke_present)
print(schools)

if "Duke" in schools:
    print("Found 'Duke'")
else:
    print("No key 'Duke' in schools")

#Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] = schools["NCSU"] + 200
schools["NCSU"] += 200


# Empty dictionary literals
schools = {}  #Same as dict()

#Alternatively initialize key-value pairs
schools = {
    "UNC": 19400,
    "Dukie": 6717,
    "NCSU": 26150}
print(schools)


for k in schools:
    print(f"Key: {k} -> Value: {0.5*schools[k]}")