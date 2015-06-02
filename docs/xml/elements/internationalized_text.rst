InternationalizedText
=====================

`InternationalizedText` has an optional attribute
``identifier``, which allows the feed to refer back to the original identifier for the information
(e.g. if the contact information came from a CSV, ``identifier`` may refer to a row ID).

+------------+--------------------+--------------+-----------+----------------------+-------------------------------+
| Tag        | Data Type          | Required?    | Repeats?  |Description           |Error Handling                 |
|            |                    |              |           |                      |                               |
+============+====================+==============+===========+======================+===============================+
| Text       |:doc:`LanguageString| **Required** | Repeats   |Contains the          |At least one valid `Text` must |
|            |<language_string>`  |              |           |translations of a     |be present for                 |
|            |                    |              |           |particular string of  |`InternationalizedText` to be  |
|            |                    |              |           |text.                 |valid. If no valid `Text` is   |
|            |                    |              |           |                      |present, the implementation is |
|            |                    |              |           |                      |required to ignore the         |
|            |                    |              |           |                      |`InternationalizedText`        |
|            |                    |              |           |                      |element.                       |
|            |                    |              |           |                      |                               |
|            |                    |              |           |                      |                               |
+------------+--------------------+--------------+-----------+----------------------+-------------------------------+
