import json
postitmp = input("Kerro postitoimipaikkasi: ")
postitmpUpperCase = postitmp.upper()
print(postitmpUpperCase)
postnrList = []

with open('postcode_map_light.json') as json_file:
    data = json.load(json_file)
    # print(data['25840'])
    for i in data:
        if data[i] == postitmpUpperCase:
            #postnrList[i] = data[i]
            print(i, end=', ')
