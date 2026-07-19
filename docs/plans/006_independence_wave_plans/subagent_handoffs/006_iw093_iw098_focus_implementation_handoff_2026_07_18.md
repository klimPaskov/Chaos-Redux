# IW-093 / IW-098 focus implementation handoff — 2026-07-18

## Scope and result

This tranche adds 43 additive `shared_focus` nodes for the Event 006 Asante
(IW-093) and Sokoto (IW-098) packages. The branches are imported into
`independence_wave_focus_tree`; they do not replace a living tree, create a
country, load Event 012's tree, or create characters/advisors/portraits/sprites.

The focus layer now unlocks the existing paid decision stages and consolidates
their durable receipts. It no longer charges decision costs, starts duplicate
timers, or builds a second factory/infrastructure project. The only structural
build in this tranche is the one-time Sokoto survival infrastructure step at
state 902, before the paid caravan-wells project.

## Files and integration points

| File | Change |
| --- | --- |
| `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` | 43 shared focuses, route locks, prerequisites, receipt gates, AI weights, and stable icon ids |
| `common/scripted_effects/006_independence_wave_iw093_iw098_focus_effects.txt` | Focus unlock/consolidation effects and package-specific cleanup helpers |
| `localisation/english/006_independence_wave_iw093_iw098_focus_l_english.yml` | 129 UTF-8-BOM title/description/tooltip keys |
| `common/national_focus/006_independence_wave_focus.txt` | Imports `independence_wave_iw093_seat_kumasi_administration` and `independence_wave_iw098_reconvene_emirate_council` |

The parent also added the 16 decision-visible unlock gates listed in the
parent integration message. Keep those gates in the decision file; the focus
effects intentionally do not call the decision transaction helpers.

## Route coverage

| Package | Survival | Government routes | Economy | Military | Host/diplomacy | Terminal/formable lane |
| --- | --- | --- | --- | --- | --- | --- |
| IW-093 Asante | Kumasi seat, Stool register, Forest Guard decision unlock | Royal Confederacy, Constitutional Cabinet, Veterans Emergency decision unlocks and receipt consolidations | Cocoa ledger; paid depot receipt; paid railway receipt; close milestones | Forest Guard receipt gate, veteran screen, supply patrols | Railway stock unlock, host settlement receipt, debt/customs/property, border policing | Royal sovereign lock, constitutional cabinet, veterans guardianship lock, FORM-24 decision unlock |
| IW-098 Sokoto | Emirate council, native administration, caravan approaches, date-aware sultan gate | Sultanic Federal, Northern Constitution, Frontier Command decision unlocks and receipt consolidations | Caravan wells receipt; route-guard close milestone; paid livestock market receipt; close milestone | Paid cavalry reorganization unlock, receipt-gated frontier infantry, civic-defence staff | Native-account unlock, host settlement receipt, railway-customs protocol, frontier account | Sultanic federal (non-terminal so FORM-25 remains eligible), northern constitution, frontier command terminal lock, FORM-25 decision unlock |

## Exact setup and cleanup contract

Before the imported roots can be used, the owning package setup must still
pass its existing fail-closed proofs and set `*_setup_complete`. Then:

1. Set `independence_wave_focus_assignment_input` to
   `constant:independence_wave_focus_assignment.full_framework` and call
   `independence_wave_assign_focus_framework = yes` for DOX. For SOK, use the
   same reviewed full-framework path only when the minimal-tree exception is
   true (`generic_focus` is present and no Event 012 priority tree is loaded);
   otherwise do not overwrite the meaningful/Event-012 tree.
2. Keep focus `available` active-only (`is_independence_wave_iw093_country` /
   `is_independence_wave_iw098_country`). The two imported roots use
   `*_prepared_scope OR *_active_scope` in `allow_branch` so the tree can be
   loaded during prepared-origin setup.
3. After setup activation and after final validation, call
   `mark_focus_tree_layout_dirty = yes` (the shared assignment effect already
   does this on assignment). Do not grant runtime attestation from focus code.
4. If the parent later exposes the generic signature surfaces, register them
   through the existing helpers/flags
   (`independence_wave_focus_register_ambition_family`,
   `independence_wave_focus_register_signature_module`, and
   `independence_wave_focus_register_formable_family`) only after the owning
   package has the required member/consent proofs. The FORM-24/FORM-25 focus
   nodes themselves only set `*_form2x_congress_decision_unlocked`; the paid
   decision alone writes `*_form2x_preparation_complete`.

The package cleanup dispatcher already calls these new helpers before clearing
values/routes:

```text
independence_wave_iw093_cleanup_focus_content = yes
independence_wave_iw098_cleanup_focus_content = yes
```

They clear every focus-owned unlock, route-consolidation milestone, old timed
marker, host/formable preparation receipt, and focus-only state flag. Decision
completion/failure receipts remain owned by the existing decision cleanup
helpers.

## Icon coverage

Every focus has a stable `GFX_goal_independence_wave_iw093_*` or
`GFX_goal_independence_wave_iw098_*` id. There are 43 focus references and 35
unique ids; repeated ids are deliberate lane reuse (constitutional cabinet,
veterans guardianship, cocoa rail/depot, caravan wells, northern constitution,
frontier command, and livestock market). No `.gfx`, DDS, portrait, advisor, or
sprite file is created or referenced. Register final sprites under these ids
before art production and do not substitute advisor assets.

## Localisation and reward review

- All 43 ids have title, `_desc`, and `_tt` keys (129 keys total); duplicate
  key scan returned none. The localisation file begins with UTF-8 BOM.
- Descriptions describe player-facing institutions and receipts rather than
  implementation history. Tooltips call out paid decisions and receipt gates.
- Rewards are intentionally varied but restrained: package variables, a few
  stability/war-support/army-experience/command-power consolidation effects,
  and one Sokoto survival infrastructure level. No free division ladder and
  no repeated positive equipment stockpile.
- Existing decision effects remain the source of paid equipment/command-power,
  70/90/120-day project timing, and project buildings. Focus closure nodes only
  require the matching completion receipts.

## AI behavior

Survival and host-threat focuses use dominant/urgent package priorities;
throughput/network/security deficits raise economy and military priorities;
route consolidation responds to the matching decision route flag; and FORM
preparation uses the exact `can_prepare_independence_wave_form24_from_iw093` /
`can_prepare_independence_wave_form25_from_iw098` gate. AI never bypasses the
decision cost or consent trigger. The generic decision AI still controls when
paid decisions are actually started.

## High-priority parent fixes and known limits

1. Keep the 16 decision-visible unlock gates in place (see parent message and
   the decision file). Without them, the focus completion only records an
   unlock flag and the paid stage remains hidden.
2. Preserve the exact Event 006 attestation/final-validation gates in package
   setup. These focuses do not admit runtime content or provide fallback
   country surfaces.
3. IW-098's accepted `can_prepare_independence_wave_form25_from_iw098` trigger
   currently permits the Sultanic Federal or Northern Constitution route, not
   the Frontier Command route. The Frontier route therefore intentionally
   ends at its terminal command settlement in this tranche; broaden the
   trigger only with an explicit package-spec decision.
4. The icon handoff is resolved: the reviewed 2026-07-18 package supplies all
   35 distinct focus DDS files and the parent interface file registers each base
   and shine sprite. No advisor asset was introduced.
5. `hoi4.focus_inspect` successfully inspected the existing root tree but its
   current inline inventory did not include the new standalone shared-focus
   source file, so it returned the pre-existing 176-node tree and unrelated
   layout warnings. No focus rewrite was run; validate the combined tree once
   the parent workspace inventory includes the new file.

## Validation evidence

- Brace counts: focus source 444/444; effect source 193/193.
- 43 focus ids, 43 helper calls, and 43 helper definitions match; no duplicate
  focus ids.
- 43 icons cover 43 focus nodes; 129 localisation keys match with no duplicate
  keys.
- No unsupported `<=`/`>=` operators, advisor/portrait/sprite references,
  runtime attestation writes, FORM-24/FORM-25 completion writes, duplicate
  decision timers, duplicate decision equipment costs, or duplicate project
  buildings remain in the focus effect file.
- `hoi4.focus_inspect` artifact (root-tree baseline, with unrelated pre-existing
  diagnostics):
  `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51cfc72177a2ad6ca208dfad826b16cf4e58d6ca9d2270eda22d4584f3db7804/b120ac5e77525d5961bf8d515078e9ebdf8359bcae1cdfb8fc8e7ab2b35187b4/focus-inspect.85fa39df5916f7ca.json`
- Root-tree render baseline (the inline inventory still omitted this standalone
  source; no new-node layout claim is made):
  `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14cd3c87995bf95777eb11cbcdf6155acaed8c7c2d3156a9a7691e23d76b9027/231be46e0382233a007a791ea1a55b14f599293a56ff8fd20a238cf185976456/independence_wave_focus_tree.focus.html`

## Simplifications and unresolved risks

- The branch does not author new FORM-24/FORM-25 consent/member mechanics; it
  correctly stops at decision unlock because the existing congress decisions
  own preparation completion and consent validation.
- No final icon art or `.gfx` registrations are included by design.
- Parent must re-run combined-tree inspect/render after adding the standalone
  source to the MCP inventory; the baseline inspect cannot validate the new
  nodes' layout.
