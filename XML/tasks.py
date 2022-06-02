import xml.etree.cElementTree as et

tree=et.parse('C:/Users/samet.colak/PycharmProjects/Samet Çolak_bloopark(WORKING STUDENT TEST CASE)/XML/xml library.xml')
root=tree.getroot()
doc = et.parse("xml library.xml")
root_node = doc.getroot()

Items = []
Descriptions = []
Calories = []

for item in root.iter('item'):
    Items.append(item.text)
for desc in root.iter('description'):
    Descriptions.append(desc.text)
for cal in root.iter('calories'):
    Calories.append(cal.text)

total_list = Items + Descriptions + Calories
print("List:", total_list)