import re
import csv

class XML_Syntax_Error(Exception):
    pass

class XML_Definition_Error(Exception):
    pass

class xml_reader:
    def __init__(self,name = "Root Element"):
        self.root_element = name                            #Name of the root element
        self.element_stack = []                             #Stack which contains name of Elements
        self.main_dict = {}                                 #Nested dict with element->{Sub_element}

    def find_element(self,element):                         #Finds out the element and returns the dictionary associated with it
        for i in self.main_dict:
            if i == element:
                return self.main_dict[i]

    def element_stacker(self,name):                         #A list of all the elements present 
        self.element_stack.append(name)
    
    def add_dict(self,element):                             #Nested Dictionary keys as Element -> {Sub_elements}
        self.main_dict[element] = {}

    def add_dict_value(self,element,key,value):            #Adding Values to the nested dictionary
        self.main_dict[element][key] = value


def main():
   print("""
Hello Developer!, This is py4xml
In order to use my functionality try "import py4xml". If that didnt worked then try using "pip install py4xml".

To know more visit:
Readme : https://github.com/MasterANK/py4xml/blob/main/README.md
Github : https://github.com/MasterANK/py4xml
PyPI : https://pypi.org/project/py4xml/
""")


def read_xml(f):
    data = f.readlines()
    xml_file = xml_reader()
    element_flag = True
    attribute_flag = False

    for i in data:
        if a := re.fullmatch(r"<(\w+)>",i.strip("\n")):         #Init Header Check
            header_flag = False
            xml_file.root_element = a.group(1)

        elif a := re.fullmatch(r"<(\w+)>",i.strip()):           #Element Check
            if header_flag != False:
                raise XML_Definition_Error("Root Element not defined")

            if element_flag:                                    #To resolve the Bug where tag closing error never occurs
                element_flag = False
            else:
                raise XML_Syntax_Error(element+" is not closed properly")

            element = a.group(1)
            xml_file.element_stacker(element)
            xml_file.add_dict(element)
        
        elif a:= re.fullmatch(r"<(\w+) (\w+)=[\"|\']([^<>]+)[\"|\']>", i.strip()):      #Element with attributes check
            if header_flag != False:
                raise XML_Definition_Error("Root Element not defined")

            if element_flag:                                    #To resolve the Bug where tag closing error never occurs
                element_flag = False
            else:
                raise XML_Syntax_Error(element+" is not closed properly")

            attribute_flag = True    
            value =  a.group(3)
            element = str(a.group(1))+"_"+str(value) ; category = 'category'+'_'+str(a.group(2)) 
            xml_file.element_stacker(element)
            xml_file.add_dict(element)
            xml_file.add_dict_value(element,category,value)


        elif a:= re.fullmatch(r"<(\w+)>([^<>]+)</(\w+)>",i.strip()):        #Sub_elements Check + Closing
            if a.group(1) != a.group(3):
                raise XML_Syntax_Error(a.group(1)+" is not closed properly")
            xml_file.add_dict_value(element,a.group(1),a.group(2))
        
        elif a := re.fullmatch(r"</(\w+)>",i.strip()):          #Closing Root_Element,Element Check
            if attribute_flag:
                if str(a.group(1))+"_"+str(value) == element:
                    attribute_flag = False

            if a.group(1) == xml_file.root_element:
                header_flag = True
            if a.group(1) == element or not attribute_flag:
                element_flag = True 


    if not header_flag:
        raise XML_Syntax_Error(xml_file.root_element + " is not closed properly")
    if not element_flag:
        raise XML_Syntax_Error(element + " is not closed properly")
    
    return xml_file


def dict_write_xml(root_element ,data : dict,  write_f : object):       #Takes dictionary and write data to xml file
    write_f.write("<"+str(root_element)+">\n")
    for i in data:
        write_f.write("  <"+str(i)+">\n")
        element_flag = False
        for j in data[i]:
            exp = "    <"+str(j)+">"+str(data[i][j])+"</"+str(j)+">\n"
            write_f.write(exp)
        else:
            if element_flag == False:
                element_flag == True
                write_f.write("  </"+str(i)+">\n")
    else:
        write_f.write("</"+str(root_element)+">\n")


def extend_xml(data, write_f):      #Extend an extensible file
    file = read_xml(write_f)
    write_f.seek(0)
    file_data = file.main_dict
    file_data.update(data)
    dict_write_xml(file.root_element,file_data,write_f)


def csv_to_xml(root_element,csv_f,key,xml_f):       #Convert CSV -> Dict -> XML
    csv_data = csv.DictReader(csv_f)
    data = {}
    for i in csv_data:
        for j in i:
            if j == str(key):
                data[i[j]] = i
    dict_write_xml(root_element,data,xml_f)


def xml_to_csv(xml_f,csv_f,elementcol = None):      #Convert XML -> Dict -> CSV
    xml_obj = read_xml(xml_f)
    xml_data = xml_obj.main_dict
    elements = xml_data[xml_obj.element_stack[0]].keys()
    elements = list(elements)
    elementcol_flag = False

    if elementcol != None and elementcol not in elements:
        elementcol_flag = True
        elements.insert(0,elementcol)
    
    csvwriter = csv.DictWriter(csv_f,elements)
    csvwriter.writeheader()

    for i in xml_data:
        if elementcol_flag:
            xml_data[i][elementcol] = i
        csvwriter.writerow(xml_data[i])


if __name__ == "__main__":
    main()