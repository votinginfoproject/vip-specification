ContactInformation
==================

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:doc:`ElectionAdministration <election_administration>`, :doc:`Office <office>`,
:doc:`Person <person>`, :doc:`Source <source>`). ContactInformation has an optional attribute
``identifier``, which allows the feed to refer back to the original identifier for the information
(e.g. if the contact information came from a CSV, ``identifier`` may refer to a row ID).

.. include:: ../../tables/elements/contact_information.rst

