import os
from kivy.lang import Builder

import xml.sax
from kivy.uix.popup import Popup




class PetElement(xml.sax.ContentHandler):
    def __init__(self, model):
        self.current_data = False
        self.pet_name = False
        self.birth_date = False
        self.last_appointment_date = False
        self.vet_name = False
        self.disease = False
        self.handler_name = False
        self.phone_number = False
        self.mail = False
        self.address = False

        self.model = model

        # self.dialog = main_view

        self.count_pet = 0
        self.count_handler = 0
        self.bad_files_count = 0





    def startElement(self, name, attrs):
        self.current_data = name
        if self.current_data == 'pets_list':
            self.pets_list = []
            self.handlers_list = []
            self.all_list = []
            self.bad_line_name = ''
            self.bad_line_count = 0
            self.line = 1

            self.pet_name_line = False
            self.birth_date_line = False
            self.last_appointment_date_line = False
            self.vet_name_line = False
            self.disease_line = False

            self.pet_name_line_count = 0
            self.birth_date_line_count = 0
            self.last_appointment_date_line_count = 0
            self.vet_name_line_count = 0
            self.disease_line_count = 0


        elif self.current_data == 'pet':
            self.pet = {}
            self.handler = {}
            self.all = {}
            self.line += 1

            self.close_pet_name = False
            self.close_birth_date = False
            self.close_last_appointment_date = False
            self.close_vet_name = False
            self.close_disease = False



        elif self.current_data == 'pet_name':
            self.pet_name=True
            self.line += 1
            self.pet_name_line_count = self.line

        elif self.current_data == 'birth_date':
            self.birth_date = True
            self.line += 1
            self.birth_date_line_count = self.line

        elif self.current_data == 'last_appointment_date':
            self.last_appointment_date = True
            self.line += 1
            self.last_appointment_date_line_count = self.line

        elif self.current_data == 'vet_name':
            self.vet_name = True
            self.line += 1
            self.vet_name_line_count = self.line

        elif self.current_data == 'disease':
            self.disease = True
            self.line += 1
            self.disease_line_count = self.line


        elif self.current_data == 'handler_name':
            self.handler_name = True
            self.line += 1
        elif self.current_data == 'phone_number':
            self.phone_number = True
            self.line += 1
        elif self.current_data == 'mail':
            self.mail = True
            self.line += 1
        elif self.current_data == 'handler_address':
            self.address = True
            self.line += 1


        self.current_data=''


    def endElement(self, tag):
        if tag == 'pet_name':
            if self.pet_name_line == True:
                self.pet_name_line = False
                self.close_pet_name = True
        elif tag == 'birth_date':
            if self.birth_date_line == True:
                self.birth_date_line = False
                self.close_birth_date = True
        elif tag == 'last_appointment_date':
            if self.last_appointment_date_line == True:
                self.last_appointment_date_line = False
                self.close_last_appointment_date = True
        elif tag == 'vet_name':
            if self.vet_name_line == True:
                self.vet_name_line = False
                self.close_vet_name = True

        elif tag == 'disease':
            if self.disease_line == True:
                self.disease_line = False
                self.close_disease = True


        elif tag == 'pet':
            self.line += 1

            if self.count_pet == 5 and self.count_handler == 4:
                self.pets_list.append(self.pet)
                self.handlers_list.append(self.handler)
                self.all_list.append(self.all)

                self.pet = {}
                self.handler = {}
                self.all = {}

                self.count_pet=0
                self.count_handler=0
            else:
                self.count_pet = 0
                self.count_handler = 0
                self.bad_files_count += 1

                if self.close_pet_name == False:
                    self.bad_line_name = 'pet_name'
                    self.bad_line_count = self.pet_name_line_count
                elif self.close_birth_date == False:
                    self.bad_line_name = 'birth_date'
                    self.bad_line_count = self.birth_date_line_count
                elif self.close_last_appointment_date == False:
                    self.bad_line_name = 'last_appointment_date'
                    self.bad_line_count = self.last_appointment_date_line_count
                elif self.close_vet_name == False:
                    self.bad_line_name = 'vet_name'
                    self.bad_line_count = self.vet_name_line_count
                elif self.close_disease == False:
                    self.bad_line_name = 'disease'
                    self.bad_line_count = self.disease_line_count
                print(self.bad_line_name, self.bad_line_count)



    def characters(self, content):
        # pet info
        if self.pet_name:
            #self.pet_name = content
            self.pet['pet_name'] = content
            self.all['pet_name'] = content
            self.count_pet += 1
            self.pet_name = False
            self.pet_name_line = True

        elif self.birth_date:
            self.birth_date_line = True
            self.count_pet += 1
            self.pet['birth_date'] = content
            self.all['birth_date'] = content

            self.birth_date = False


        elif self.last_appointment_date:
            self.pet['last_appointment_date'] = content
            self.all['last_appointment_date'] = content
            self.last_appointment_date = False
            self.last_appointment_date_line = True

            self.count_pet += 1

        elif self.vet_name:
            self.pet['vet_name'] = content
            self.all['vet_name'] = content
            self.vet_name = False
            self.vet_name_line = True

            self.count_pet += 1


        elif self.disease:
            self.pet['disease'] = content
            self.all['disease'] = content
            self.disease = False
            self.disease_line = True

            self.count_pet += 1


        # handler info
        elif self.handler_name:
            self.handler['handler_name'] = content
            self.all['handler_name'] = content
            self.handler_name = False
            self.count_handler += 1
        elif self.phone_number:
            self.handler['phone_number'] = content
            self.all['phone_number'] = content
            self.phone_number = False
            self.count_handler += 1
        elif self.mail:
            self.handler['mail'] = content
            self.all['mail'] = content
            self.mail = False
            self.count_handler += 1
        elif self.address:
            self.handler['handler_address'] = content
            self.all['handler_address'] = content
            self.address = False
            self.count_handler += 1

           #self.disease = content

    def return_pets_list(self):
        return self.pets_list
    def return_handlers_list(self):
        return self.handlers_list
    def return_all_list(self):
        return self.all_list
    def return_bad_files_count(self):
        return self.bad_files_count
    def return_bad_line_name(self):
        return self.bad_line_name
    def return_bad_line_count(self):
        return self.bad_line_count


#Builder.load_file(os.path.join(os.path.dirname(__file__), "sax_parser.kv"))