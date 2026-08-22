# Chemical First-Exposure Adaptation

## Overview

Chemical first-use surprise belongs to the defender's adaptation state. A validated chemical release can magnify the immediate disruption and casualties in its exact target state when the victim has no prior chemical-exposure awareness. It does not grant a national combat buff to the attacker.

The canonical implementation is `cbrn_dispatch_apply_first_exposure_shock` in `common/scripted_effects/cbrn_consequence_effects.txt`. Every supported chemical route reaches it only through `cbrn_dispatch_chemical_consequences` after target, payload, protection, and route receipts have been accepted.

## First exposure

An unprepared victim receives the full first-exposure multipliers from `cbrn_chemical_first_use`:

- disruption: 150% of the prepared action value;
- military casualties: 140%;
- civilian casualties: 130%;
- a fourteen-day national adaptation penalty through `cbrn_first_chemical_shock_idea`.

Real high protection lowers the immediate multipliers to 115%, 112%, and 110%. Prior confirmed world use lowers them to 125%, 118%, and 115%, representing warnings learned from foreign use without treating unrelated countries as already exposed.

After the first accepted exposure, the victim receives permanent `cbrn_chemical_exposure_awareness`. Later attacks still pass through the full chemical consequence pipeline but do not repeat the first-exposure shock.

## Consequences and protection

The shock modifies only the immediate disruption and casualty calculations. It does not alter payload debit, contamination, medical saturation, mask loss, evidence, attribution, death recording, confirmed-use history, Condemnation, treaty breach, sanctions, or retaliation classification.

Protective equipment and the target country's readiness remain active inputs. Headquarters warning, gas-mask reserves, issue policy, decontamination, and medical preparation therefore reduce the harm of first exposure through the same shared calculation used for later attacks.

## Assets and wiring

- idea icon: `gfx/interface/ideas/stage_6_chemical_delivery/cbrn_first_chemical_shock.dds`;
- sprite: `GFX_idea_cbrn_first_chemical_shock` in `interface/cbrn_chemical_delivery.gfx`;
- idea: `cbrn_first_chemical_shock_idea` in `common/ideas/cbw_ideas.txt`;
- localisation: `localisation/english/cbrn_chemical_delivery_l_english.yml`.

No attacker-side first-use idea or icon is active.

## Future extensions

If a current-version native warning-sharing hook exposes exact participating allies, chemical awareness could be shared through that proven relationship. It must not be approximated with a world pulse or faction-wide estimator.
