# Native warfare policy integration

`national_policy_warfare_effects.txt` and `../scripted_triggers/national_policy_warfare_triggers.txt` integrate the chemical, biological and nuclear native law slots with existing action owners.
Native law ids provide permission, while existing project, protection, readiness, target, custody and technical checks provide capability.
The combined `cbrn_use_policy` variable is a compatibility display/history value and grants no final action authority.

## Helper contract

| Helper | Scope and inputs | Result and side effects | Consumers |
| --- | --- | --- | --- |
| `national_policy_on_warfare_law_changed` | Country, temporary `national_policy_changed_family`, `national_policy_previous_value`, `national_policy_new_value` supplied by the law publisher | Preserves shared C/B policy peak and history, dispatches a C/B reservation breach only on broadening, asks the Event 023 owner to clear an unauthorized uncommitted combat reservation | `national_policy_publish_chemical`, `national_policy_publish_biological`, `national_policy_publish_nuclear` |
| `national_policy_record_confirmed_nuclear_use` | Launcher ROOT, hit-state FROM in `on_nuke_drop` | Adds exact-pair confirmed-use evidence through the existing bilateral ledger, with no damage, population, stockpile or condemnation debit | `023_sov_nuclear_bombs_on_actions.txt` before Event 023 confirmation clears request context |
| `national_policy_biological_allows_{battlefield,strategic}_use_against_from` | Actor country, exact hostile target FROM | Boolean family-law permission and temporary exact target id | Biological native raids, campaign raids, Event 002/020 targeting and corresponding prepare checks |
| `national_policy_biological_allows_{battlefield,strategic}_use_against_target_id` | Actor country, temporary `cbrn_retaliation_target_id` supplied from an exact target scope | Boolean family-law permission | Biological outcome bridges, sabotage, campaign and normalized deliberate record validators |
| `national_policy_biological_allows_{battlefield,strategic}_use` | Country | Staging/procurement eligibility using the family law and at least one current exact hostile receipt for retaliation | Biological preparation and shared AI procurement posture |
| `national_policy_biological_allows_extreme_use` | Country | Boolean unrestricted biological law check | Existing extreme biological routes |
| `national_policy_nuclear_allows_use_against_from` | Actor country, exact hostile target FROM | Boolean permission with a localized native launch requirement | All six native nuclear `launchable` blocks |
| `national_policy_nuclear_allows_use_against_target_id` | Actor country, temporary exact target id | Boolean nuclear permission, always false for nuclear-none | Native launch helper and Event 023 combat validator |
| `national_policy_nuclear_event_action_policy_is_valid` | Country, existing Event 023 action type/target | Revalidates combat requests against the current nuclear law, preserving all other action-class validators | Event 023 request and native confirmation validators |
| `national_policy_ai_has_{chemical,biological,nuclear}_retaliation_right` | Country | Read-only current-enemy receipt query, no law or capability grant | Native law AI and family staging predicates |

The existing generic `cbrn_policy_*` permission helpers refer to chemical law.
The biological consumers use their explicit family helper names.
Battlefield law retains battlefield first use, retaliation law retains the existing exact-offender ordinary battlefield/strategic exception, and extreme routes require the family's unrestricted law.
Battlefield law does not gain strategic retaliation through this split.
The normalized biological record validator rechecks current family permission before a deliberate result can commit.
Tests and accidents retain their separate record paths.

### Existing bilateral evidence helpers

`cbrn_country_has_active_retaliation_right_against_target_id` checks exact receipt owner, exact existing offender and expiry without choosing a family law.
Permission callers combine that evidence with their own family law.
`cbrn_diplomacy_classify_retaliation_action` takes required argument `POLICY`, the native retaliation law for the acting family.
Chemical exposure passes `POLICY = national_policy_chemical_retaliation` and biological classification passes `POLICY = national_policy_biological_retaliation`.
This retains the established relief/classification exception rather than extending it to unrestricted first use.

```text
cbrn_diplomacy_classify_retaliation_action = {
	POLICY = national_policy_chemical_retaliation
}
```

The classifier still needs `event_target:cbrn_retaliation_target_country`, current war, and the existing action class/severity proof.
Its output is temporary `cbrn_action_retaliation_status`, with the existing last-action history variables as side effects.
No default family argument exists.

## Constants and receipts

The existing shared tuning `cbrn_diplomacy_duration.retaliation_window_days = 365` controls receipt expiry and the temporary flag duration.
`cbrn_diplomacy_source.nuclear = 3` extends the existing chemical 1 and biological 2 source discriminator.
The law publisher's family values share those three values.
Existing `cbrn_use_policy` tuning supplies the established 2/3/5 history tiers.

Each victim receipt stores `cbrn_retaliation_<offender id>_owner` and `_offender` as country scope pointers, plus expiry, first-use date, latest action date, confirmation day and source.
The same exact pair/action day does not refresh expiry when confirmation is repeated.
An independently confirmed later action day can renew the window.
Expiry gates permission lazily, and no periodic country loop is added.
Permanent earliest-use variables and crime/history flags remain intact.

The per-direction `_authority_owner` and `_authority_first_date` fields distinguish current country authority from copied civil-war evidence.
They support the existing earliest-first-user comparison while leaving permanent `_first_action_date` evidence untouched.
An inherited receipt whose recorded owner differs from the holder fails closed, even after the child later obtains a different valid receipt.
Same-day first-use ties revoke live expiry in both directions and retain contested history.

Regular chain event targets `cbrn_retaliation_target_country` and `cbrn_retaliation_confirmed_offender` carry exact scope pointers within the confirmation chain.
No global event target is introduced.
Policy changes never erase confirmed-use history or receipt attribution.
Only Event 023's existing owner cleanup can refund its uncommitted reservation, and a pending native delivery is excluded from that cleanup.
Cancellation uses the published new law value because native `on_add` can briefly see both old and replacement ideas.

## Nuclear boundary

`on_nuke_drop` identifies the launcher through ROOT and the struck state through FROM.
The evidence recipient is the current hostile controller, with no faction, other-enemy or state-owner propagation.
An Event 023 pending request matching the exact state must pass its established country validator, nonce and combat classification.
A test, demonstration, accident or unresolved matching request cannot fall through as an ordinary native combat strike.
The existing asteroid visual flags exclude visual-only callbacks.
Nuclear evidence does not call the C/B convention's member-attacked adapter and never applies physical or diplomatic consequences a second time.

## Migration and presentation

The three five-Command-Power policy decisions are removed from `cbrn_doctrine_decisions.txt`.
Legacy `cbrn_set_use_policy` and `cbrn_change_chaos_warfare_use_policy` adapters fail closed without charging or changing a law.
Native law initialization and CXT setup are owned by `national_policy_effects.txt`.
The native law callback is suppressed during law initialization by its owning publisher.
No focus, UI, map or asset is added by this integration.
Requirement localisation lives in `localisation/english/national_policy_warfare_l_english.yml` and uses existing native law/raid presentation, so no additional sprites are required.

## Validation limits and future work

The bounded source tests under `.tools/test_national_policy_warfare.py` execute the production permission and evidence helpers against mixed-family, exact-enemy, expiry, duplicate, civil-war, same-day tie, controller attribution, callback exclusion and tightening fixtures.
Native primitives and the Event 023 confirmation acceptance result are declared fixtures, so these checks do not establish native launch timing, native cancellation refunds or observed game behavior.
MCP script validation reports no findings on the new effect and trigger files but leaves argument semantics and file root scope unresolved.
The parent owns final weighted-AI review, localisation review, law/UI integration and current system-document reconciliation.
Future changes should reuse the exact-pair receipt contract and keep physical consequences with their existing action owner.
