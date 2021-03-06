# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectPaymentProduct863SpecificInput(DataObject):

    __integration_type = None

    @property
    def integration_type(self):
        """
        | The type of integration with WeChat. Possible values:
        
        * desktopQRCode - used on desktops, the consumer opens the WeChat app by scanning a QR code.
        * urlIntent - used in mobile apps or on mobile web pages, the consumer opens the WeChat app using a URL intent.
        * nativeInApp - used in mobile apps that use the WeChat Pay SDK.
        
        Type: str
        """
        return self.__integration_type

    @integration_type.setter
    def integration_type(self, value):
        self.__integration_type = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct863SpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'integrationType', self.integration_type)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct863SpecificInput, self).from_dictionary(dictionary)
        if 'integrationType' in dictionary:
            self.integration_type = dictionary['integrationType']
        return self
