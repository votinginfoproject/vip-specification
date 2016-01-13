internationalized_text.txt
==========================

InternationalizedText allows for support of multiple languages for a string.
InternationalizedText has an optional attribute label which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, label may refer to a row ID). Examples of InternationalizedText can be seen in:

* Any element that extends :ref:`single-xml-contest-base`

* Any element that extends :ref:`single-xml-ballot-selection-base`

* :ref:`single-xml-candidate`

* :ref:`single-xml-contact-information`

* :ref:`single-xml-election`

* :ref:`single-xml-election-administration`

* :ref:`single-xml-office`

* :ref:`single-xml-party`

* :ref:`single-xml-person`

* :ref:`single-xml-polling-location`

* :ref:`single-xml-source`

.. include:: ../../built_rst/tables/elements/internationalized_text.rst

LanguageString
--------------

LanguageString extends xs:string and can contain text from any language. LanguageString
has one required attribute, language, that must contain the 2-character `language code`_ for the
type of language LanguageString contains.

.. _`language code`: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

.. literalinclude:: ../../csv/example_files/internationalized_text.txt
   :linenos:
