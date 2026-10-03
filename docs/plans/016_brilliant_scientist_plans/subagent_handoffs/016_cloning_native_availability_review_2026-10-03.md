# Event016 Cloning native availability source review

Date: 2026-10-03.
Role: chaosx_scripted_system_architect, source-only review.
Disposition: bounded source review completed, parent final review and engine evidence remain unresolved.

## Finding

No concrete source defect was found in the bounded Cloning availability patch.
The private accepted-project gate no longer mistakes the legacy shared completed flag for a private Prototype or exact custom-project completion.
The legacy wrapper denies new legacy access to the registered non-Kruger Event016 package owner even when an incident invalidates its strict live-provider predicate.
The exact running-project query permits an existing legacy job through this added exclusion while preserving the original camp eligibility requirement.

Acceptance basis: the parent explicitly applied the Cloning availability portion separately from the Rocketry commitment architecture and requested these exact source scenarios.
`sp_brilliant_scientist_cloning` remains the accepted private route.
No Rocketry commitment, pending receipt, start/cancel hook, or lifecycle redesign is accepted or implemented by this review.

## Reviewed logic

Let C be `camp_rework_germany_cloning_project_currently_available`.
Let O be the conjunction of `is_mengele_clone_directorate_country`, registry flag present, and Kruger current-host flag absent.
Let R be `is_special_project_being_researched = sp:sp_mengele_cloning` in the owning country.
The legacy wrapper at bridge lines 61-75 evaluates `C AND ((NOT O) OR R)`.
Its explicit AND inside NOT correctly negates the complete package-owner condition.
It does not reject a country merely because one individual owner condition is present.

The private gate at bridge lines 77-86 requires strict provider validity, private Cloning Theory, no private Cloning Prototype, no exact `sp_brilliant_scientist_cloning` completion, and the existing all-project or Cloning availability flag.
It no longer reads `directorate_special_project_cloning_completed`.
This is availability logic and does not itself grant or adopt a provider stage.

## Manual source scenario matrix

| Scenario | Source result |
| --- | --- |
| Ordinary non-provider consumer, C true | O false, so legacy wrapper remains true irrespective of R. Original camp eligibility is preserved. |
| Directorate identity without registry | O false. No extra legacy restriction is introduced by identity alone. |
| Kruger current host with Directorate identity and registry | O false because the no-current-host condition fails. Legacy gate remains C, while the private strict provider gate rejects that host. |
| Registered non-Kruger provider, no running legacy job | O true and R false. Legacy visibility and availability both fail even if C true. The accepted custom route remains governed by its private prerequisites. |
| Registered provider during an incident, no running legacy job | The incident disables strict provider validity but does not negate O. Legacy remains blocked. The custom private gate also remains blocked by its strict provider alias. No incident fallback opens a new legacy start. |
| Registered provider already researching exact legacy project, C true | R true. The wrapper permits both legacy display gates even when O true, including an incident if C still passes. This is preservation of current access, not a start receipt or callback. |
| Running legacy project but C false | Wrapper remains false. The running exception bypasses only the added owner exclusion. It does not override the original camp gate or guarantee access through unrelated program closure or availability removal. This retains the original prerequisite and is not a new regression from this patch. |
| Legacy shared completion present, exact custom project incomplete | With strict provider, private Theory, no private Prototype, and existing availability, the custom gate passes. Legacy/shared completion alone neither authorizes a private stage nor prevents access to the accepted custom route. |
| Exact custom project already complete | Custom gate rejects through its exact completed-project query, independently of legacy shared flags. Stage adoption is owned by other code and is not validated here. |
| Private Cloning Prototype already complete | Custom gate rejects independently of exact native query or shared legacy completion. |
| Missing Theory, strict provider validity, or existing availability | Custom gate rejects. Removing the shared-flag veto does not weaken these independent requirements. |

Ordinary consumer results remain conditional on the unchanged camp gate.
That gate supports its existing German-program branch and Directorate availability branch, at camp trigger lines 2109-2124.
The broader package-owner classifier at Germany trigger lines 89-98 does not test incident state, supporting the intended incident-safe exclusion.

## Scope and tooltips

Both legacy `visible` and `available` blocks retain their existing `FROM = { ... }` entry at project lines 23-33.
Installed project documentation lines 36-46 identifies those blocks as project scope with FROM country.
The wrapper and its nested `is_special_project_being_researched` therefore execute in COUNTRY scope, as required by installed trigger documentation lines 6228-6241.
The query is statically bound to `sp_mengele_cloning`, so running a different project cannot satisfy R.

The new package-owner and running-project branch is entirely inside `hidden_trigger`, at bridge lines 63-74.
Installed trigger documentation lines 5103-5114 confirms that this suppresses its tooltip while preserving evaluation.
The new registry/current-host raw flag checks are not exposed by this branch.
The original camp gate remains outside the hidden block, preserving its existing presentation.
This is not a full localisation/render audit of inherited camp or private-gate tooltips.
No new player-facing identifier or effect text was introduced by the reviewed patch.

## Preservation evidence

The prior architecture handoff records pre-patch hashes for these exact files.
For the legacy project, replacing the two new wrapper tokens in memory with the original camp trigger reconstructs SHA-256 `6E5A2A8BC286E2DB00288070EF52A815FAC6DD5C376FBC0641C440229F57B645`, exactly matching that prior source revision.
For the bridge, removing the added comment/wrapper block in memory and restoring the removed shared-completion veto reconstructs SHA-256 `03B38228120B24D5228AC9986AC3745F7760DCEBC38D61D6DCE8DE29C50325CD`, also matching the prior revision.
No reconstructed content was written to disk.

This establishes that the reviewed project file changes consist only of the two display-gate callers and that the bridge changes consist only of the stated wrapper and veto removal.
Native costs, AI-weight text, project IDs, output consumers, and the rest of those files match the earlier source bytes under that reversal.
The availability patch does alter eligibility, so byte preservation is not a probability or runtime behavior claim.
Model and unrelated CBRN files were not scanned or modified.

## Limits and parent follow-up

Meaningful validation performed: manual source truth-table cases above, exact COUNTRY/FROM and hidden-trigger documentation reads, and reconstruction of both prior file hashes.
MCP calls, game execution, display-state transitions during native cancellation/resume, native engine refresh timing, and live tooltip rendering were not performed under the explicit source-only delegation.
No MCP service failure is asserted.
The evidence gap is the absence of executed engine/MCP scenarios in this task, retained by the parent for final integration.

The running query supplies an observation of current research.
It does not create an actual native start/cancel hook, prove payment, or resolve the separate Rocketry selection/pending-ownership architecture.
Preservation of a running legacy job is conditional on the original camp gate continuing to pass.
No stronger preservation guarantee should be claimed.

Only this handoff was written.
No gameplay, localisation, model, other-document, skill, index, or commit changes.
No fallback or simplification was introduced.
Skills used: chaos-redux-subagents and chaos-redux-events.
Current AGENTS.md and subagent-skill hashes match the versions read earlier in this session.
Parent retains final review, documentation integration, MCP evidence, wiring, and commit.

## Source and reference revisions

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Local SHA-256 hashes identify the source/reference revisions.
The wiki reference is the offline snapshot, with no web wiki lookup.

| File | Relevant lines | SHA-256 |
| --- | --- | --- |
| `common/scripted_triggers/016_mengele_project_bridge_triggers.txt` | 59-86 | `F1489F0C8137A47D05B2C0ECC369B2D638000A7E4D74C3C1D0EC0E87E482CD19` |
| `common/special_projects/projects/mengele_cloning_projects.txt` | 17-78 | `2031613338D6E464F3201781CEDF13184174F5D1213185B839F87506EE7B8D97` |
| `common/scripted_triggers/016_mengele_project_stage_triggers.txt` | 16-49 | `5AB7041CE22F13FBFECF641F4CA9E6FC7D693DDF366DA14E631A3DFA498E537C` |
| `common/scripted_triggers/camp_repression_rework_triggers.txt` | 2109-2124 | `5E21B40D7F864379FA132EDC8C54955B8EADCAF68CBDA58404CAD0D9D9D2A57F` |
| `common/scripted_triggers/germany_mengele_triggers.txt` | 89-98 | `88988F10E39973B942107F810CE300CBB55577EEC032671EAFA683F08D5A7E40` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` | 5103-5114, 6228-6241 | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/special_projects/projects/documentation.md` | 36-46 | `16879504BC72AA357F1D3C0F1093E94A3946F8C35E7942F65AC9A5D3BCD6C643` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | 885-886 | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
