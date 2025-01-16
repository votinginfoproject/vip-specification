# Updating the Documentation

To update the documentation, you must update the yaml files. These will then be used to 
update the RST and HTML files automatically.

## How does the automatic RST and HTML generation work?

When you run the command, `make build`, a series of scripts in the repo are triggered
that will generate the RST files.

The `vip.py` script performs the following actions:

1. Normalizing the YAML
2. Generating the RST files.

Following that, the `sphinx-autobuild` library is used to generate the HTML and preview the results locally.

## Main Sections in the YAML

For each element, there are a few key sections to be aware of:

1. **Names** - Each page has a name
2. **Description** - Each page has a description, shared by XML and CSV
3. **Posts** - Used for displaying example data
4. **Extensions** - Some elements add unique fields to a pre-defined base of fields.
5. **Skip Element Designation** - Some elements should be skipped for the CSV documentation.
6. **Sub Types** - Defines elements that are subsumed under another.
7. **Primary Type Designation** - An override for sub-types.
8. **Tags** - Used for displaying tables for each field and associated information

More detailed explanations are below.

## Names

The XML name for the elements is defined with `_name`. The CSV is `csv-header-name`.

Example:

```
_name: BallotMeasureContest
csv-header-name: ballot_measure_contest
```

## Descriptions

Descriptions are written in this way:

```
description: |-
  The BallotMeasureContest provides information about a ballot measure before the voters, including
  summary statements on each side. Extends :ref:`$$$-contest-base`.
```

In this example, a hyperlink is added by including `:ref: \`$$$-contest-base\``. 

Notice how even on CSV, the name will be shown as "BallotMeasureContest".
There is currently no description field specific to CSV.


## Posts

When sharing example data either for CSV or XML, posts are used. For XML, the label is simply `post`.
CSV posts are `csv-post`:

```
post: |-
  .. code-block:: xml
     :linenos:

     <BallotMeasureContest id="bmc30001">
        <BallotSelectionIds>bms30001a bms30001b</BallotSelectionIds>
        <BallotTitle>
           <Text language="en">State of the State</Text>
           <Text language="es">Estado del Estado.</Text>
        </BallotTitle>
        <ElectoralDistrictId>ed60129</ElectoralDistrictId>
        <Name>Referendum on Virginia</Name>
        <ConStatement label="bmc30001con">
           <Text language="en">This is no good.</Text>
           <Text language="es">Esto no es bueno.</Text>
        </ConStatement>
        <EffectOfAbstain label="bmc30001abs">
           <Text language="en">Nothing will happen.</Text>
           <Text language="es">Nada pasará.</Text>
        </EffectOfAbstain>
        <ProStatement label="bmc30001pro">
           <Text language="en">Everything will be great.</Text>
           <Text language="es">Todo va a estar bien.</Text>
        </ProStatement>
        <Type>referendum</Type>
     </BallotMeasureContest>

  .. _competing initiatives: http://ballotpedia.org/Laws_governing_the_initiative_process_in_California#Competing_initiatives
  ```

```
csv-post: |-
  .. code-block:: csv-table
     :linenos:


      id,abbreviation,ballot_selection_ids,ballot_sub_title,ballot_title,elecoral_district_id,electorate_specification,external_identifier_type,external_identifier_othertype,external_identifier_value,has_rotation,name,sequence_order,vote_variation,other_vote_variation,con_statement,effect_of_abstain,full_text,info_uri,passage_threshold,pro_statement,summary_text,type,other_type
      bmc0001,HB2,bs001 bs002 bs003,Raising levy for School Bond,School Bond Issue,ed001,all registered voters,,54,false,School Bond,42,majority,,This is no good.,No effect,A measure to do raise funds for etc etc,www.ballotmeasure.com,two-thirds,Everything will be great.,It’s a referendum about school funding,referendum,
```

## Extensions

Some element types, like contests, share a number of fields. To avoid duplication, we created bases that 
contain all shared elements. When an element extends a base, the base's information will be
appended to the unique fields. In the HTML, it appears as a separate section at the bottom 
of the documentation.

```
extends:
- ContestBase
```

## Sub Types

When an element is defined as a sub-type, we should expect the sub-type to appear 
on the same pages as its super-type and on the table of contents as such.

This behavior is useful for XML, where elements are nested.

These are indicated in this manner:
```
_sub_types:
- Department
- ElectionNotice
- VoterService
```

## Primary Type Designation

To define an element as a primary type overrides the sub-type designation
in a given format, either CSV or XML.

Since CSV doesn't have nested elements, this is useful behavior.

```primary_type_on: csv```


## Skip Element Designation

Using this label means a given element is skipped when generating a specified 
version of the documentation. For example, the HoursOpen element only exists
in the XML version of the documentation. Thus:

```skip_element_on: csv```

## Tags

Tags have their own labels:

1. Names
2. Descriptions
3. Type
4. Repeating
5. Required Status
6. Error Behavior
7. Skip On

Each element has multiple tags, with each group separated by "- ":

```
tags:
- _name: StartTime
  csv-header-name: start_time
  csv-type: TimeWithZone
  description: The time at which this place opens.
  
  type: TimeWithZone
- _name: EndTime
  csv-header-name: end_time
  csv-type: TimeWithZone
  description: The time at which this place closes.
  
  type: TimeWithZone
```

The `name` and `description` labels are straightforward. The others are detailed below:

### Type

The type describes the data type for the tag. Can indicate a sub-element (in XML) or enumeration:

1. `xs:string`
2. `xs:anyURI`
3. `xs:boolean`
4. `xs:IDREFS` - A reference to another entity
5. `xs:integer`
6. Sub-elements:
     - `InternationalizedText`
     - `ExternalIdentifiers`
     - `HTMLColorString`
     - `ContactInformation`
      - Sub-elements will show up as hyperlinks to those pages.

### Required Status

If a tag has `required: true`, the `Required` field will reflect that.
If it is absent, that field will default to `Optional`.

### Error Behavior

If needed, a custom message about error handling can be added with the label `error`. This policy would then
be included precisely as entered in the YAML:

`error: [insert custom, hardcoded error behavior here]`

This is useful when an item becomes required when certain criteria are met (e.g. `StartHouseNumber`), or when the absence
of a value would result in a default value being assumed.

### Skip On

Some tags should only be visible on either XML or CSV. 
Thus by defining `skip_on: csv`, the tag will not be generated for the CSV version
of the documentation.






