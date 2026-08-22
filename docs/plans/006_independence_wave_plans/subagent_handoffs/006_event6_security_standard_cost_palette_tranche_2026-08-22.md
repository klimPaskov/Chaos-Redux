# Event 006 security-standard cost palette tranche

Date: 2026-08-22

Status: **implemented locally; parent review required**.

## Scope and decision

The bounded family was the five Event 006 callers of the shared `independence_wave_cost_security_standard_factory` selector: `independence_wave_form01_coordinate_maritime_defence`, `independence_wave_form02_build_air_warning_chain`, `independence_wave_form04_coordinate_corridor_security`, `independence_wave_hbx_screen_federal_arsenals`, and `independence_wave_udm_establish_industrial_emergency_command`.

The factory variant exposed five cost groups (manpower, Army Experience, infantry equipment, support equipment, and a civilian-factory reservation), while the shared security payment and trigger already define a complete four-group palette. The narrow fix reuses the existing four-group selector and removes only the four light civilian-factory reservations attached to the formable and HBX callers. The UDM caller had no matching `civilian_factory_use` modifier, so its fix is selector-only.

## Changed files and identifiers

- `common/decisions/006_independence_wave_form01_02_04_decisions.txt:253,345,437`
  - FORM01 maritime defence, FORM02 air-warning chain, and FORM04 corridor security now use `independence_wave_cost_security_standard`.
  - Removed each `civilian_factory_use = @CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT` modifier.
- `common/decisions/006_independence_wave_pacific_decisions.txt:50`
  - HBX federal arsenals now use `independence_wave_cost_security_standard`.
  - Removed its light civilian-factory reservation modifier.
- `common/decisions/006_independence_wave_udm_decisions.txt:154`
  - UDM industrial emergency command now uses `independence_wave_cost_security_standard`.
- No constants, scripted triggers/effects, AI blocks, or localisation files required edits because the existing four-group implementation already matches these callers.

## Before and after behavior

Before, four callers reserved one light civilian factory for the project and all five displayed the factory-bearing cost string. After, each caller displays and gates on exactly manpower, Army Experience, infantry equipment, and support equipment, and pays through the unchanged `independence_wave_decision_pay_security_standard` effect. The decisions retain their existing visibility, progression/package gates, durations, completion/remove/cancel effects, and AI weights. No pre-event decision surface was touched.

The canonical trigger remains `can_pay_independence_wave_security_standard_cost` at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:272-277`; it checks the same four groups. The canonical payment remains `independence_wave_decision_pay_security_standard` at `common/scripted_effects/006_independence_wave_decision_effects.txt:209-221`; it consumes the same four groups. The existing icon-first normal and blocked strings remain `independence_wave_cost_security_standard`, `_tooltip`, and `_blocked` at `localisation/english/006_independence_wave_decisions_l_english.yml:36,89-90`.

## Audit notes

Severity P1 resolved for this family: no in-scope caller now exposes or reserves a fifth cost group. The legacy factory localisation triplet remains available for other deferred cost-palette work but has no active decision source caller after this tranche.

Lifecycle remains intact: the five actions retain their existing package/formable activation, one-active-project gates, durations, completion effects, remove effects, cancellation, and timeout ownership. These are decision/project surfaces rather than standalone mission families, so no mission owner, region, duplicate-mission, or new cleanup contract was introduced.

AI is unchanged (`high` for the three formable decisions, `urgent` for HBX, and the existing war-sensitive `high` modifier for UDM). This keeps source behavior stable while the player-facing gate and payment now agree. A dedicated `chaosx_ai_probability_auditor` route was not callable in this runtime. Direct `hoi4.probability_inspect` was attempted with `decision_ai_will_do` and the scoped decision source, but the MCP call timed out after 180 seconds; no quantitative balance claim is made.

## Validation and evidence

- Scoped search confirms no decision source still references `independence_wave_cost_security_standard_factory`.
- Scoped search confirms all five changed blocks retain the security-standard custom trigger and security-standard completion payment.
- `git diff --check` passed for the three changed decision files.
- Read-only GUI evidence was refreshed because Event 006 has decision-owned status presentation: `hoi4.gui_inspect` artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b5634e8af85ad8a251440db7966d1d7c8b9cbb5b6ad3912c767e0d606887549/d54ede9acc35a56ef9530d14bf66407e5d06c2dc8cfd77395c98b388bf788e48/gui-inspect.3bdd0ec978e13a84.json`; `hoi4.gui_render` artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d245b460614d138be4d724b8fbbe4c0c3ae510648ae12c90abf3733e231c13/04c99b404466dc431b2586531f62d5b28e046013c2c482b043b5514027360303/independence_wave_status_window-full.svg`.
- GUI evidence is fidelity-only, not a patch validation: the workspace reports 2,000 retained global graph diagnostics, 75 visible overlaps, and 12 unresolved elements. No GUI rewrite was in scope or performed.

## Deferred broader redesign and uncertainty

Other Event 006 families still exceed four cost groups, including reclamation, border ultimatum, integration, breakaway sponsorship, strategic, and Pacific strategic palettes. They require separate accepted balance decisions and are intentionally untouched. Removing the factory reservation changes project capacity pressure for these five post-event callers; parent review should confirm that the accepted design treats the factory reservation as optional rather than a required fifth spendable group. If factory pressure must remain, a separate four-group palette decision is needed; this tranche does not invent or add one.

Skipped live HOI4 validation because agents must not launch the game; live consumer validation remains user-owned.
