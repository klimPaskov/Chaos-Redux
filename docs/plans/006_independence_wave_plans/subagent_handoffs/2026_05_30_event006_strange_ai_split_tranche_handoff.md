# Event 006 Strange AI Split Tranche Handoff

Scope: close the documented gap where strange Event 006 releases had only a generic broad AI strategy after the Sealed Dossier and strange focus follow-through tranche.

## Files changed

- `common/ai_strategy/006_independence_wave.txt`
- `docs/events/006_independence_wave.md`

No flag assets, country setup files, country history files, Event 005 files, or `gfx/flags` files were edited.

## Implemented AI strategy split

The previous `independence_wave_strange_package_containment` strategy now only applies before the strange route is publicly revealed. It also reacts to the sealed archive audit and active containment review flags, not only package type.

New broad AI postures:

- `independence_wave_strange_contained_recovery`
  - active for `independence_wave_strange_contained`, `independence_wave_sealed_registry_closed`, or contained recovery focus flags
  - prioritizes restraint, civilian recovery, infrastructure, support equipment, and moderate defense
- `independence_wave_strange_revealed_escalation`
  - active for `chaosx_iw_strange_revealed` when containment has not succeeded
  - prioritizes army buildup, infantry/artillery production, division-template XP spending, and reduced war restraint

The AI strategy constants remain file-local `@` constants, matching the existing Event 006 AI strategy pattern.

## Documentation

`docs/events/006_independence_wave.md` now records that strange AI posture is split between pre-reveal containment, contained public-registry recovery, and revealed unmarked-ministry escalation.

## Validation

- Brace balance:
  - `common/ai_strategy/006_independence_wave.txt`: clean
  - `docs/events/006_independence_wave.md`: clean
- No unsupported less-than-or-equal / greater-than-or-equal operators in the touched files.
- `git diff --check -- common/ai_strategy/006_independence_wave.txt docs/events/006_independence_wave.md`: clean.
- `git status --short -- gfx/flags common/countries history/countries`: no output.

## Simplifications, omissions, and blockers

- This is a broad AI strategy split only. It does not add full strange country packages, strange formables, strange super-event triggers, or final strange assets.
- It does not add target-specific diplomacy against nearby states because there is not yet a complete strange world-threat or impossible-diplomacy system.
