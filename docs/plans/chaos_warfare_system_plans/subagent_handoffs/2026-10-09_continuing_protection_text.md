# Continuing hospital protection localisation alignment

Disposition: implemented within the parent-assigned text scope.
Acceptance basis: parent task of 2026-10-09 and the accepted continuing protection source review in `2026-10-09_continuing_protection_review.md`.
Parent retains final source integration, documentation integration and commit.
No index or commit action was taken.

## Changed files and keys

| File | Keys or identifiers |
| --- | --- |
| `localisation/english/cbrn_protection_l_english.yml` | `cbrn_protect_hospitals_and_utilities_complete_tt`; parent integration also updates `cbrn_protect_hospitals_and_utilities_desc` |
| `localisation/english/cbrn_designers_l_english.yml` | `cbrn_medical_respiratory_care_tt`, `cbrn_medical_antidote_production_tt`, `cbrn_value_respiratory_care_reduction`, `cbrn_value_burn_treatment_reduction`, `cbrn_value_antidote_reduction` |
| `common/scripted_localisation/cbrn_designer_value_localisation.txt` | `GetCbrnValueRespiratoryCareReduction`, `GetCbrnValueBurnTreatmentReduction`, `GetCbrnValueAntidoteReduction` |
| This handoff | Evidence and limitations |

Hospital completion previously mentioned protected capacity and initial saturation only.
It retains the payment condition, state name and existing duration getter, and adds: "Care provided during this time can reduce later chemical deaths, depending on existing protection and medical care."
No flat hospital death percentage is promised, because current equipment and care can remain on a protection-table plateau.

Respiratory completion previously promised unconditional 15% lower choking and continuing blister deaths.
Final wording is "In states controlled by this country, choking-agent deaths fall by up to [respiratory getter]% and continuing blister-agent deaths by up to [burn getter]%. The reduction depends on existing protection and medical care."
Antidote completion previously promised unconditional 15% lower nerve deaths.
Final wording is "In states controlled by this country, nerve-agent deaths fall by up to [antidote getter]%, depending on existing protection and medical care."
The actual YML uses the named This getters and retains green percentage formatting.

Each percentage getter calculates `(constant:cbrn_math.one - constant:cbrn_medical_designer_effect.<multiplier>) * constant:cbrn_math.percent_divisor` in its own temporary variable.
The three actual multiplier keys are `respiratory_care_choking_death_mult`, `burn_treatment_continuing_death_mult` and `antidote_nerve_death_mult`, all currently 0.85.
No constant namespace is interpolated directly into YML.
The existing direct trigger/value-key pattern is mirrored from `cbrn_protection_value_localisation.txt`.
Parent review aligned percentage conversion with the semantic `cbrn_math.percent_divisor` constant and added explicit `always = yes` after arithmetic in all three triggers.
Current 15% and substituted 20% source arithmetic cases were rerun after that correction, with consumer phrases unchanged.

## Audit and prose review

Missing keys: none among assigned keys and new getter results.
Duplicate keys: none among all six touched/new YML keys across English localisation.
Scripted localisation issues: static authored percentages were replaced with three constant-backed independent bindings.
Dynamic opportunities implemented: independent respiratory, burn and antidote percentages, so different future values cannot silently share one display.
No encoding concern remains in the two owned YML files.

Vagueness: the hospital tooltip omitted its continuing-care payoff, which is now stated as a conditional benefit.
Bloat and obvious explanation: no issue requiring unrelated deletion was found in the assigned passages.
Repetition: the respiratory and burn percentages require independent bindings despite currently matching values.
Overcomplication: current control eligibility leads both MIO tooltips, and the shared protection dependency uses one short clause or sentence.
Style-rule repair: categorical reduction promises became accurate upper bounds, without internal ledger, pulse, timing-window or update-history explanation.
There are no sourced or attributed quotations on the inspected surfaces.
Existing state/duration tokens and green formatting were preserved, and the literal 15% values were deliberately replaced by dynamic getters.
The parent-integrated hospital description covers a chemical emergency rather than requiring an incoming raid, matching the accepted contamination response route.
Cost rows, icons, other MIO and biological/vaccine text remain unchanged.

Cross-surface source search found assigned completion keys only in the hospital decision and the two MIO trait completion tooltips.
No event/detail/evolution/catalog prose change is required by these key changes.
No spreadsheet wording handoff is needed, and no workbook or export was edited.
No new mechanic or design-depth gap was introduced, so no improvement plan was written.

## Meaningful validation

Read actual continuing collector, event `.4`, respiratory/antidote exposure consumers, Burn Treatment helper and MIO/decision tooltip call sites.
The continuing collector applies current protection with paid hospital overlap and clamps combined additional care to the existing same-mask residual floor.
The tooltips avoid promising an additional reduction when that shared floor or the authored table plateau prevents one.
Source checks resolved the six touched/new keys uniquely and connected each new getter to its exact multiplier and result key.
A bounded arithmetic check executed the three authored set/subtract/multiply sequences against current constants, yielding 15 each.
An independent 0.80 multiplier fixture yielded 20 in each sequence, confirming that the displays derive the reduction rather than preserve a literal 15 claim.
These checks model getter arithmetic and references, not native engine execution or tooltip wrapping.

The parent confirmed there is no usable paired native tooltip render.
An earlier MIO inspect selected zero elements, while generic GUI/framework/graph renders do not prove these tooltips.
That failed capability was not retried here, because the parent established no corrected input that would address it.
Native wrapping and live percentage getter display remain visually unverified.
No HOI4 launch or log action was performed.
There are no unresolved wording decisions or gameplay simplifications in this text tranche.

## Reference evidence

Live reference_context, reference_search and reference_read succeeded.
Live source_lookup for the existing duration getter returned no definition from its workspace index, so the actual local file was read directly.
This index gap is not proof that the existing getter is absent.

| Source | Read lines | Revision |
| --- | --- | --- |
| `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` | 656-705 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` | 216-222 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md` | 1-34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |

The offline Localisation section explicitly permits temporary arithmetic in defined_text triggers and preserves those temporaries for the selected result key.
Installed documentation confirms scoped variables accept fixed-point constants with the constant prefix.
Vanilla `common/scripted_localisation/SEA_PRC_scripted_loc.txt:38-55` supplies a directly read arithmetic-in-trigger precedent.
Skills read and applied: chaos-redux-subagents, chaos-redux-decisions-missions and the shared prose guidance in chaos-redux-events.
