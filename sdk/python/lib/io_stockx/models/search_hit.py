# coding: utf-8

"""
    StockX API

    PRERELEASE API - Subject to change before release. Provides access to StockX's public services, allowing end users to query for product and order information.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from io_stockx.models.search_hit_media import SearchHitMedia  # noqa: F401,E501
from io_stockx.models.search_hit_searchable_traits import SearchHitSearchableTraits  # noqa: F401,E501


class SearchHit(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'brand': 'str',
        'thumbnail_url': 'str',
        'media': 'SearchHitMedia',
        'url': 'str',
        'release_date': 'str',
        'categories': 'list[str]',
        'product_category': 'str',
        'ticker_symbol': 'str',
        'style_id': 'str',
        'make': 'str',
        'model': 'str',
        'short_description': 'str',
        'gender': 'str',
        'colorway': 'str',
        'price': 'int',
        'description': 'str',
        'highest_bid': 'str',
        'total_dollars': 'str',
        'lowest_ask': 'str',
        'last_sale': 'str',
        'sales_last_72': 'int',
        'deadstock_sold': 'int',
        'quality_bid': 'int',
        'active': 'int',
        'new_release': 'str',
        'searchable_traits': 'SearchHitSearchableTraits',
        'object_id': 'str',
        'annual_high': 'str',
        'annual_low': 'str',
        'deadstock_range_low': 'str',
        'deadstock_range_high': 'str',
        'average_deadstock_price': 'str',
        'change_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'brand': 'brand',
        'thumbnail_url': 'thumbnail_url',
        'media': 'media',
        'url': 'url',
        'release_date': 'release_date',
        'categories': 'categories',
        'product_category': 'product_category',
        'ticker_symbol': 'ticker_symbol',
        'style_id': 'style_id',
        'make': 'make',
        'model': 'model',
        'short_description': 'short_description',
        'gender': 'gender',
        'colorway': 'colorway',
        'price': 'price',
        'description': 'description',
        'highest_bid': 'highest_bid',
        'total_dollars': 'total_dollars',
        'lowest_ask': 'lowest_ask',
        'last_sale': 'last_sale',
        'sales_last_72': 'sales_last_72',
        'deadstock_sold': 'deadstock_sold',
        'quality_bid': 'quality_bid',
        'active': 'active',
        'new_release': 'new_release',
        'searchable_traits': 'searchable_traits',
        'object_id': 'objectID',
        'annual_high': 'annual_high',
        'annual_low': 'annual_low',
        'deadstock_range_low': 'deadstock_range_low',
        'deadstock_range_high': 'deadstock_range_high',
        'average_deadstock_price': 'average_deadstock_price',
        'change_value': 'change_value'
    }

    def __init__(self, name=None, brand=None, thumbnail_url=None, media=None, url=None, release_date=None, categories=None, product_category=None, ticker_symbol=None, style_id=None, make=None, model=None, short_description=None, gender=None, colorway=None, price=None, description=None, highest_bid=None, total_dollars=None, lowest_ask=None, last_sale=None, sales_last_72=None, deadstock_sold=None, quality_bid=None, active=None, new_release=None, searchable_traits=None, object_id=None, annual_high=None, annual_low=None, deadstock_range_low=None, deadstock_range_high=None, average_deadstock_price=None, change_value=None):  # noqa: E501
        """SearchHit - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._brand = None
        self._thumbnail_url = None
        self._media = None
        self._url = None
        self._release_date = None
        self._categories = None
        self._product_category = None
        self._ticker_symbol = None
        self._style_id = None
        self._make = None
        self._model = None
        self._short_description = None
        self._gender = None
        self._colorway = None
        self._price = None
        self._description = None
        self._highest_bid = None
        self._total_dollars = None
        self._lowest_ask = None
        self._last_sale = None
        self._sales_last_72 = None
        self._deadstock_sold = None
        self._quality_bid = None
        self._active = None
        self._new_release = None
        self._searchable_traits = None
        self._object_id = None
        self._annual_high = None
        self._annual_low = None
        self._deadstock_range_low = None
        self._deadstock_range_high = None
        self._average_deadstock_price = None
        self._change_value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if brand is not None:
            self.brand = brand
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if media is not None:
            self.media = media
        if url is not None:
            self.url = url
        if release_date is not None:
            self.release_date = release_date
        if categories is not None:
            self.categories = categories
        if product_category is not None:
            self.product_category = product_category
        if ticker_symbol is not None:
            self.ticker_symbol = ticker_symbol
        if style_id is not None:
            self.style_id = style_id
        if make is not None:
            self.make = make
        if model is not None:
            self.model = model
        if short_description is not None:
            self.short_description = short_description
        if gender is not None:
            self.gender = gender
        if colorway is not None:
            self.colorway = colorway
        if price is not None:
            self.price = price
        if description is not None:
            self.description = description
        if highest_bid is not None:
            self.highest_bid = highest_bid
        if total_dollars is not None:
            self.total_dollars = total_dollars
        if lowest_ask is not None:
            self.lowest_ask = lowest_ask
        if last_sale is not None:
            self.last_sale = last_sale
        if sales_last_72 is not None:
            self.sales_last_72 = sales_last_72
        if deadstock_sold is not None:
            self.deadstock_sold = deadstock_sold
        if quality_bid is not None:
            self.quality_bid = quality_bid
        if active is not None:
            self.active = active
        if new_release is not None:
            self.new_release = new_release
        if searchable_traits is not None:
            self.searchable_traits = searchable_traits
        if object_id is not None:
            self.object_id = object_id
        if annual_high is not None:
            self.annual_high = annual_high
        if annual_low is not None:
            self.annual_low = annual_low
        if deadstock_range_low is not None:
            self.deadstock_range_low = deadstock_range_low
        if deadstock_range_high is not None:
            self.deadstock_range_high = deadstock_range_high
        if average_deadstock_price is not None:
            self.average_deadstock_price = average_deadstock_price
        if change_value is not None:
            self.change_value = change_value

    @property
    def name(self):
        """Gets the name of this SearchHit.  # noqa: E501


        :return: The name of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchHit.


        :param name: The name of this SearchHit.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def brand(self):
        """Gets the brand of this SearchHit.  # noqa: E501


        :return: The brand of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this SearchHit.


        :param brand: The brand of this SearchHit.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this SearchHit.  # noqa: E501


        :return: The thumbnail_url of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this SearchHit.


        :param thumbnail_url: The thumbnail_url of this SearchHit.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def media(self):
        """Gets the media of this SearchHit.  # noqa: E501


        :return: The media of this SearchHit.  # noqa: E501
        :rtype: SearchHitMedia
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this SearchHit.


        :param media: The media of this SearchHit.  # noqa: E501
        :type: SearchHitMedia
        """

        self._media = media

    @property
    def url(self):
        """Gets the url of this SearchHit.  # noqa: E501


        :return: The url of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SearchHit.


        :param url: The url of this SearchHit.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def release_date(self):
        """Gets the release_date of this SearchHit.  # noqa: E501


        :return: The release_date of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this SearchHit.


        :param release_date: The release_date of this SearchHit.  # noqa: E501
        :type: str
        """

        self._release_date = release_date

    @property
    def categories(self):
        """Gets the categories of this SearchHit.  # noqa: E501


        :return: The categories of this SearchHit.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this SearchHit.


        :param categories: The categories of this SearchHit.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def product_category(self):
        """Gets the product_category of this SearchHit.  # noqa: E501


        :return: The product_category of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """Sets the product_category of this SearchHit.


        :param product_category: The product_category of this SearchHit.  # noqa: E501
        :type: str
        """

        self._product_category = product_category

    @property
    def ticker_symbol(self):
        """Gets the ticker_symbol of this SearchHit.  # noqa: E501


        :return: The ticker_symbol of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._ticker_symbol

    @ticker_symbol.setter
    def ticker_symbol(self, ticker_symbol):
        """Sets the ticker_symbol of this SearchHit.


        :param ticker_symbol: The ticker_symbol of this SearchHit.  # noqa: E501
        :type: str
        """

        self._ticker_symbol = ticker_symbol

    @property
    def style_id(self):
        """Gets the style_id of this SearchHit.  # noqa: E501


        :return: The style_id of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        """Sets the style_id of this SearchHit.


        :param style_id: The style_id of this SearchHit.  # noqa: E501
        :type: str
        """

        self._style_id = style_id

    @property
    def make(self):
        """Gets the make of this SearchHit.  # noqa: E501


        :return: The make of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this SearchHit.


        :param make: The make of this SearchHit.  # noqa: E501
        :type: str
        """

        self._make = make

    @property
    def model(self):
        """Gets the model of this SearchHit.  # noqa: E501


        :return: The model of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this SearchHit.


        :param model: The model of this SearchHit.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def short_description(self):
        """Gets the short_description of this SearchHit.  # noqa: E501


        :return: The short_description of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this SearchHit.


        :param short_description: The short_description of this SearchHit.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def gender(self):
        """Gets the gender of this SearchHit.  # noqa: E501


        :return: The gender of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this SearchHit.


        :param gender: The gender of this SearchHit.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def colorway(self):
        """Gets the colorway of this SearchHit.  # noqa: E501


        :return: The colorway of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._colorway

    @colorway.setter
    def colorway(self, colorway):
        """Sets the colorway of this SearchHit.


        :param colorway: The colorway of this SearchHit.  # noqa: E501
        :type: str
        """

        self._colorway = colorway

    @property
    def price(self):
        """Gets the price of this SearchHit.  # noqa: E501


        :return: The price of this SearchHit.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SearchHit.


        :param price: The price of this SearchHit.  # noqa: E501
        :type: int
        """

        self._price = price

    @property
    def description(self):
        """Gets the description of this SearchHit.  # noqa: E501


        :return: The description of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SearchHit.


        :param description: The description of this SearchHit.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def highest_bid(self):
        """Gets the highest_bid of this SearchHit.  # noqa: E501


        :return: The highest_bid of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._highest_bid

    @highest_bid.setter
    def highest_bid(self, highest_bid):
        """Sets the highest_bid of this SearchHit.


        :param highest_bid: The highest_bid of this SearchHit.  # noqa: E501
        :type: str
        """

        self._highest_bid = highest_bid

    @property
    def total_dollars(self):
        """Gets the total_dollars of this SearchHit.  # noqa: E501


        :return: The total_dollars of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._total_dollars

    @total_dollars.setter
    def total_dollars(self, total_dollars):
        """Sets the total_dollars of this SearchHit.


        :param total_dollars: The total_dollars of this SearchHit.  # noqa: E501
        :type: str
        """

        self._total_dollars = total_dollars

    @property
    def lowest_ask(self):
        """Gets the lowest_ask of this SearchHit.  # noqa: E501


        :return: The lowest_ask of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._lowest_ask

    @lowest_ask.setter
    def lowest_ask(self, lowest_ask):
        """Sets the lowest_ask of this SearchHit.


        :param lowest_ask: The lowest_ask of this SearchHit.  # noqa: E501
        :type: str
        """

        self._lowest_ask = lowest_ask

    @property
    def last_sale(self):
        """Gets the last_sale of this SearchHit.  # noqa: E501


        :return: The last_sale of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._last_sale

    @last_sale.setter
    def last_sale(self, last_sale):
        """Sets the last_sale of this SearchHit.


        :param last_sale: The last_sale of this SearchHit.  # noqa: E501
        :type: str
        """

        self._last_sale = last_sale

    @property
    def sales_last_72(self):
        """Gets the sales_last_72 of this SearchHit.  # noqa: E501


        :return: The sales_last_72 of this SearchHit.  # noqa: E501
        :rtype: int
        """
        return self._sales_last_72

    @sales_last_72.setter
    def sales_last_72(self, sales_last_72):
        """Sets the sales_last_72 of this SearchHit.


        :param sales_last_72: The sales_last_72 of this SearchHit.  # noqa: E501
        :type: int
        """

        self._sales_last_72 = sales_last_72

    @property
    def deadstock_sold(self):
        """Gets the deadstock_sold of this SearchHit.  # noqa: E501


        :return: The deadstock_sold of this SearchHit.  # noqa: E501
        :rtype: int
        """
        return self._deadstock_sold

    @deadstock_sold.setter
    def deadstock_sold(self, deadstock_sold):
        """Sets the deadstock_sold of this SearchHit.


        :param deadstock_sold: The deadstock_sold of this SearchHit.  # noqa: E501
        :type: int
        """

        self._deadstock_sold = deadstock_sold

    @property
    def quality_bid(self):
        """Gets the quality_bid of this SearchHit.  # noqa: E501


        :return: The quality_bid of this SearchHit.  # noqa: E501
        :rtype: int
        """
        return self._quality_bid

    @quality_bid.setter
    def quality_bid(self, quality_bid):
        """Sets the quality_bid of this SearchHit.


        :param quality_bid: The quality_bid of this SearchHit.  # noqa: E501
        :type: int
        """

        self._quality_bid = quality_bid

    @property
    def active(self):
        """Gets the active of this SearchHit.  # noqa: E501


        :return: The active of this SearchHit.  # noqa: E501
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SearchHit.


        :param active: The active of this SearchHit.  # noqa: E501
        :type: int
        """

        self._active = active

    @property
    def new_release(self):
        """Gets the new_release of this SearchHit.  # noqa: E501


        :return: The new_release of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._new_release

    @new_release.setter
    def new_release(self, new_release):
        """Sets the new_release of this SearchHit.


        :param new_release: The new_release of this SearchHit.  # noqa: E501
        :type: str
        """

        self._new_release = new_release

    @property
    def searchable_traits(self):
        """Gets the searchable_traits of this SearchHit.  # noqa: E501


        :return: The searchable_traits of this SearchHit.  # noqa: E501
        :rtype: SearchHitSearchableTraits
        """
        return self._searchable_traits

    @searchable_traits.setter
    def searchable_traits(self, searchable_traits):
        """Sets the searchable_traits of this SearchHit.


        :param searchable_traits: The searchable_traits of this SearchHit.  # noqa: E501
        :type: SearchHitSearchableTraits
        """

        self._searchable_traits = searchable_traits

    @property
    def object_id(self):
        """Gets the object_id of this SearchHit.  # noqa: E501


        :return: The object_id of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this SearchHit.


        :param object_id: The object_id of this SearchHit.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def annual_high(self):
        """Gets the annual_high of this SearchHit.  # noqa: E501


        :return: The annual_high of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._annual_high

    @annual_high.setter
    def annual_high(self, annual_high):
        """Sets the annual_high of this SearchHit.


        :param annual_high: The annual_high of this SearchHit.  # noqa: E501
        :type: str
        """

        self._annual_high = annual_high

    @property
    def annual_low(self):
        """Gets the annual_low of this SearchHit.  # noqa: E501


        :return: The annual_low of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._annual_low

    @annual_low.setter
    def annual_low(self, annual_low):
        """Sets the annual_low of this SearchHit.


        :param annual_low: The annual_low of this SearchHit.  # noqa: E501
        :type: str
        """

        self._annual_low = annual_low

    @property
    def deadstock_range_low(self):
        """Gets the deadstock_range_low of this SearchHit.  # noqa: E501


        :return: The deadstock_range_low of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._deadstock_range_low

    @deadstock_range_low.setter
    def deadstock_range_low(self, deadstock_range_low):
        """Sets the deadstock_range_low of this SearchHit.


        :param deadstock_range_low: The deadstock_range_low of this SearchHit.  # noqa: E501
        :type: str
        """

        self._deadstock_range_low = deadstock_range_low

    @property
    def deadstock_range_high(self):
        """Gets the deadstock_range_high of this SearchHit.  # noqa: E501


        :return: The deadstock_range_high of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._deadstock_range_high

    @deadstock_range_high.setter
    def deadstock_range_high(self, deadstock_range_high):
        """Sets the deadstock_range_high of this SearchHit.


        :param deadstock_range_high: The deadstock_range_high of this SearchHit.  # noqa: E501
        :type: str
        """

        self._deadstock_range_high = deadstock_range_high

    @property
    def average_deadstock_price(self):
        """Gets the average_deadstock_price of this SearchHit.  # noqa: E501


        :return: The average_deadstock_price of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._average_deadstock_price

    @average_deadstock_price.setter
    def average_deadstock_price(self, average_deadstock_price):
        """Sets the average_deadstock_price of this SearchHit.


        :param average_deadstock_price: The average_deadstock_price of this SearchHit.  # noqa: E501
        :type: str
        """

        self._average_deadstock_price = average_deadstock_price

    @property
    def change_value(self):
        """Gets the change_value of this SearchHit.  # noqa: E501


        :return: The change_value of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._change_value

    @change_value.setter
    def change_value(self, change_value):
        """Sets the change_value of this SearchHit.


        :param change_value: The change_value of this SearchHit.  # noqa: E501
        :type: str
        """

        self._change_value = change_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchHit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other