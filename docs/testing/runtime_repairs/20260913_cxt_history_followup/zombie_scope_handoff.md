# Zombie profile and biological state-scope repair handoff

Disposition: implemented source patch with partial MCP evidence and blocked event comparison.
Acceptance basis: parent `/root` explicitly accepted a deterministic existing-choice representative profile within the user-authorized CXT fixture scope on 2026-09-13.
Ordinary research choices and weights were required to remain unchanged.

## Applied patches and owned files

- `ZS-01`: `common/scripted_effects/zombie_special_project_effects.txt` adds `initialize_cxt_weaponized_zombie_profile`, calls it from `complete_weaponized_zombie_project_from_project_output` and `complete_weaponized_zombie_project`, and suppresses the success-report event schedule for CXT.
- `ZS-02`: `common/script_constants/zombie_special_project_constants.txt` adds the isolated `weaponized_zombie_cxt_fixture` table.
- `ZS-03`: `common/scripted_triggers/020_black_plague_weaponization_triggers.txt` replaces State-scope `exists = yes` in `black_plague_weaponization_target_state_is_valid` with `scope_exists = yes`.
- `ZS-04`: `common/scripted_triggers/biological_stockpile_safety_triggers.txt` makes the same correction in `bio_stockpile_safety_state_is_valid_designation_candidate` and the nested arsenal-pointer State block.
- `ZS-DOC`: `common/scripted_effects/zombie_special_project_effects.md` documents the helper contract, fixture source, lifecycle, call sites, and assets.

Exact pre-edit copies of the owned existing script/event files are under `baseline/<relative path>` in this repair folder.
`zombie_baseline_hashes.json` records their SHA-256 hashes.
The event baseline was retained for review although `events/zombie_weaponized_special_projects.txt` was not changed.
`common/special_projects/projects/zombie_weaponized_projects.txt` was inspected but not changed.
No CXT setup/history files, localisation, spreadsheet, GUI, assets, focus trees, portraits, or AI weights were edited by this worker.
No files were staged or committed, as required by the parent ownership contract.

## Cause and profile flow

Scripted native project completion bypasses ordinary prototype rewards, so the country had no acquired trait deltas.
The final resolver initializes missing country variables to zero and resolves a default archetype, producing the observed empty profile and unrelated default prose.
The project source already uses the correct vanilla contract: `iteration_output.country_effects` is country scope and `FROM` is the project.
Acquisition resets country tracking, each prototype choice adds its temporary deltas through `weaponized_zombie_apply_profile_delta`, and project step flags are written through `FROM` while country step flags remain on the actor.
Successful ordinary research resolves the same persistent country profile and does not need a project-to-country copy.
Source review confirmed five combat/cure attribute option families contribute 1/2/3; obedience contributes 0/1/2, with zero being an intentional hostile option rather than missing research data.
The ordinary delta helper and random console-completion helper were compared against their exact baselines and remain unchanged.

CXT initialization stores a recorded real-choice sum: strength 3, infectiousness 3, speed 2, durability 2, cure resistance 2, obedience 2, test subjects 3, and accident risk 1.55.
Its nature is neurobiological, life state dead, and resource level expanded.
The fixture skips field testing and uses ordinary refinement, with no forbidden branch.
Those flags fail the existing demonic/mutant override prerequisites and the Wendigo completion-failure prerequisites, so initializing this fixture does not launch a random outbreak or failure report.
The six country trait-step flags and variables make repeated initialization idempotent.
A fully tracked existing CXT profile is retained; incomplete tracking is reset before the fixture is installed.

## CXT owner integration contract and popup coverage

Execute `initialize_cxt_weaponized_zombie_profile = yes` in CXT country scope before native scripted completion of `weaponize_the_zombies`.
The generic project-output and completion helpers also invoke it idempotently, so reaching either path directly still initializes the fixture.
Do not replace it with `randomize_and_complete_weaponized_zombie_project`, which selects random traits and owns separate console-completion semantics.
The CXT owner retains native project registration/completion, CXT history, and broader popup suppression.
This worker communicated the contract to `/root/cxt_history_runtime` and `/root`.

The ordinary successful completion helper retains `apply_weaponized_zombie_completed_bonuses`, unlock tooltip, and the completion achievement.
That existing bonus helper retains zombie delivery technology with `popup = no`, completed/availability flags, initial stockpile, cost tier, raid success profile, cure advantage, and conditional achievements.
Only scheduling `chaosx.weaponized_zombies.1` is suppressed for CXT.
Ordinary countries receive the same report as before.
Direct manual invocation of the report event and genuine runtime accidents/field tests are outside this setup-popup guard.
The failure branch was preserved; a retained fully tracked dangerous CXT profile could therefore still fail under the original rules.

## State validity and cleanup

The installed vanilla trigger documentation identifies `exists` as COUNTRY-only and `scope_exists` as supported in any scope.
The corrected checks validate the selected actual State scope instead of asking the engine to run a country-only trigger there.
All controller existence, war, ownership/control, impassability, exact pointer/source, ordinary pathogen eligibility, rat-control exclusions, exposure/provenance, facility level, and operational-building conditions remain unchanged.
The third nested State occurrence was corrected in the same owned safety trigger file to prevent the same failure in pointer validation.
No alternate state selection or eligibility bypass was introduced.

The fixture reuses `reset_weaponized_zombie_project_tracking` for stale country research, resolution, nature/life/resource, accident, forbidden, completion-failure, and stockpile markers.
No event targets or global pointers were added, and no new target cleanup is required.
No shared scripted helper registry or router was created.

## Meaningful validation and evidence limits

`zombie_choice_profile_check.json` records all 14 selected ordinary prototype option tokens and independently sums their profile, subject, and risk deltas.
The result matches every fixture-table value, including obedience 2 and accident risk 1.55.
A baseline comparison verified the two State trigger files differ only in the three intended State validity checks and retain every other eligibility condition.
A baseline block comparison verified `weaponized_zombie_apply_profile_delta` and `randomize_and_complete_weaponized_zombie_project` are unchanged.
No ordinary balance weights or probability pools were patched, so no probability audit-patch-compare transaction was required.
The fixture route itself invokes no weighted-selection helper under its recorded flags.

`zombie_mcp_evidence.json` records baseline and after event inspect/render responses, artifact links, revisions, and boundaries.
The server returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, with `helpers = 0` and the explicit limitation: “Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked”.
Absolute Windows source paths select the bounded zombie event surface; initial relative/event selectors selected no nodes and are not treated as useful rendered coverage.
The after scope render selected 15 nodes and retained source-linked JSON/SVG/PNG artifacts.
The event source itself is unchanged, and the MCP graph revision remains `3ac0bcfca142cdb797cca8faf293cfa1085b9019421045d9f385374ad094fc2a`, so these artifacts do not establish helper-write comparison proof.
The valid `hoi4.event_compare` request used the baseline `artifactUri`, `render = false`, and `refresh = true`; it returned no result after several minutes and the running orchestration cell 14 was terminated to prevent unbounded workspace analysis.
Mandatory comparison evidence remains blocked, and source verification is not presented as equivalent MCP engine evidence.
No live game was launched or controlled.

Required offline core wiki pages were consulted, including Data structures, Scopes, Triggers, Effects, Event modding, On actions, Decision modding, Idea modding, AI modding, Modifiers, and Localisation.
The offline snapshot contains no Special project Modding page; this exact reference gap is recorded rather than replaced with online Paradox wiki access.
Vanilla project and prototype-reward documentation, Script Constants documentation/schema, relevant effect/trigger entries, and land-project country/iteration-output precedents were consulted.
Existing dynamic helper source/docs were read before adding the owner-local fixture helper.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or updated for this bounded runtime repair.

## Simplifications, omissions, and blockers

No gameplay simplification was made; the representative CXT strain is the explicitly accepted sandbox fixture rather than an ordinary-country balance substitute.
MCP helper/lifecycle coverage is partial and the required event comparison is blocked as stated above.
CXT native completion/history integration belongs to the country owner and requires parent review of that owner’s changes.
The broader CXT popup-spam fix belongs to the parent and CXT owner; this patch covers only the zombie successful setup report.