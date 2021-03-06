# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.personal_name import PersonalName


class PersonalInformation(DataObject):

    __date_of_birth = None
    __gender = None
    __name = None

    @property
    def date_of_birth(self):
        """
        | The date of birth of the consumer
        | Format: YYYYMMDD
        
        Type: str
        """
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value

    @property
    def gender(self):
        """
        | The gender of the consumer, possible values are:
        
        * male
        * female
        * unknown or empty
        
        Type: str
        """
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def name(self):
        """
        | Object containing the name details of the consumer
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.personal_name.PersonalName`
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def to_dictionary(self):
        dictionary = super(PersonalInformation, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'dateOfBirth', self.date_of_birth)
        self._add_to_dictionary(dictionary, 'gender', self.gender)
        self._add_to_dictionary(dictionary, 'name', self.name)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalInformation, self).from_dictionary(dictionary)
        if 'dateOfBirth' in dictionary:
            self.date_of_birth = dictionary['dateOfBirth']
        if 'gender' in dictionary:
            self.gender = dictionary['gender']
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = PersonalName()
            self.name = value.from_dictionary(dictionary['name'])
        return self
