# coding: utf-8

"""
    ECommerce Checkout Flow API

    Registration, Address Information, Delivery Options, Payment, Confirmation

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class CheckoutTotals(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, currency=None, product_sub_totals=None, sub_totals=None, total=None):
        """
        CheckoutTotals - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'currency': 'str',
            'product_sub_totals': 'list[ProductSubTotal]',
            'sub_totals': 'list[CheckoutSubTotal]',
            'total': 'str'
        }

        self.attribute_map = {
            'currency': 'currency',
            'product_sub_totals': 'productSubTotals',
            'sub_totals': 'subTotals',
            'total': 'total'
        }

        self._currency = currency
        self._product_sub_totals = product_sub_totals
        self._sub_totals = sub_totals
        self._total = total


    @property
    def currency(self):
        """
        Gets the currency of this CheckoutTotals.


        :return: The currency of this CheckoutTotals.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this CheckoutTotals.


        :param currency: The currency of this CheckoutTotals.
        :type: str
        """

        self._currency = currency

    @property
    def product_sub_totals(self):
        """
        Gets the product_sub_totals of this CheckoutTotals.


        :return: The product_sub_totals of this CheckoutTotals.
        :rtype: list[ProductSubTotal]
        """
        return self._product_sub_totals

    @product_sub_totals.setter
    def product_sub_totals(self, product_sub_totals):
        """
        Sets the product_sub_totals of this CheckoutTotals.


        :param product_sub_totals: The product_sub_totals of this CheckoutTotals.
        :type: list[ProductSubTotal]
        """

        self._product_sub_totals = product_sub_totals

    @property
    def sub_totals(self):
        """
        Gets the sub_totals of this CheckoutTotals.


        :return: The sub_totals of this CheckoutTotals.
        :rtype: list[CheckoutSubTotal]
        """
        return self._sub_totals

    @sub_totals.setter
    def sub_totals(self, sub_totals):
        """
        Sets the sub_totals of this CheckoutTotals.


        :param sub_totals: The sub_totals of this CheckoutTotals.
        :type: list[CheckoutSubTotal]
        """

        self._sub_totals = sub_totals

    @property
    def total(self):
        """
        Gets the total of this CheckoutTotals.


        :return: The total of this CheckoutTotals.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this CheckoutTotals.


        :param total: The total of this CheckoutTotals.
        :type: str
        """

        self._total = total

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
