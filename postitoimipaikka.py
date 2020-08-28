import json
postinro = input("Kerro postinumero: ")
print(postinro)


with open('postcodes.json') as json_file:
    data = json.load(json_file)
    for i in data:
        if i['postcode'] == postinro:
            print(i['postcode_fi_name'])
            break
