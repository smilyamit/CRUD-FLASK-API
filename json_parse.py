import json



# for writting json file
def  dump_values(numList, fName ="test.json") :

    with open(fName, "r+") as jsonFile:
        data = json.load(jsonFile)
        data['address']['values'] = numList
        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()

#for reading json file
def  load_jsonFile(file_name):
    with open(file_name, "r") as jsonFile:
        data = json.load(jsonFile)
        numList = data['address']['values'] 
    return  numList


