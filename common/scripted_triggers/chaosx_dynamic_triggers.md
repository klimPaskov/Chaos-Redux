# chaosx_dynamic_triggers

This file documents reusable cross-system scripted triggers defined in `common/scripted_triggers/chaosx_dynamic_triggers.txt`. Subsystem-private APIs belong beside their owning system even when several files inside that system call them.

## Reuse guidance

Use this registry only for triggers with demonstrated call-site breadth across unrelated systems or event families. Reusable logic confined to one subsystem belongs in that subsystem's scripted-trigger files and dedicated reference documentation.

## Table of contents

- [is_desert_state](#is_desert_state)
- [is_special_chaos_country](#is_special_chaos_country)
- [is_actual_nonhuman_country](#is_actual_nonhuman_country)

## is_desert_state

State-scope trigger. Returns true for the maintained list of desert states used by shared event and map logic.

The list is an explicit state-ID registry because the game does not expose a shared desert-region collection for this mechanic. Each state appears once so callers receive the same boolean result without duplicate alternatives.

When adding a state, update this trigger and record the consuming event or system in its documentation. Do not replace the list with an event-local desert classifier.

## is_special_chaos_country

Country-scope trigger. Returns true for system actors and special scenario countries that should not be treated like normal civilian societies.

Current coverage includes:

- `ZZZ` / original `ZZZ` outbreak countries
- dynamic zombie outbreak countries
- weaponized zombie outbreak countries
- `REV` and countries with original tag `REV`
- communist rebel-state flags
- `ZIN`
- countries using the `The Holy Realm` cosmetic tag
- countries using the `The Great Mandala` or `The Silent Mandala` Holy Realm identity cosmetic tags
- countries with the Holy Realm active marker
- Germany Mengele civil-war and post-coup state markers
- active Fury actor countries
- `DTH` / original `DTH` / countries with the Death country marker
- `DHO` / original `DHO` / countries with the Event 018 cave-country marker
- Event 014 cannibal warlord countries
- the unified Event 014 country
- the transformed Event 014 Wendigo country
- Event 019 derivative countries through
  `is_infantry_spawn_derivative_country`. A human claimant breakaway requires
  the derivative marker, claimant marker, positive claimant UID,
  ordinary-family sentinel, and no nonhuman marker. A nonhuman family host
  requires the derivative and nonhuman markers, a positive registered family
  ID, parent-isolation proof, and public-package proof. Future registered
  families therefore need no classifier list edit.
- The fixed Event 016 `KRG` country and any host transformed by proven
  institutional capture. Hosted Directorates remain ordinary countries.
- Event 020 `RTA` Rat Nation and `RTX` Rat King actors through the shared
  `black_plague_rat_country` and `black_plague_rat_king_country` markers. Both
  are special actors and are excluded from ordinary human-host logic.

## is_actual_nonhuman_country

Country-scope trigger. Returns true only for countries that should currently be treated as actually nonhuman rather than merely unusual or scenario-specific.

Current coverage includes:

- `ZZZ` / original `ZZZ` outbreak countries
- dynamic zombie outbreak countries
- weaponized zombie outbreak countries
- Wendigo outbreak flags or the Wendigo cosmetic tag
- `ZIN`
- `DTH` / original `DTH` / countries with the Death country marker
- `DHO` / original `DHO` / countries with the Event 018 cave-country marker
- the transformed Event 014 Wendigo country; ordinary cannibal warlords and the ordinary unified country remain human
- Event 019 derivatives through
  `is_infantry_spawn_nonhuman_derivative_country`, which requires the nonhuman
  marker, positive registered family ID, parent-isolation proof, and
  public-package proof; claimant-only human breakaways remain special without
  being classified as nonhuman
- Event 016 Kruger sovereignties only after an explicit machine, clone-only,
  engineered-biological, or alien-government population transition. A human
  Kruger State remains special without being classified as nonhuman.
- Event 020 `RTA` Rat Nation and `RTX` Rat King actors through the shared
  `black_plague_rat_country` and `black_plague_rat_king_country` markers. Their
  plague immunity and non-human forces depend on this classification.

The current Event 019 registry/scenario v4 reaudit is clean for both shared
classifier routes. Neither trigger contains a zombie, ghost, golem, or future
provider list, and neither classifier contributes to a parent event's actor,
stage, evolution, super-event, or world-end state.
