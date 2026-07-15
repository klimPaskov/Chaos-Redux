# Event 006 formable identity tag collision audit

Date: 2026-07-15

## Result

The reviewed FORM-01 through FORM-04 cosmetic identity tags are:

| Family | Identity | Tag | Result |
| --- | --- | --- | --- |
| FORM-01 | Celtic Congress | `KCX` | clear |
| FORM-02 | North Atlantic Union | `NUX` | clear |
| FORM-03 | Confederation of the Low Countries | `LCX` | clear |
| FORM-04 | Rhenish League | `RLX` | clear |

`CCX` is not clear. Event 6 package `IW-055` already reserves it in the accepted
206-row candidate registry, so FORM-01 was migrated to `KCX` before gameplay
registration. No fallback or shared namespace remains.

## Scope checked

The audit checked:

- every resolved and proposed tag in the Event 6 candidate registry;
- vanilla country tags, aliases, cosmetic identities, localisation namespaces,
  history filenames, flag filenames, and scripted tag uses;
- all 122 installed Hearts of Iron IV Workshop directories;
- the three sibling local mods and the linked music mod surface;
- loose country definitions, tag aliases, cosmetic assignments, localisation,
  gameplay references, history files, and flag filenames;
- all eight installed Workshop ZIP archives, including the one archive with tag
  surfaces.

The external loose-file scan and archive scan found no `KCX`, `NUX`, `LCX`, or
`RLX` collision. The current Chaos Redux occurrences are the reviewed Event 6
identity implementations and asset packages themselves.

## Reservation rule

These identifiers are cosmetic identity inputs for their exact formable
families. They must not be assigned to a country package, another formable,
another route, or another event. A future installed-mod audit that finds a new
external definition blocks that identity until a repository-wide remap is
reviewed.
