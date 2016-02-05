# VIP Release Notes

This document includes release notes for the [VIP Spec][vip] for versions
5.1 and later.

## Version 5.1

### Spec Changes
* Use `xs:IDREFS` instead of `xs:IDREF maxOccurs="unbounded"`.
  * The [NIST][nist_spec] also moved to `xs:IDREFS`
  * This was also causing some issues with Java code generation.
  * Issue [#298](https://github.com/votinginfoproject/vip-specification/issues/298)
* Support for city-level wildcarding
  * Issue [#299](https://github.com/votinginfoproject/vip-specification/issues/299)

### Other Changes
* Updated sample feed
  * Describe support for party affiliations in open primary elections
    * Issue [#268](https://github.com/votinginfoproject/vip-specification/issues/268)
  * Include use of multiple offices on a single `CandidateSelection`
    * President and Vice-President [PR
  #303](https://github.com/votinginfoproject/vip-specification/pull/303)

## Version 5.0

### Spec Changes
* Convergence with the [NIST][nist_spec] election results reporting spec.
  * Issue [#42](https://github.com/votinginfoproject/vip-specification/issues/42)
  * Objects and enumerations also used in the NIST ERR spec include:
    * `CandidatePreElectionStatus` and `CandidatePostElectionStatus`
    * `DistrictType`
    * `IdentifierType`
    * `BallotSelectionBase`, `BallotMeasureSelection`, and `CandidateSelection`
    * `BallotStyle`
    * `Candidate`
    * `ContactInformation`
    * `ContestBase`, `BallotMeasureContest`, `CandidateContest`, `PartyContest`,
      and `RetentionContest`
    * `HoursOpen` (known in NIST ERR as `Schedule`)
    * `Office`
    * `OrderedContest`
    * `Party`
    * `Person`
* Object identifiers use the `xs:ID` and `xs:IDREF` types instead of `xs:string`
  or `xs:integer`. The `xs:ID` type [has certain restrictions and
  requirements](http://books.xmlschemata.org/relaxng/ch19-77151.html) beyond
  normal strings or integers.
  * Issue [#45](https://github.com/votinginfoproject/vip-specification/issues/45)
* Add support for internationalization (i.e. multiple languages) via the
  `InternationalizedText` type.
  * Issues [#39](https://github.com/votinginfoproject/vip-specification/issues/39) and
  [#77](https://github.com/votinginfoproject/vip-specification/issues/77)
* Per-`Precinct` links to `BallotStyle` elements.
  * Issue [#94](https://github.com/votinginfoproject/vip-specification/issues/94)
* Per-`PollingLocation` lat/lng support.
  * Issue [#165](https://github.com/votinginfoproject/vip-specification/issues/165)
* Structured hours for open and close times.
  * Issue [#21](https://github.com/votinginfoproject/vip-specification/issues/21)
* `StreetSegment` objects can use `IncludesAllAddresses` instead of magic values
  for `StartHouseNumber` and `EndHouseNumber`.
  * Issue [#235](https://github.com/votinginfoproject/vip-specification/issues/235)
* Support for various voter services being handled by different departments or
  people.
  * Issue [#63](https://github.com/votinginfoproject/vip-specification/issues/63)
* Better handling of apartments/multi-home lots.
  * Issue [#22](https://github.com/votinginfoproject/vip-specification/issues/22)
* Removed `NonHouseAddress` since it was only used in one element now.
  * Issue [#258](https://github.com/votinginfoproject/vip-specification/issues/259)
* All elements which specify web links are now of type `xs:anyURI` (instead of
  `xs:string`) and end in `Uri` instead of `Url`.
  * Issue [#87](https://github.com/votinginfoproject/vip-specification/issues/87)
* Structured handling of types for `ElectoralDistrict` and `Locality`, replacing
  the free-form string with an enumeration.
  * Issues [#30](https://github.com/votinginfoproject/vip-specification/issues/30) and
  [#129](https://github.com/votinginfoproject/vip-specification/issues/129)
* The odd/even/both type (`OebType`) is now lower-case only.
  * Issue [#46](https://github.com/votinginfoproject/vip-specification/issues/46)
* The `yesNoEnum` has been replaced by `xs:boolean`, meaning those field can
  only take the values `true` or `false` (case-sensitive).
  * Issue [#66](https://github.com/votinginfoproject/vip-specification/issues/66)

### Other Changes
* The spec and all content in this repository is available under a [Creative
  Commons Attribution 4.0 International](LICENSE.md) license.
  * Issue [#269](https://github.com/votinginfoproject/vip-specification/pulls/269)
* The spec generally uses a [Venetian
  Blind](http://www.oracle.com/technetwork/java/design-patterns-142138.html) design philosophy.
  * Issue [#113](https://github.com/votinginfoproject/vip-specification/issues/113)
* Created a
  [spec style
  guide](https://github.com/votinginfoproject/vip-specification/blob/vip5/STYLEGUIDE.md).
  * Issues [#41](https://github.com/votinginfoproject/vip-specification/issues/41),
  [#74](https://github.com/votinginfoproject/vip-specification/issues/74),
  [#75](https://github.com/votinginfoproject/vip-specification/issues/75),
  [#83](https://github.com/votinginfoproject/vip-specification/issues/83),
  [#85](https://github.com/votinginfoproject/vip-specification/issues/85),
  [#106](https://github.com/votinginfoproject/vip-specification/issues/106),
  [#126](https://github.com/votinginfoproject/vip-specification/issues/126),
  [#136](https://github.com/votinginfoproject/vip-specification/issues/136), and
  [#138](https://github.com/votinginfoproject/vip-specification/issues/138)
* Created a
  [CONTRIBUTING
  guide](https://github.com/votinginfoproject/vip-specification/blob/vip5/CONTRIBUTING.md).
  * Issue [#93](https://github.com/votinginfoproject/vip-specification/issues/93)
* Documentation is now stored in YAML files, which are then used to generate the
  RST and HTML documentation
  * Issue [#255](https://github.com/votinginfoproject/vip-specification/issues/255)
* Created an approval process for pull requests.
  * Issue [#117](https://github.com/votinginfoproject/vip-specification/issues/117)
* The sample feed now uses UTF-8.
  * Issue [#81](https://github.com/votinginfoproject/vip-specification/issues/81)

[nist_spec]: https://github.com/usnistgov/Voting
[vip]: https://github.com/votinginfoproject/vip-specification
