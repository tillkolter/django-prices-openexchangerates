# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_prices_openexchangerates', '0002_auto_20160329_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversionrate',
            name='rate',
            field=models.DecimalField(decimal_places=12, max_digits=20, verbose_name='Conversion rate'),
        ),
        migrations.AlterField(
            model_name='conversionrate',
            name='to_currency',
            field=models.CharField(choices=[('DZD', 'Algerian Dinar'), ('QAR', 'Qatari Rial'), ('BGN', 'Bulgarian Lev'), ('BMD', 'Bermudan Dollar'), ('PAB', 'Panamanian Balboa'), ('BWP', 'Botswanan Pula'), ('TZS', 'Tanzanian Shilling'), ('VND', 'Vietnamese Dong'), ('KYD', 'Cayman Islands Dollar'), ('UAH', 'Ukrainian Hryvnia'), ('AWG', 'Aruban Florin'), ('GIP', 'Gibraltar Pound'), ('BYR', 'Belarusian Ruble (pre-2016)'), ('ALL', 'Albanian Lek'), ('XPD', 'Palladium Ounce'), ('BYN', 'Belarusian Ruble'), ('DJF', 'Djiboutian Franc'), ('THB', 'Thai Baht'), ('BND', 'Brunei Dollar'), ('NIO', 'Nicaraguan C\xf3rdoba'), ('LAK', 'Laotian Kip'), ('SYP', 'Syrian Pound'), ('MAD', 'Moroccan Dirham'), ('MZN', 'Mozambican Metical'), ('YER', 'Yemeni Rial'), ('ZAR', 'South African Rand'), ('NPR', 'Nepalese Rupee'), ('CRC', 'Costa Rican Col\xf3n'), ('AED', 'United Arab Emirates Dirham'), ('GBP', 'British Pound Sterling'), ('HUF', 'Hungarian Forint'), ('LSL', 'Lesotho Loti'), ('XDR', 'Special Drawing Rights'), ('TTD', 'Trinidad and Tobago Dollar'), ('SBD', 'Solomon Islands Dollar'), ('KPW', 'North Korean Won'), ('ANG', 'Netherlands Antillean Guilder'), ('RWF', 'Rwandan Franc'), ('NOK', 'Norwegian Krone'), ('MOP', 'Macanese Pataca'), ('INR', 'Indian Rupee'), ('MXN', 'Mexican Peso'), ('TJS', 'Tajikistani Somoni'), ('COP', 'Colombian Peso'), ('TMT', 'Turkmenistani Manat'), ('HNL', 'Honduran Lempira'), ('FJD', 'Fijian Dollar'), ('ETB', 'Ethiopian Birr'), ('PEN', 'Peruvian Nuevo Sol'), ('BZD', 'Belize Dollar'), ('ILS', 'Israeli New Sheqel'), ('DOP', 'Dominican Peso'), ('GGP', 'Guernsey Pound'), ('MDL', 'Moldovan Leu'), ('BSD', 'Bahamian Dollar'), ('ZMK', 'Zambian Kwacha (pre-2013)'), ('JEP', 'Jersey Pound'), ('AUD', 'Australian Dollar'), ('SRD', 'Surinamese Dollar'), ('KRW', 'South Korean Won'), ('VEF', 'Venezuelan Bol\xedvar Fuerte'), ('ZMW', 'Zambian Kwacha'), ('LTL', 'Lithuanian Litas'), ('CDF', 'Congolese Franc'), ('RUB', 'Russian Ruble'), ('MMK', 'Myanma Kyat'), ('PLN', 'Polish Zloty'), ('MKD', 'Macedonian Denar'), ('TOP', 'Tongan Pa?anga'), ('GNF', 'Guinean Franc'), ('WST', 'Samoan Tala'), ('ERN', 'Eritrean Nakfa'), ('BAM', 'Bosnia-Herzegovina Convertible Mark'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verdean Escudo'), ('PGK', 'Papua New Guinean Kina'), ('SOS', 'Somali Shilling'), ('STD', 'S\xe3o Tom\xe9 and Pr\xedncipe Dobra'), ('BTC', 'Bitcoin'), ('IRR', 'Iranian Rial'), ('XPF', 'CFP Franc'), ('XOF', 'CFA Franc BCEAO'), ('MTL', 'Maltese Lira'), ('NZD', 'New Zealand Dollar'), ('LVL', 'Latvian Lats'), ('ARS', 'Argentine Peso'), ('RSD', 'Serbian Dinar'), ('BHD', 'Bahraini Dinar'), ('SDG', 'Sudanese Pound'), ('XAU', 'Gold Ounce'), ('NAD', 'Namibian Dollar'), ('GHS', 'Ghanaian Cedi'), ('EGP', 'Egyptian Pound'), ('BOB', 'Bolivian Boliviano'), ('DKK', 'Danish Krone'), ('LBP', 'Lebanese Pound'), ('AOA', 'Angolan Kwanza'), ('KHR', 'Cambodian Riel'), ('MYR', 'Malaysian Ringgit'), ('LYD', 'Libyan Dinar'), ('JOD', 'Jordanian Dinar'), ('SAR', 'Saudi Riyal'), ('XPT', 'Platinum Ounce'), ('HKD', 'Hong Kong Dollar'), ('CHF', 'Swiss Franc'), ('SVC', 'Salvadoran Col\xf3n'), ('MRO', 'Mauritanian Ouguiya'), ('HRK', 'Croatian Kuna'), ('XAF', 'CFA Franc BEAC'), ('XAG', 'Silver Ounce'), ('VUV', 'Vanuatu Vatu'), ('UYU', 'Uruguayan Peso'), ('PYG', 'Paraguayan Guarani'), ('ZWL', 'Zimbabwean Dollar'), ('NGN', 'Nigerian Naira'), ('EEK', 'Estonian Kroon'), ('MWK', 'Malawian Kwacha'), ('LKR', 'Sri Lankan Rupee'), ('PKR', 'Pakistani Rupee'), ('SZL', 'Swazi Lilangeni'), ('MNT', 'Mongolian Tugrik'), ('AMD', 'Armenian Dram'), ('UGX', 'Ugandan Shilling'), ('JMD', 'Jamaican Dollar'), ('SCR', 'Seychellois Rupee'), ('SHP', 'Saint Helena Pound'), ('AFN', 'Afghan Afghani'), ('TRY', 'Turkish Lira'), ('BDT', 'Bangladeshi Taka'), ('HTG', 'Haitian Gourde'), ('MGA', 'Malagasy Ariary'), ('PHP', 'Philippine Peso'), ('LRD', 'Liberian Dollar'), ('XCD', 'East Caribbean Dollar'), ('CZK', 'Czech Republic Koruna'), ('TWD', 'New Taiwan Dollar'), ('BTN', 'Bhutanese Ngultrum'), ('MUR', 'Mauritian Rupee'), ('IDR', 'Indonesian Rupiah'), ('ISK', 'Icelandic Kr\xf3na'), ('SEK', 'Swedish Krona'), ('CUP', 'Cuban Peso'), ('CLF', 'Chilean Unit of Account (UF)'), ('BBD', 'Barbadian Dollar'), ('KMF', 'Comorian Franc'), ('GMD', 'Gambian Dalasi'), ('IMP', 'Manx pound'), ('CUC', 'Cuban Convertible Peso'), ('GEL', 'Georgian Lari'), ('CLP', 'Chilean Peso'), ('EUR', 'Euro'), ('KZT', 'Kazakhstani Tenge'), ('OMR', 'Omani Rial'), ('BRL', 'Brazilian Real'), ('KES', 'Kenyan Shilling'), ('USD', 'United States Dollar'), ('AZN', 'Azerbaijani Manat'), ('MVR', 'Maldivian Rufiyaa'), ('IQD', 'Iraqi Dinar'), ('GYD', 'Guyanaese Dollar'), ('KWD', 'Kuwaiti Dinar'), ('BIF', 'Burundian Franc'), ('SGD', 'Singapore Dollar'), ('UZS', 'Uzbekistan Som'), ('CNY', 'Chinese Yuan'), ('SLL', 'Sierra Leonean Leone'), ('TND', 'Tunisian Dinar'), ('FKP', 'Falkland Islands Pound'), ('KGS', 'Kyrgystani Som'), ('RON', 'Romanian Leu'), ('GTQ', 'Guatemalan Quetzal'), ('JPY', 'Japanese Yen')], db_index=True, max_length=3, unique=True, verbose_name='To'),
        ),
    ]
