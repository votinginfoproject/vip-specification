.. This file is auto-generated.  Do not edit it by hand!

.. _xml-multi-internationalized-text:

InternationalizedText
=====================

``InternationalizedText`` allows for support of multiple languages for a string.
``InternationalizedText`` has an optional attribute ``label``, which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, ``label`` may refer to a row ID). Examples of ``InternationalizedText`` can be seen in:

* Any element that extends :doc:`ContestBase <contest_base>`

* Any element that extends :doc:`BallotSelectionBase <ballot_selection_base>`

* :doc:`Candidate <candidate>`

* :doc:`ContactInformation <contact_information>`

* :doc:`Election <election>`

* :doc:`ElectionAdministration <election_administration>`

* :doc:`Office <office>`

* :doc:`Party <party>`

* :doc:`Person <person>`

* :doc:`PollingLocation <polling_location>`

* :doc:`Source <source>`

+--------------+-------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type         | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===================+==============+==============+==========================================+==========================================+
| Text         | `LanguageString`_ | **Required** | Repeats      | Contains the translations of a           | At least one valid ``Text`` must be      |
|              |                   |              |              | particular string of text.               | present for ``InternationalizedText`` to |
|              |                   |              |              |                                          | be valid. If no valid ``Text`` is        |
|              |                   |              |              |                                          | present, the implementation is required  |
|              |                   |              |              |                                          | to ignore the ``InternationalizedText``  |
|              |                   |              |              |                                          | element.                                 |
+--------------+-------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _xml-multi-language-string:

LanguageString
--------------

``LanguageString`` extends xs:string and can contain text from any language. ``LanguageString``
has one required attribute, ``language``, that must contain the 2-character `language code`_ for the
type of language ``LanguageString`` contains.

.. _`language code`: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

.. code-block:: xml
   :linenos:

   <BallotTitle>
      <Text language="en">Retention of Supreme Court Justice</Text>
      <Text language="es">La retención de juez de la Corte Suprema</Text>
   </BallotTitle>
