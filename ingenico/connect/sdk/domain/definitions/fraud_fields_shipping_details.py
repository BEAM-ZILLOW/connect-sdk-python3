# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class FraudFieldsShippingDetails(DataObject):

    __method_details = None
    __method_speed = None
    __method_type = None

    @property
    def method_details(self):
        """
        | Details regarding the shipping method
        
        Type: str
        """
        return self.__method_details

    @method_details.setter
    def method_details(self, value):
        self.__method_details = value

    @property
    def method_speed(self):
        """
        | Shipping method speed indicator
        
        Type: int
        """
        return self.__method_speed

    @method_speed.setter
    def method_speed(self, value):
        self.__method_speed = value

    @property
    def method_type(self):
        """
        | Shipping method type indicator
        
        Type: int
        """
        return self.__method_type

    @method_type.setter
    def method_type(self, value):
        self.__method_type = value

    def to_dictionary(self):
        dictionary = super(FraudFieldsShippingDetails, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'methodDetails', self.method_details)
        self._add_to_dictionary(dictionary, 'methodSpeed', self.method_speed)
        self._add_to_dictionary(dictionary, 'methodType', self.method_type)
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudFieldsShippingDetails, self).from_dictionary(dictionary)
        if 'methodDetails' in dictionary:
            self.method_details = dictionary['methodDetails']
        if 'methodSpeed' in dictionary:
            self.method_speed = dictionary['methodSpeed']
        if 'methodType' in dictionary:
            self.method_type = dictionary['methodType']
        return self
