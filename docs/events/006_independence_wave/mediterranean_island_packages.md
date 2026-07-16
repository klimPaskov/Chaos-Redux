# Event 006 Mediterranean island packages

## Scope

This document owns the playable Event 006 implementation contract for:

| Package | Country | Gameplay tag | Depth | Anchor | Former host |
| --- | --- | --- | --- | --- | --- |
| IW-017 | Corsica | registered vanilla `COR` | Level 1 | state 1 | dynamic released owner, normally France |
| IW-018 | Sardinia | Event 006 tag `ARX` | Level 1 | state 114 | dynamic released owner, normally Italy |
| IW-019 | Sicily | Event 006 tag `ASX` | Level 2 | state 115 | dynamic released owner, normally Italy |

All three packages remain members of the Mediterranean and Iberia allocation
region and the Mediterranean Island League formable family. `COR` is reused
only when it is not living and still owns the vanilla `generic_focus` tree.
`COR`, `ARX`, and `ASX` then receive the full shared Event 006 framework. A
mod-provided meaningful COR tree fails the setup gate and rolls the release
back instead of being overwritten.

## Release and host-survival contract

The shared allocator owns reservation, collision handling, and synchronized
release. The country adapters begin only after that transaction has assigned:

- one unique anchor state to the new country;
- a dynamic former-host scope and ledger;
- a protected surviving state still owned by every living former host;
- Event 006 origin, package, region, depth, and archetype variables; and
- the exact force profile frozen for that package.

IW-017 receives only state 1, IW-018 only state 114, and IW-019 only state 115.
The packages do not take mainland French or Italian territory during release.
Sicily can later prepare claims on states 117 and 156 through its explicit Two
Sicilies dossier; the focus does not transfer or core those states and cleanup
removes the staged claims.

Final validation proves the anchor is still owned and controlled by the new
country and the former host still owns its protected state. A failed adapter
removes its missions, decisions, ideas, flags, variables, staged claims, and
Event 006-only Corsican characters before the shared release transaction
rolls back.

## Playable package identity

### IW-017 Corsica

Corsica begins with an exposed island-supply crisis and a Maritime Access
ledger. Customs, mountain roads, communes, former-host accounts, and the
government route all change that ledger and the shared Legitimacy,
Recognition, Capacity, Security, Instability, host, network, and league
values.

Because `COR` is a registered vanilla country, Event 006 does not edit its
country history. Vanilla COR has no unique national tree, so the adapter first
proves that the active tree is still `generic_focus`, then loads the complete
Event 006 framework and its five-focus Corsican extension. Cleanup restores
the generic tree and retires the four Event 006-only male characters. If any
other mod supplies COR with a meaningful tree, the proof fails before the
framework can replace it.

Government settlements:

- constitutional communes under Petru Santucci;
- traditional mountain communes under Petru Santucci;
- an emergency island-guard mandate under Pasquale Venturi; or
- a protected customs mandate under Petru Santucci.

The popular-council and radical-sovereignty shared routes are excluded for
this package. The Corsican decision family and the full framework use the same
locked route transaction and install the same package-specific government, so
neither surface can select a second route.

### IW-018 Sardinia

Sardinia begins with fragmented island authority and a Civic Cohesion ledger.
Municipal books, Cagliari shipping, mountain guards, former-host property, and
the island settlement build a reconstruction council able to govern the full
island.

Government settlements:

- an island constitution under Antioco Melis;
- a Sardinian labor compact under Antioco Melis;
- a crown consultative state under Vittorio Pala; or
- a mountain-guard directorate under Gavino Piras.

The patron-client and radical-sovereignty shared routes are excluded. The
country receives the full Event 006 focus framework plus a six-focus Sardinian
module. Its ambition remains island and league oriented; it does not inherit
the claims or identity of vanilla Sardinia-Piedmont.

### IW-019 Sicily

Sicily begins with contested port authority and a Port Authority ledger.
Palermo port books, interior grain routes, straits garrisons, island
administration, Italian property, and customs service determine whether the
state can sustain a Level 2 route.

Government settlements:

- a Palermo constitution under Sebastiano Restivo;
- a chambers-of-labor compact under Sebastiano Restivo;
- a Two Sicilies crown council under Vincenzo Lanza;
- a straits security directorate under Salvatore Licata; or
- a protected Mediterranean mandate under Sebastiano Restivo.

The radical-sovereignty shared route is excluded. The eight-focus Sicilian
module ends in a mutually exclusive choice between a staged Two Sicilies
dossier and a Mediterranean republic mandate. The dossier supplies claims
and an ambition incident, not free territory, cores, units, or an automatic
war. The republic route prepares the charter-driven league path.

## Forces and setup

The shared dynamic force transaction applies the exact frozen profile after
the roster proof succeeds:

| Package | Force profile | Military tradition | Navy | Air |
| --- | --- | ---: | --- | --- |
| IW-017 | coastal maritime | 53 | yes | no |
| IW-018 | coastal maritime | 52 | yes | no |
| IW-019 | regular defectors | 65 | yes | yes |

The force transaction scales with scenario intensity and available equipment.
Package decisions never create free formations, and repeated projects do not
award equipment or units. Baseline laws are civilian economy, export focus,
and volunteer only.

## Decisions and missions

Each country receives a founding mission plus serialized timed projects.
Projects require the shared administration, security, diplomatic, or
strategic costs; infrastructure projects also occupy civilian factories.
Losing the capital, entering an invalid host state, or interrupting a project
applies the package failure transaction instead of a passive checklist reward.

Corsican projects cover Ajaccio customs, the mountain post road, coastal
commune registration, four government settlements, and the maritime congress.
Sardinian projects cover municipal ledgers, Cagliari shipping, mountain
guards, four government settlements, and the maritime congress. Sicilian
projects cover Palermo port books, grain routes, straits garrisons, Italian
property, five government settlements, and the maritime congress.

Only one package project can run at a time. The congress decision also obeys
the shared formable-operation lock and does not itself proclaim FORM-05.

## Focus integration

Corsica's five-focus extension begins from the Event 006 capital-administration
focus and covers customs, the mountain road, communes, the French maritime
accounts, and FORM-05 delegation authority.

The full framework contains a separate right-side island module for Sardinia
and Sicily. Sardinia has six country focuses; Sicily has eight and a final
mutually exclusive ambition split. The country-specific branch gates use exact
package triggers, so ARX cannot see ASX content and neither can expose the
Corsican framework extension.

## Ideas and lifecycle

Each package begins with one crisis idea, replaces it with one mature state
compact when its ledger reaches the stable threshold, and installs exactly one
government-route idea after route selection. Scripted effects remove every
other package route idea before each swap.

The icon map uses eleven explicit Mediterranean semantic families rather than
nonexistent or generic picture tokens: island crisis, state compact,
constitutional assembly, mountain communes, labor compact, crown council,
island guard, patron customs, and the three FORM-05 lifecycle states.

## AI behavior

Origin-locked AI profiles prioritize island infantry, support equipment,
artillery, trains, convoys, infrastructure, dockyards, and coastal defenses.
Founding governments strongly avoid new wars unless the former-host ledger
reports a severe threat. Civic governments retain diplomatic restraint;
emergency governments raise army and coastal-defense priorities. The Sicilian
restoration dossier reduces, but does not remove, war restraint and never
issues a scripted declaration. A ratified FORM-05 carrier prioritizes convoys,
dockyards, coastal defense, and continued league restraint.

All values live under `independence_wave_mediterranean_ai` in
`common/script_constants/006_independence_wave_mediterranean_constants.txt`.

## Flag and portrait contract

Corsica deliberately reuses its registered vanilla flag family. Sardinia and
Sicily require historical, ImageGen-authored flat flag designs rather than
flag artwork or generic ideological overlays. The final route map must state
whether one historical national design is deliberately retained by every
government or which researched historical design belongs to each engine
ideology filename. Every generated master, processed ladder, source citation,
prompt, and hash belongs in the Event 006 asset manifest.

Every live leader and commander portrait depicts one adult man in a distinctive
1930s HOI4 painted head-and-shoulders composition. The package uses eight full
156x210 leader/commander textures. Its three corps commanders follow vanilla's
supported large-only army-portrait pattern; no optional army-small dossier is
declared. The six political advisers have no portrait block, custom dossier,
or advisor sprite dependency.

## Asset wiring

Final package assets are registered through dedicated Event 006 `.gfx` files:

- eight large leader/commander portrait sprites under
  `gfx/leaders/006_independence_wave/`;
- eight focus families plus shine sprites under
  `gfx/interface/goals/006_independence_wave/`;
- eight package decision families under
  `gfx/interface/decisions/006_independence_wave/`;
- eight Mediterranean package idea families under
  `gfx/interface/ideas/006_independence_wave/`; and
- one package-neutral Mediterranean incident report image under
  `gfx/event_pictures/006_independence_wave/`.

FORM-05 owns its additional charter decisions, report image, emblem, lifecycle
ideas, and MIX flag ladder in its separate document and manifest.

## Validation scenarios

The package audit must cover at least:

1. FRA survives Corsica with its protected capital state while COR receives
   only state 1.
2. ITA survives simultaneous Sardinian and Sicilian releases while retaining
   the single protected state reserved before allocation.
3. COR is already living and is rerolled without any overwrite.
4. a dormant COR resolves to a non-generic focus tree supplied by another mod;
   package setup fails and rollback leaves that tree untouched.
5. ARX or ASX is living or externally reserved and is rerolled.
6. Event 5 reserves one of the anchors before the joint cluster transaction;
   the Event 6 candidate is rerolled before release.
7. every automatic wave count can use the three packages without duplicate
   anchors or tags;
8. all scenario intensities change territory/forces only and never bypass
   package readiness;
9. each government route installs one leader, party identity, route idea, and
   matching AI behavior;
10. all timed-project cancellation and package rollback paths remove their
   state; and
11. FORM-05 invitation, refusal, ratification, failure, and recovery preserve
    sovereign non-consenting islands.

## Future plans

- Add other researched island packages to FORM-05 through the same consent and
  maritime-connection contract.
- Add late diplomatic settlements with living French and Italian hosts without
  turning the host ledger into an automatic war generator.
- Expand the Sicilian dossier only after mainland state packages and their
  collision groups are implemented, so staged claims never pre-empt a future
  release candidate.
