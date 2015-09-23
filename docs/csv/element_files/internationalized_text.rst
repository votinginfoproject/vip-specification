internationalized_text.txt
==========================

InternationalizedText allows for support of multiple languages for a string.
InternationalizedText has an optional attribute label which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, label may refer to a row ID). Examples of InternationalizedText can be seen in:

* Any element that extends :doc:`ContestBase <contest_base>`

* Any element that extends :doc:`BallotSelection <ballot_selection>`

* :doc:`Candidate <candidate>`

* :doc:`ContactInformation <contact_information>`

* :doc:`Election <election>`

* :doc:`ElectionAdministration <election_administration>`

* :doc:`Office <office>`

* :doc:`Party <party>`

* :doc:`Person <person>`

* :doc:`PollingLocation <polling_location>`

* :doc:`Source <source>`

.. include:: ../../tables/elements/internationalized_text.rst

LanguageString
--------------

LanguageString extends xs:string and can contain text from any language. LanguageString
has one required attribute, language, that must contain the 2-character `language code`_ for the
type of language LanguageString contains.

.. _`language code`: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

.. literalinclude:: ../../csv/example_files/internationalized_text.txt
   :linenos:
