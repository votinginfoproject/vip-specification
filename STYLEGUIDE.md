# Coding Styles


## Text Files

This section applies to all text files in the repository (XML, HTML,
Markdown, etc).

* The file encoding should be UTF-8.

* Line endings should be LF (as opposed to CRLF).  Git should handle this
  automatically for you via the project [`.gitattributes`](.gitattributes) file.

* Trailing white space should be removed from the end of lines.

* Spaces should be used instead of tabs.  See the file-type specific
  section for how many spaces should be used for indentations.

* Lines should adhere to a non-strict 100 character length limit.  Exceptions
  can be made for things like readability.  This guideline does not apply
  to the sample feed files (e.g. the XML and CSV sample files).


## XSD Styles

### Indentation

* Two-space indents should be used (e.g. in place of tabs).


### Casing

+ Attributes should be camelCased - The first letter of the second and subsequent words are capitalized.
+ Elements should be TitleCased (PascalCased) - The first letter of every word is capitalized.
+ Enumerations should be spinal-case - all lower case with spaces replaced with hyphens.


### Type Names

* Type names should only end in "Type" if _instances_ of the type correspond
  to types.  For example, instances of the "Candidate" type represent
  candidates rather than types of candidates.  In contrast, "OfficeTermType"
  instances correspond to the different types of office terms:

  ```xml
  <xs:simpleType name="OfficeTermType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="full-term" />
      <xs:enumeration value="unexpired-term" />
    </xs:restriction>
  </xs:simpleType>
  ```

* The names of abstract "base class" types (e.g. those with `abstract="true"`)
  should end in "Base" as a reminder that such types should not be
  instantiated directly.  For example--

  ```xml
  <xs:complexType name="ContestBase" abstract="true">
    <xs:sequence>
      <xs:element name="BallotSelectionId" type="xs:IDREF" minOccurs="0" maxOccurs="unbounded" />
      <xs:element name="ExternalIdentifiers" type="ExternalIdentifiers" minOccurs="0" />
      ...
  ```


### IDs

* A primary key ID should be an attribute with type "xs:ID" and name "id".
  For example,

    ```xml
    <xs:attribute name="id" type="xs:ID" use="required" />
    ```
  Note that this departs from the style used by [VSSC 1622.2][vssc_1622],
  where the name is "object_id".

* A reference to a primary key should have type "xs:IDREF".  The name
  of the element or attribute should normally end with the name of the type
  of the object being referenced, followed by "Id" (and made TitleCased or
  camelCased as appropriate).  For example,

    ```xml
    <xs:element name="ElectoralDistrictId" type="xs:IDREF" />
    ```
  If the type is abstract, the trailing "Base" should be removed prior
  to adding "Id".  For example,
    ```xml
    <!-- Instead of ContestBaseId. -->
    <xs:element name="ContestId" type="xs:IDREF" />
    ```


### Element/Attribute Property Ordering

Element and attribute properties should appear in the following order:

1. name
2. type
3. minOccurs
4. maxOccurs

Any attributes not listed above should appear after those listed.  Also,
a single space should separate the final attribute from the closing "`/>`".
For example--

```xml
<xs:attribute name="id" type="xs:ID" use="required" />
```

### Element/Attribute Ordering

Within a type, elements should be listed first, followed by attributes. Each
should be in alphabetical order, with only two exceptions:

1. If an element named `Foo` is an enumeration which contains a value
   `other`, then `OtherFoo` should be placed immediately after `Foo`.
2. If a pair of values represent a range and are named `StartFoo` and `EndFoo`,
   `EndFoo` should be placed after `StartFoo`.

E.g.,

```xml
<xs:element name="Foo">
  <xs:complexType>
    <xs:all>
      <xs:element name="Alpha" type="xs:string" />
      <xs:element name="Delta" type="xs:string" />
      <xs:element name="StartDate" type="xs:date" />
      <xs:element name="EndDate" type="xs:date" />
      <xs:element name="Type" type="SomeEnumValue" />
      <xs:element name="OtherType" type="xs:string" />
    </xs:all>
    <xs:attribute name="beta" type="xs:string" />
    <xs:attribute name="id" type="xs:ID" />
  </xs:complexType>
</xs:element>
```

With `EndDate` and `OtherType` removed, we see an ordering of `Alpha`, `Delta`,
`StartDate`, and `Type`. Once we place `EndDate` and `OtherType` back in we get
the proper ordering.

### Enumeration Ordering and "Other"

Enumeration values should be arranged alphabetically, except for "other",
which should appear last.

To support "other" values in an enumeration, include "other" as a value.
For example--

```xml
<xs:simpleType name="Color">
  <xs:restriction base="xs:string">
    <xs:enumeration value="blue" />
    <xs:enumeration value="green" />
    <xs:enumeration value="red" />
    <xs:enumeration value="other" />
  </xs:restriction>
</xs:simpleType>
```

Then, whenever using the type in an element named `[Name]`, add an element
named `Other[Name]` with type `xs:string`.  The value "other" for element
`[Name]` means to look at `Other[Name]` for the value.  For example--

```xml
<xs:element name="BallotColor" type="Color" minOccurs="0" />
<xs:element name="OtherBallotColor" type="xs:string" minOccurs="0" />
```


### Type Definitions: Global vs. Local

This subsection describes when a type definition should be "global"
(i.e. named and an immediate child of "xs:schema") versus
"local" (i.e. anonymous and nested within another component, aka in-lined).

Global might look like--

```xml
<xs:schema>
  <xs:complexType name="Person">
    <xs:element name="Name" type="xs:string" />
  </xs:complexType>
  ...
```

Local might look like--

```xml
<xs:element name="Person">
  <xs:complexType>
    <xs:element name="Name" type="xs:string" />
  </xs:complexType>
</xs:element>
```

Our approach is in the spirit of "Venetian Blind."  Define a type globally
if any of the following are true:

1. elements of the type are referenced by ID via `type="xs:IDREF"`.
   For example--

   ```xml
   <xs:element name="PrecinctId" type="xs:IDREF" />
   ```

2. elements of the type occur in more than one location within the
   root element.  For example--

   ```xml
   <xs:element name="Title" type="InternationalizedText" />
   <xs:element name="Subtitle" type="InternationalizedText" />
   ```

3. the type is an "enum" or other pattern-restricted string.  For example--

   ```xml
   <xs:simpleType name="OebEnum">
     <xs:restriction base="xs:string">
       <xs:enumeration value="odd" />
       <xs:enumeration value="even" />
       <xs:enumeration value="both" />
     </xs:restriction>
   </xs:simpleType>

   <xs:simpleType name="HtmlColorString">
     <xs:restriction base="xs:string">
       <xs:pattern value="[0-9a-f]{6}" />
     </xs:restriction>
   </xs:simpleType>
   ```


### Global Type Definition Ordering

Global type definitions should be ordered as follows:

1. Put global type definitions before the root element.

2. Group them in the following order: enumerations, other simple types,
   then complex types.

3. Within each of the groups in (2) above, order them alphabetically by name.
   When alphabetizing, view the names as words separated by spaces.
   For example, "VoteVariation" should come before "VoterServiceType"
   since "vote variation" comes before "voter service type" when the
   names are viewed as words.


## CSV Styles
To be determined


[vssc_1622]: http://grouper.ieee.org/groups/1622/groups/2/index.html
