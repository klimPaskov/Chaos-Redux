# Event 006 sourced portrait integration handoff

Date: 2026-07-22
Owner: parent integration agent

## Policy enforced

Grounded Event 006 countries use attributed real male people or authentic
archive material. Generated leaders are permitted only for a country that the
accepted registry explicitly classifies as truly fictional and high-chaos.
None of the current 206 candidate rows qualifies for that exception. Missing
grounded identities block the package; no generated or generic substitute is
accepted.

Real portraits follow one fixed pipeline: unchanged attributed master,
explicit head-and-shoulders crop, deterministic identity-preserving HOI4
leader finish, visual comparison against the skill-local vanilla references,
and `156x210` DDS conversion. ImageGen is not used to reconstruct or stylize a
real face.

## Integrated tranche

The authoritative ledger is
`docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/manifest.md`.
It records twenty-four sourced and visually reviewed treatments and exact
runtime hashes. A later active-vanilla-character ownership sweep rejects three
of those treatments for Event 006 runtime use: Konrad Adenauer, Franz Ritter
von Epp, and Edmund Ironside are already recruited by GER or ENG. Their files
remain evidence pending different sourced replacements and do not clear their
packages. Luigi Rizzo remains ownership-safe because vanilla uses his name only
for ship-production lines, not a character or portrait.
This pass added and wired:

- Saunders Lewis for the Welsh civic-leader token;
- Josef Harpe for the Rhenish river-command token;
- Heinrich Held for the Bavarian civic-leader token; and
- Franz Ritter von Epp for the Bavarian emergency-command token; this treatment
  is retained but rejected after the later active-vanilla-character sweep.

Earlier work in the same ledger covers Cornwall, Flanders, Wallonia, Frisia,
Scotland, Corsica, Sardinia, Sicily, the Middle Volga, Assyria, and Sokoto.
Naum Faiq and Agha Petros have reviewable treatments but no runtime DDS because
both died before 1936. David Kalakaua Kawananakoa remains rejected because the
available scan cannot survive an identity-preserving finish.

The Rupprecht of Bavaria and Josef Friedrich Matthes DDS files remain
byte-locked at their user-approved hashes. Epp is not an admissible Event 006
identity because vanilla owns him as an active GER character.

## Advisor and commander asset boundary

Event 006 defines no advisor, high-command, officer-corps, dossier, commander
miniature, or `_small` portrait asset. The obsolete runtime and archived
dossier derivatives, sprite registrations, and `army.small` consumers were
removed. Commanders use only full `156x210` leader portraits.

## Validation evidence

- 24 treatment-ledger runtime rows decode as RGBA `156x210`, match their
  processed PNG pixel-for-pixel, and match the ledger SHA-256 values. Conversion
  fidelity does not override the three active-character ownership rejections.
- All 413 sprites across the 22 Event 006 GFX files have unique names and
  existing textures.
- Event 006 has zero `_small` DDS files and zero portrait-small consumers.
- Event 006 has zero female character declarations and no remaining active
  `salvatore_licata` reference.
- The four new western masters match their locally recorded archive hashes;
  two initially mistyped hash strings in the research manifest and handoff
  were corrected to the actual 64-character SHA-256 values.
- Both touched localisation files retain UTF-8 BOM encoding.

## Admission and remaining blockers

No package is re-admitted by this asset tranche. The compile-time Event 006
content-attestation set remains empty.

- IW-002 Wales still lacks a sourced military commander.
- IW-001 Scotland requires a different sourced male commander because vanilla
  recruits Edmund Ironside for ENG.
- IW-008 Rhineland and IW-009 Bavaria require different sourced male route
  identities because vanilla recruits Konrad Adenauer and Franz Ritter von Epp
  for GER. Protected Matthes and Rupprecht, Josef Harpe, and Heinrich Held remain
  valid within their respective rosters.
- IW-004 Brittany, IW-006 Wallonia, IW-010 Saar, IW-018 Sardinia, IW-043
  Middle Volga, IW-058 Assyria, IW-093 Asante, IW-098 Sokoto, IW-179
  Micronesia, and IW-184 California retain one or more unresolved grounded
  leadership roles and remain fail-closed.
