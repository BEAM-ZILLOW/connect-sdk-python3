# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair
from ingenico.connect.sdk.domain.payment.definitions.redirect_data import RedirectData
from ingenico.connect.sdk.domain.product.definitions.payment_product_field import PaymentProductField


class MerchantAction(DataObject):

    __action_type = None
    __form_fields = None
    __redirect_data = None
    __rendering_data = None
    __show_data = None

    @property
    def action_type(self):
        """
        | Action merchants needs to take in the online payment process. Possible values are:
        
        * REDIRECT - The consumer needs to be redirected using the details found in redirectData
        * SHOW_FORM - The consumer needs to be shown a form with the fields found in formFields. You can submit the data entered by the user in a Complete payment <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/complete.html> request. Additionally:
        
        * for payment product 3012 (Bancontact), to support payments via the Bancontact app, showData contains a QR code and URL intent.
        * for payment product 863 (WeChat Pay), to support payments via the WeChat app, showData contains a QR code, URL intent, or signature and nonce combination. The showData field describes when each of these values can be returned.
        | Note that WeChat Pay does not support completing payments.
        
        
        * SHOW_INSTRUCTIONS - The consumer needs to be shown payment instruction using the details found in showData. Alternatively the instructions can be rendered by us using the instructionsRenderingData
        * SHOW_TRANSACTION_RESULTS - The consumer needs to be shown the transaction results using the details found in showData. Alternatively the instructions can be rendered by us using the instructionsRenderingData
        
        Type: str
        """
        return self.__action_type

    @action_type.setter
    def action_type(self, value):
        self.__action_type = value

    @property
    def form_fields(self):
        """
        | Populated only when the actionType of the merchantAction is SHOW_FORM. In this case, this field contains the list of fields to render, in the format that is also used in the response of Get payment product <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/get.html>.
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.payment_product_field.PaymentProductField`]
        """
        return self.__form_fields

    @form_fields.setter
    def form_fields(self, value):
        self.__form_fields = value

    @property
    def redirect_data(self):
        """
        | Object containing all data needed to redirect the consumer
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirect_data.RedirectData`
        """
        return self.__redirect_data

    @redirect_data.setter
    def redirect_data(self, value):
        self.__redirect_data = value

    @property
    def rendering_data(self):
        """
        | This field contains the blob with data for the instructions rendering service.
        
        | This service will be available at the following endpoint:http(s)://{{merchant specific subdomain}}.{{base MyCheckout hosted payment pages domain}}/instructions/{{merchantId}}/{{clientSessionId}}
        
        | This instructions page rendering service accepts the following parameters:
        
        * instructionsRenderingData (required, the content of this field)
        * locale (optional, if present overrides default locale, e.g. "en_GB")
        * variant (optional, code of a variant, if present overrides default variant, e.g. "100")
        
        | You can offer a link to a consumer to see an instructions page for a payment done earlier. Because of the size of the instructionsRenderingData this will need to be set in a web form as a value of a hidden field. Before presenting the link you need to obtain a clientSessionId by creating a session using the S2S API. You will need to use the MyCheckout hosted payment pages domain hosted in the same region as the API domain used for the createClientSession call.
        
        | The instructionsRenderingData is a String blob that is presented to you via the Server API as part of the merchantAction (if available, and non-redirect) in the JSON return values for the createPayment call or the getHostedCheckoutStatus call (merchantAction inside createdPaymentOutput when available).You are responsible to store the instructionsRenderingData blob in order to be able to present the instructions page at a later time, when this information might no longer be available through Server API calls.
        
        Type: str
        """
        return self.__rendering_data

    @rendering_data.setter
    def rendering_data(self, value):
        self.__rendering_data = value

    @property
    def show_data(self):
        """
        | This is returned for the SHOW_INSTRUCTION, the SHOW_TRANSACTION_RESULTS and the SHOW_FORM actionType.
        | When returned for SHOW_TRANSACTION_RESULTS or SHOW_FORM, this contains an array of key value pairs of data that needs to be shown to the consumer.
        | Note: The returned value for the key BARCODE is a base64 encoded gif image. By prepending 'data:image/gif;base64,' this value can be used as the source of an HTML inline image.
        
        | For SHOW_FORM, for payment product 3012 (Bancontact), this contains a QR code and a URL intent that can be used to complete the payment in the Bancontact app.
        | In this case, the key QRCODE contains a base64 encoded PNG image. By prepending 'data:image/png;base64,' this value can be used as the source of an HTML inline image on a desktop or tablet (intended to be scanned by an Android device with the Bancontact app). The key URLINTENT contains a URL intent that can be used as the link of an 'open the app' button on an Android device.
        
        | For SHOW_FORM, for payment product 863 (WeChat Pay), this contains the PaymentId that WeChat has assigned to the payment. In this case, the key WECHAT_PAYMENTID contains this PaymentId. In addition, this can contain different values depending on the integration type:
        
        * desktopQRCode - contains a QR code that can be used to complete the payment in the WeChat app. In this case, the key QRCODE contains a base64 encoded PNG image. By prepending 'data:image/png;base64,' this value can be used as the source of an HTML inline image on a desktop or tablet (intended to be scanned by a mobile device with the WeChat app).
        * urlIntent - contains a URL intent that can be used to complete the payment in the WeChat app. In this case, the key URLINTENT contains a URL intent that can be used as the link of an 'open the app' button on a mobile device.
        * nativeInApp - contains a signature of the payment values and a nonce used to generate the signature, that can be used to complete the payment using the WeChat SDK. In this case, the key WECHAT_SIGNATURE contains the signature that should be used for the WeChat SDK field sign. The key SIGNATURE_NONCE contains the nonce that should be used for the WeChat SDK field noncestr.
        
        Type: list[:class:`ingenico.connect.sdk.domain.definitions.key_value_pair.KeyValuePair`]
        """
        return self.__show_data

    @show_data.setter
    def show_data(self, value):
        self.__show_data = value

    def to_dictionary(self):
        dictionary = super(MerchantAction, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'actionType', self.action_type)
        self._add_to_dictionary(dictionary, 'formFields', self.form_fields)
        self._add_to_dictionary(dictionary, 'redirectData', self.redirect_data)
        self._add_to_dictionary(dictionary, 'renderingData', self.rendering_data)
        self._add_to_dictionary(dictionary, 'showData', self.show_data)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MerchantAction, self).from_dictionary(dictionary)
        if 'actionType' in dictionary:
            self.action_type = dictionary['actionType']
        if 'formFields' in dictionary:
            if not isinstance(dictionary['formFields'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['formFields']))
            self.form_fields = []
            for formFields_element in dictionary['formFields']:
                formFields_value = PaymentProductField()
                self.form_fields.append(formFields_value.from_dictionary(formFields_element))
        if 'redirectData' in dictionary:
            if not isinstance(dictionary['redirectData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectData']))
            value = RedirectData()
            self.redirect_data = value.from_dictionary(dictionary['redirectData'])
        if 'renderingData' in dictionary:
            self.rendering_data = dictionary['renderingData']
        if 'showData' in dictionary:
            if not isinstance(dictionary['showData'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['showData']))
            self.show_data = []
            for showData_element in dictionary['showData']:
                showData_value = KeyValuePair()
                self.show_data.append(showData_value.from_dictionary(showData_element))
        return self
