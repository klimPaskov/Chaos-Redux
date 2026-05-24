# Event 005 focus duplicate payoff addendum

## Purpose

Several Event 005 focus pairs currently feel too similar because adjacent focuses give the same broad rewards. This addendum keeps the existing focus IDs, layout, base country setup, and route intent, but gives each focus a clearer job in play.

The goal is not to add more focus count. The goal is to make the existing branches read and play differently.

## Design Direction

### Ukraine military branch

- `ukr_soviet_collapse_officer_patronage_lists` should be about officer vetting and loyalty control. It should improve command reliability, expose patronage networks, and reduce the danger that foreign or Moscow-linked patrons own the officer corps.
- `ukr_soviet_collapse_general_staff_war_college` should be about professional training. It should improve doctrine, staff quality, and long-term army organization rather than handing out another generic equipment package.

Queued later: an officer-politics event can contrast a vetted but suspicious army with a professional staff-school army.

### Ukraine democratic branch

- `ukr_soviet_collapse_rural_deputy_bloc` should turn the grain and village path into parliamentary leverage. It should help stability and village legitimacy while reducing old-movement rural pressure.
- `ukr_soviet_collapse_minority_autonomy_statutes` should turn border and minority settlement into a legal shield against outside patrons. It should improve recognition, resilience, and cohesion without copying the rural-deputy reward.

Queued later: a Rada-versus-governor event can react to both rural votes and autonomy coverage.

### Baltic recognition and defense branch

- `baltic_soviet_collapse_baltic_recognition_dossier` should compile internal evidence: archives, casualty rolls, port records, legal continuity, and verified claims.
- `baltic_soviet_collapse_the_legal_front_abroad` should use that evidence abroad: recognition briefs, foreign legal pressure, and diplomatic legitimacy.
- `baltic_soviet_collapse_pan_baltic_war_room` should coordinate allied command and planning.
- `baltic_soviet_collapse_baltic_shield_doctrine` should harden the map with defensive doctrine, forts, and air defense.

Queued later: tie the Baltic dossier into Soviet counterclaim missions and add a Baltic defense objective if the branch still needs more active play.

### Don Host civil branch

- `DHC_stanitsa_mediation` should be civil law: settling disputes, stabilizing stanitsas, and preventing local guard autonomy from becoming private command.
- `DHC_stanitsa_oath_boards` should be military obligation: mustering riders, binding guards to the Host Circle, and improving readiness.

Queued later: add a small dispute event once the mediation and oath-board rewards are stable.

### MFR factory rivalry branch

- `MFR_builders_waste_steel` should be unilateral steel seizure. It should trade civilian recovery for weapons, arsenal quotas, and Soviet depot pressure.
- `MFR_civilian_factory_rivalry` should use CFR's existence as an active rivalry surface: contractor pressure, recognition leverage, and inter-factory competition.

Queued later: add a CFR counter-decision or event after the MFR-side rivalry is stable.

## Asset Notes

- Keep current base flags and country identities intact.
- Keep most existing focus icons, but the Baltic war room and DHC mediation should use distinct icons when available.
- If new icons are needed, route them through the normal icon workflow rather than using placeholders as final art.

## Balance Notes

- These focuses are branch differentiators, not capstones. Their rewards should be noticeable but smaller than route finishers.
- AI priorities should react to existing route state, war state, stability, and Soviet pressure rather than using only flat base weights.
- Do not add whole-world on-actions for this work.

## Validation Follow-Up

- Verify the named focus pairs no longer call identical reward stacks.
- Verify tooltip text describes the new in-world payoff clearly.
- Re-run a focus audit after implementation to check duplicate rewards, AI behavior, icon identity, and localisation.
- Use a decision/mission audit only if the implementation adds new focus-unlocked decisions.
