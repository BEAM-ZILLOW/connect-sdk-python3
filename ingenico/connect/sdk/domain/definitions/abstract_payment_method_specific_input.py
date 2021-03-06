# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class AbstractPaymentMethodSpecificInput(DataObject):

    __payment_product_id = None

    @property
    def payment_product_id(self):
        """
        | Payment product identifier
        | Please see payment products <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/paymentproducts.html> for a full overview of possible values.
        
        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    def to_dictionary(self):
        dictionary = super(AbstractPaymentMethodSpecificInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'paymentProductId', self.payment_product_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
