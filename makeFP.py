from xml.etree.ElementTree import Element, SubElement, ElementTree
import xml.etree.ElementTree as ET

with open('recipes.js', 'r') as f:
    data = f.read()
    data=data[223:]
    data = data.replace('export default [', '[')
    data = data.replace('];', ']')
    data = eval(data)

for i in data:
    if i['sensor'] != 4:
        continue
    sample = ET.parse('sample.FP1')
    root = sample.getroot()
    print(ET.dump(root.find("PropertyGroup")))
    target_tag = root.find("PropertyGroup")
    target_tag.set('label', str(i['name']+' by '+i['creator']))
    target_tag.find('ExposureBias').text =  str(i['ev'])
    target_tag.find('DynamicRange').text = str(i['dr'].replace('DR', ''))

    tree = ElementTree(root)
    tree.write('recipe/'+i['name']+' by '+i['creator']+'.FP1', encoding='utf-8', xml_declaration=True)
    break