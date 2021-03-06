# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.mandates.definitions.create_mandate_base import CreateMandateBase
from ingenico.connect.sdk.domain.payment.definitions.abstract_sepa_direct_debit_payment_product771_specific_input import AbstractSepaDirectDebitPaymentProduct771SpecificInput


class SepaDirectDebitPaymentProduct771SpecificInputBase(AbstractSepaDirectDebitPaymentProduct771SpecificInput):
    """
    | Object containing information specific to SEPA Direct Debit for Hosted Checkouts.
    """

    __mandate = None

    @property
    def mandate(self):
        """
        | Object containing information to create a SEPA Direct Debit mandate. Required for creating HostedCheckouts with SEPA Direct Debit supported.
        
        Type: :class:`ingenico.connect.sdk.domain.mandates.definitions.create_mandate_base.CreateMandateBase`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value

    def to_dictionary(self):
        dictionary = super(SepaDirectDebitPaymentProduct771SpecificInputBase, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'mandate', self.mandate)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SepaDirectDebitPaymentProduct771SpecificInputBase, self).from_dictionary(dictionary)
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = CreateMandateBase()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
