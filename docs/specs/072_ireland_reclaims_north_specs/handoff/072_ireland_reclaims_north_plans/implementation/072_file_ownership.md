# Proposed runtime ownership

Paths below are integration targets to validate against the current checkout.
They are not created runtime files in this planning package.
Preserve established equivalents where the repository already owns a shared surface.

| Surface | Proposed owned or inspected path | Ownership boundary |
| --- | --- | --- |
| Entry events | events/072_ireland_reclaims_north.txt | Preserve namespace and entry ID, replace legacy behavior |
| Gameplay helpers | common/scripted_effects/072_ireland_reclaims_north_effects.txt | Parent or bounded scripted-system worker |
| Eligibility helpers | common/scripted_triggers/072_ireland_reclaims_north_triggers.txt | One policy source for gameplay, AI and GUI |
| Tuning | common/script_constants/072_ireland_reclaims_north_constants.txt | Costs, thresholds, grants and timing |
| Decisions and missions | common/decisions/072_ireland_reclaims_north_decisions.txt | Event-owned actions and mission callbacks |
| Category metadata | common/decisions/categories/072_ireland_reclaims_north_categories.txt | Explicit generated GUI attachments |
| Focus content | common/national_focus/072_ireland_reclaims_north_focus.txt and approved partner supplements | Irish success gate and additive partner behavior |
| Focus and decision AI | Existing supported AI plan paths plus 072-owned helpers | Narrow lifecycle and route overrides |
| National ideas | common/ideas/072_ireland_reclaims_north_ideas.txt | Three owned families only |
| Local state work | Existing state modifier patterns | Only genuine location effects |
| Country identities | Existing countries and approved cosmetic-tag surfaces | Reuse before creating new identities |
| Units and equipment | Existing supported OOB/template/equipment paths | Verified spawn and reinforcement ledger |
| Asset registrations | interface/072_ireland_reclaims_north_assets.gfx | Actual produced sprite consumers |
| GUI consumer declarations | docs/formables/state_puzzles/approved_072_consumer/ | Draft until map, assets and tool evidence complete |
| Generated puzzle output | Existing universal runtime generator surfaces | Generated ownership, no manual shared-node edits |
| English localisation | localisation/english/072_ireland_reclaims_north_l_english.yml | Valid encoding and actual dynamic effects |
| Achievements | Existing mod achievement system | Ten new tracked contracts and icon triplets |
| News and super-events | Existing shared systems | Parent integration and once-only presentation guards |
| Event log and settings | Existing shared schemas | Parent only, no duplicate new global systems |
| Catalog workbook | Authoritative repository workbook, path to inspect | Spreadsheet worker after final writing, export CSV afterward |

The file layout can be divided further where actual engine or repository conventions require it.
Do not spread one ownership rule across unrelated global files merely to make a narrow worker's task easier.
No worker is authorized to modify another event's gameplay, shared settings, or the full catalog as an incidental cleanup.
