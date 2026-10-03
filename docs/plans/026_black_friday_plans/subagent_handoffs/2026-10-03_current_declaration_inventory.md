# Event 026 current declaration inventory handoff — 2026-10-03

Disposition: implemented documentation refresh; Event 26 implementation and manual semantic coverage remain unresolved.

## Scope, acceptance, and source-of-truth map

The parent authorized writes only to the two cost inventories and this new handoff.
The acceptance basis is the parent prompt dated 2026-10-03: the original user goal requires a full universal cost registry against the final commit.
Current implementation is source evidence only, and does not approve a reduced registry, exclusions, balance targets, or enabling Event 26.
No gameplay, registry, catalog, other documentation, or specialist-owned adapter was edited.
Event 26 remains incomplete and default-disabled as directed by the parent.

| Surface | Disposition and authority | Evidence and limitation |
| --- | --- | --- |
| Original Event 26 universal-registry goal | accepted and queued for final integration; acceptance is the current parent prompt's explicit record of the original user goal | Final commit is not frozen; the parent owns full registry reconciliation and completion review. |
| [Custom inventory](../event26_cost_surface_custom_inventory.md) | implemented declaration-discovery refresh | All 100 mod / 38 Vanilla active custom owners, exact lines, excluded comments, bounded source pointers; manual semantic coverage incomplete. |
| [Native inventory](../event26_cost_surface_native_inventory.md) | implemented declaration-discovery refresh | Every one of 201 mod / 145 Vanilla scanned paths, occurrence partitions, source hashes; no discount or effective-owner claim. |
| Shared cost registry | unresolved final coverage; parent-owned and unchanged by this curator | The 346 hash-bound decision files are discovery inputs, not complete logical transaction/component records. |
| Existing bounded owner handoffs | unresolved current acceptance/semantic coverage; historical evidence preserved through links | Current decision call sites are retained, but old dates, component totals, source pointers, probability and native results do not become final-freeze proof. |
| RSA specialist tranche | unresolved; pending parent review | Mechanical source counts/hash only; no audit, promotion, or discount certification of the pending adapter. |
| Japan native-raid replacement | superseded decision ownership according to the parent prompt | Both old Japan decision paths are absent; raid declarations, prices and adapters lie outside this decision-only scan and require the parent's owning review. |
| Required decision MCP evidence | blocked for this pass | Exposed `mcp__hoi4_agent_tools__hoi4_decision_inspect` was called with `{ mode: "inventory", refresh: true }`; no final tool result arrived before the orchestration wait was terminated. |

## Counts and snapshot identity

Scan window: 2026-10-03T05:18:11.9235070Z through 2026-10-03T05:18:37.7233668Z.
Repository HEAD observed at scan end: `4991fd7de71e40ca78b5ccfe31749dd42e9029d8`.
An earlier pre-scan HEAD read was `f48758822b294aeed4c179868e27fddf6abab93d`; the parent/concurrent work advanced HEAD while discovery was being prepared.
The source snapshot therefore deliberately uses file hashes, rather than representing either HEAD as a frozen implementation commit.
The first independent recheck at 2026-10-03T05:20:47.8535524Z matched the original scan.
Later checks detected concurrent changes in nine source paths; those paths were rescanned through 2026-10-03T05:31:23.6952522Z, under HEAD `5cb073ae0f4471f4a3330f8cdebb6d0b62a5c876`, with aggregate declaration counts unchanged.
The final independent recheck at 2026-10-03T05:31:29.5310770Z matched all 346 recorded file hashes and paths.
This is a contemporaneous worktree snapshot and remains refreshable at the parent's final commit freeze.

Targeted drift refreshes:

- `common\decisions\028_asteroid_incoming_decisions.txt`
- `common\decisions\039_murder_mystery_decisions.txt`
- `common\decisions\016_mengele_alien_arms_stage_decisions.txt`
- `common\decisions\016_mengele_cloning_stage_decisions.txt`
- `common\decisions\016_mengele_paleogenetics_stage_decisions.txt`
- `common\decisions\016_mengele_robotics_stage_decisions.txt`
- `common\decisions\016_mengele_teleportation_stage_decisions.txt`
- `common\decisions\016_mengele_temporal_stage_decisions.txt`
- `common\decisions\016_mengele_xenobiological_synthesis_stage_decisions.txt`
Combined canonical source-manifest SHA-256: `aa74ae0af3bb85519ebe74ac603343271bd34cfe75fb4ee40cf482f4b929089a`.

| Source | Files scanned | Active custom owners | Raw trigger / text | Active trigger / text | Native owners | Raw native cost | Active native cost | Literal zero | Numeric nonzero | Symbolic/unresolved |
| --- | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Mod | 201 | 100 | 2342 / 2343 | 2342 / 2343 | 55 | 1316 | 1316 | 343 | 140 | 833 |
| Vanilla | 145 | 38 | 371 / 371 | 368 / 368 | 86 | 2955 | 2903 | 387 | 2150 | 366 |

The parent's mod count is verified exactly.
The old 2,224 / 2,225 / 81 custom baseline is superseded by a net increase of 118 declarations per key and 19 custom owners.
Vanilla's three excluded trigger/text pairs are commented source in `common\decisions\CZE.txt`: triggers 1129, 1147, 1744; text 1132, 1153, 1747.
The custom mismatch remains the text-only terminal-readiness display at `common\decisions\020_black_plague_rat_decisions.txt:923`; source points to a requirement, not a proven payment.
The old native 1,328 / 1,033 / 295 metadata was a stale snapshot; current mod discovery is 1,316 active declarations with 973 not written as literal zero and 343 literal-zero declarations.
Among those 973, 833 are symbolic, so their actual zero/nonzero values are not resolved by this mechanical inventory.
Vanilla has 52 commented native-cost matches excluded from active totals; every excluded path/line is listed in the native inventory.
Vanilla `AST.txt:810` has numeric `cost = -7`, retained in nonzero discovery without a positive-purchase or discount claim.

## Added and removed owner paths

Changes below compare exact owner paths to the prior two inventory documents, not to every historical repository file or to the parent registry.
Newly discovered means added to this inventory's owner set, not necessarily a newly created source file.

### Added mod custom owners (23)

- `common\decisions\006_independence_wave_don_decisions.txt`
- `common\decisions\012_africa_gods_decisions.txt`
- `common\decisions\016_brilliant_scientist_directorate_project_board.txt`
- `common\decisions\016_brilliant_scientist_kruger_state_clone_machine_decisions.txt`
- `common\decisions\016_mengele_alien_arms_stage_decisions.txt`
- `common\decisions\016_mengele_biological_stage_decisions.txt`
- `common\decisions\016_mengele_biomedical_prototype_decision.txt`
- `common\decisions\016_mengele_cloning_stage_decisions.txt`
- `common\decisions\016_mengele_computation_incident_decisions.txt`
- `common\decisions\016_mengele_computation_stage_decisions.txt`
- `common\decisions\016_mengele_conventional_incident_decisions.txt`
- `common\decisions\016_mengele_conventional_stage_decisions.txt`
- `common\decisions\016_mengele_materials_stage_decisions.txt`
- `common\decisions\016_mengele_paleogenetics_stage_decisions.txt`
- `common\decisions\016_mengele_remaining_conventional_prototype_decisions.txt`
- `common\decisions\016_mengele_robotics_stage_decisions.txt`
- `common\decisions\016_mengele_singularity_construction_decisions.txt`
- `common\decisions\016_mengele_singularity_incident_decisions.txt`
- `common\decisions\016_mengele_singularity_stage_decisions.txt`
- `common\decisions\016_mengele_teleportation_stage_decisions.txt`
- `common\decisions\016_mengele_temporal_stage_decisions.txt`
- `common\decisions\016_mengele_xenobiological_synthesis_stage_decisions.txt`
- `common\decisions\camp_administration_country_decisions.txt`

### Removed mod custom owners (4)

- `common\decisions\016_brilliant_scientist_biological_operations.txt`: absent from the scan; no semantic status transferred to another owner.
- `common\decisions\070_africa_gods_decisions.txt`: absent from the scan; no semantic status transferred to another owner.
- `common\decisions\japan_biological_campaign_decisions.txt`: absent from the scan; no semantic status transferred to another owner.
- `common\decisions\japan_chemical_campaign_decisions.txt`: absent from the scan; no semantic status transferred to another owner.

### Added mod native-cost owners (3)

- `common\decisions\012_africa_gods_decisions.txt`
- `common\decisions\camp_administration_country_decisions.txt`
- `common\decisions\chaosx_test_country_debug_decisions.txt`

### Paths removed from the prior native owner list (10)

| Prior owner path | Current finding |
| --- | --- |
| `common\decisions\016_brilliant_scientist_biological_operations.txt` | Path absent from the current scan; no native coverage claim carried forward. |
| `common\decisions\070_africa_gods_decisions.txt` | Path absent from the current scan; no native coverage claim carried forward. |
| `common\decisions\biological_raid_staging_decisions.txt` | Path absent from the current scan; no native coverage claim carried forward. |
| `common\decisions\biological_sabotage_decisions.txt` | Path absent from the current scan; no native coverage claim carried forward. |
| `common\decisions\biological_stockpile_safety_decisions.txt` | Path absent from the current scan; no native coverage claim carried forward. |
| `common\decisions\cbrn_battlefield_operation_decisions.txt` | Path absent from the current scan; no native coverage claim carried forward. |
| `common\decisions\cbrn_diplomacy_decisions.txt` | Path remains present with zero active native cost declarations; retained explicitly in the current all-file ledger. |
| `common\decisions\cbrn_doctrine_decisions.txt` | Path remains present with zero active native cost declarations; retained explicitly in the current all-file ledger. |
| `common\decisions\chemical_warfare_decisions.txt` | Path absent from the current scan; no native coverage claim carried forward. |
| `common\decisions\japan_chemical_campaign_decisions.txt` | Path absent from the current scan; no native coverage claim carried forward. |

The old native table contained zero-declaration CBRN diplomacy/doctrine rows while labeling its owner total as files with native cost; current metadata separates all scanned files from owners with actual occurrences.
The current native table retains all zero-declaration paths, including these two owners and all category files.
The parent identifies removed legacy `070_africa_gods_decisions.txt` and the Japan native-raid replacement; the current `012_africa_gods_decisions.txt` is discovered separately, without inherited adapter approval.
Replacement mapping for the removed Scientist biological decision file and other removed bio/chemical owners remains a parent semantic reconciliation item.

## Contradictions resolved and still open

| Evidence or contradiction | Cleanup / remaining disposition |
| --- | --- |
| Both inventories claimed September baselines but mixed in later CBRN rows. | Resolved in the two allowed files: one current snapshot, full owner/line regeneration, no mixed-date aggregate. |
| Custom inventory retained removed `070`, Japan and Scientist biological owners. | Resolved in current owner tables; removed paths survive only as explicit historical removal evidence. |
| Vanilla's 371 raw custom matches per key were labeled declarations. | Resolved: 368 active plus three commented occurrences per key. |
| Vanilla rows were `engine_inaccessible_without_owner_adapter` solely because no generic hook existed. | Resolved: unresolved owner-adapter status; mod owner overrides remain a possible adaptation path. |
| Old 104/111-component totals included historical Japan decision components and omit newer candidate work. | Superseded as current discovery metadata; component totals must be rebuilt by the parent registry owner, not inferred from declarations. |
| Random Faction row retained `source_adapter_bounded_pending_live_with_static_two_payer_exception`. | Resolved in custom inventory: linked `random_faction_liaison_adapter.md` supersedes the historical static exception; current payment call at line 90 is recorded, with parent review limits. |
| CBRN protection formerly claimed one shelter adapter and seven unadapted rows. | Updated to shelter source pointers plus three current material-payment candidates; their acceptance and full semantics remain unresolved pending parent review. |
| CBRN occupation formerly claimed no adapter. | Current PP-fee candidate calls are recorded; `2026-10-03_cbrn_protective_aid_pp_adapter.md` remains unresolved, including mask-shipment/factory coverage. |
| CBRN doctrine fixed-policy exception appears in historical handoff language. | Still open: that handoff's asserted acceptance is not independently established by this inventory or the full-registry user goal; parent must preserve explicit exception acceptance or resolve the conflict. |
| Universal goal exceeds current declaration discovery and bounded source adapters. | Still open: no universal, final-registry, engine-coverage, or gameplay-completion claim. |

## Plan and handoff dispositions; stale instructions and duplication

| Document / tranche | Disposition, reason, and replacement or review boundary |
| --- | --- |
| The two refreshed inventories | implemented for this discovery scope; previous snapshot metadata is superseded in place by the dated tables and this handoff. |
| `subagent_handoffs\owner_adapter_tranche_current.md` | unresolved as current-state evidence; its September 2 counts, removed Japan decision paths and 104-component total remain stale; replacement for discovery is this handoff plus the two inventories; file left unchanged outside write scope. |
| `subagent_handoffs\2026-09-27_current_cbrn_custom_cost_crosswalk.md` | unresolved as complete current-state evidence; read through its final diplomacy follow-up, but early unadapted claims and old protection/occupation lines do not describe all current candidates; left unchanged outside write scope. |
| `subagent_handoffs\random_faction_adapter.md` historical static liaison claim | superseded by named `subagent_handoffs\random_faction_liaison_adapter.md`; existing supersession notice and scenario-specific evidence preserved, neither handoff edited. |
| `subagent_handoffs\africa_elephant_adapter.md` | unresolved final acceptance; parent-integration source findings support bounded pointers, while live/contract interruption limits remain. |
| `subagent_handoffs\germany_mengele_adapter.md` | unresolved final acceptance; four direct command-power payment pointers retained; historical missing-route/probability findings are not refreshed into service-health claims. |
| `subagent_handoffs\genocide_crisis_adapter.md` predecessor patch | rejected as recorded in its own handoff; no accepted replacement or delayed-lifecycle adapter is established by this discovery pass. |
| `2026-10-03_cbrn_protective_aid_pp_adapter.md` | unresolved candidate with exact current decision call sites; no promotion from implementation presence or its claimed design acceptance. |
| RSA `012_africa_rsa_*` pending work | unresolved and pending parent review by explicit parent instruction; no specialist handoff supplied or audited in this pass. |

No prompt files were supplied for cleanup, and none were inspected or changed.
Stale resume instructions that would reuse the old September counts, removed owner paths, static liaison exception, or whole-tranche component totals must use this dated discovery handoff instead.
No document was deleted or merged into a new design; historical handoffs remain intact, with their limited evidentiary role stated above.
No accidental mid-sentence hard wraps were identified in the two prior inventory files; rewritten prose keeps each sentence on one physical line and preserves headings, paragraphs, lists, code fences, and complete Markdown table rows.
No separate resume packet was created because it lies outside the three-file write scope.

## Scan reproduction and hash protocol

The two scan roots are the mod root and installed Vanilla root listed in the inventories.
The following is the one-off PowerShell scan executed for this refresh; it is included as reproducibility evidence, not installed as a tool or wrapper.
The compact JSON serializes native and excluded occurrence pairs as alternating line/value and key/line arrays; table generation partitions these pairs without dropping occurrences.

```powershell
$ErrorActionPreference = 'Stop'
$taskRoots = @((Get-Location).Path, 'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV')
$taskRows = @()
$taskStart = (Get-Date).ToUniversalTime().ToString('o')
foreach ($taskRoot in $taskRoots) {
  $taskFiles = @(rg --files --hidden --no-ignore -g '*.txt' (Join-Path $taskRoot 'common\decisions') | Sort-Object)
  foreach ($taskFile in $taskFiles) {
    $taskBytes = [IO.File]::ReadAllBytes($taskFile)
    $taskHash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskBytes)).ToLowerInvariant()
    $taskText = [Text.Encoding]::UTF8.GetString($taskBytes)
    $taskClean = [regex]::Replace($taskText, '"(?:\\.|[^"\\])*"|#[^\r\n]*', { param($m) [regex]::Replace($m.Value, '[^\r\n]', ' ') })
    [int[]]$taskNewlines = @([regex]::Matches($taskText, '\n') | ForEach-Object { $_.Index })
    $taskItems = @()
    foreach ($m in [regex]::Matches($taskClean, '(?<![A-Za-z0-9_])(custom_cost_trigger|custom_cost_text|cost)\s*=')) {
      $taskIndex = [Array]::BinarySearch($taskNewlines, [int]$m.Index)
      $taskLine = 1 + $(if($taskIndex -lt 0){-$taskIndex-1}else{$taskIndex})
      $taskValue = ''
      if ($m.Groups[1].Value -eq 'cost') {
        $taskValue = [regex]::Match($taskClean.Substring($m.Index+$m.Length), '^\s*([^\s{}#]+|\{)').Groups[1].Value
      }
      $taskItems += [pscustomobject]@{key=$m.Groups[1].Value;line=$taskLine;value=$taskValue}
    }
    $taskRaw = @()
    foreach ($m in [regex]::Matches($taskText, '(?<![A-Za-z0-9_])(custom_cost_trigger|custom_cost_text|cost)\s*=')) {
      $taskIndex = [Array]::BinarySearch($taskNewlines, [int]$m.Index)
      $taskLine = 1 + $(if($taskIndex -lt 0){-$taskIndex-1}else{$taskIndex})
      $taskRaw += [pscustomobject]@{key=$m.Groups[1].Value;line=$taskLine}
    }
    $taskRows += [pscustomobject]@{source=($(if($taskRoot -eq $taskRoots[0]){'Mod'}else{'Vanilla'}));path=$taskFile.Substring($taskRoot.Length+1);sha256=$taskHash;items=$taskItems;raw=$taskRaw}
  }
}
$taskCompact = @($taskRows | ForEach-Object {
  $taskRow = $_
  $taskExcluded = @($taskRow.raw | Where-Object { $r=$_; -not ($taskRow.items | Where-Object { $_.key -eq $r.key -and $_.line -eq $r.line }) } | ForEach-Object { @($_.key,$_.line) })
  [pscustomobject]@{source=$taskRow.source;path=$taskRow.path;sha256=$taskRow.sha256;triggers=@($taskRow.items | Where-Object key -eq 'custom_cost_trigger' | ForEach-Object line);texts=@($taskRow.items | Where-Object key -eq 'custom_cost_text' | ForEach-Object line);costs=@($taskRow.items | Where-Object key -eq 'cost' | ForEach-Object { @($_.line,$_.value) });excluded=$taskExcluded}
})
[pscustomobject]@{startUtc=$taskStart;endUtc=(Get-Date).ToUniversalTime().ToString('o');head=(git rev-parse HEAD);rows=$taskCompact} | ConvertTo-Json -Depth 6 -Compress
```

Each file hash is SHA-256 of the exact original bytes, including BOM and line endings, before lexical masking.
The aggregate manifest serializes the native inventory rows in their listed order: Mod rows first, then Vanilla rows, each in the scan's `Sort-Object` path order.
Each record is `source<TAB>relative Windows path<TAB>lowercase SHA-256<LF>`; the final record also ends in LF, encoded as UTF-8 without BOM.
The resulting combined hash is `aa74ae0af3bb85519ebe74ac603343271bd34cfe75fb4ee40cf482f4b929089a`.
The native inventory stores every individual file hash, so the parent can identify which source changed rather than relying only on the aggregate.
RSA discovery source at this snapshot: `common\decisions\012_africa_rsa_decisions.txt`, SHA-256 `40283784e0d0ea091bd96c96c46f0155ec01e911091b2b20a0389ac5e1d696cc`.
Its category file hash is recorded separately in the native ledger; neither hash certifies the pending adapter.

## MCP and reference evidence limits

The connected tool list exposes `hoi4.decision_inspect`, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.
The decision inventory request produced no final result before its wait was terminated; no artifact URI, workspace revision, coverage, diagnostic status, or verified service-health result can be retained from that request.
This is the exact route limitation for this pass, not a claim that the tool is absent or that every server route is unhealthy.
Standalone viewer availability was not verified or required for this decision-only declaration scan.
The reference routes were not exercised in this documentation-only discovery pass; pertinent local sections were read directly, and no MCP reference-retrieval claim is made.
Local references: `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:285–338`, SHA-256 `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; installed `common\decisions\_documentation.md:1–46`, SHA-256 `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
Those sections support the separation between display declarations and actual payment, and the native decision timing context; they do not prove runtime behavior.
Existing scenario-specific probability handoffs remain linked through `random_faction_adapter.md` and `random_faction_liaison_adapter.md`; this pass does not run weighted analysis, replace the probability auditor, or convert historical scenarios into final-freeze proof.

## Validation, skipped coverage, and parent follow-up

Meaningful checks: independently verified the parent's 2,342 / 2,343 raw mod custom count with `rg`; reconciled Vanilla raw vs commented matches; regenerated every exact owner/line list; partitioned every native occurrence; compared prior owner sets; checked current bounded call-site pointers; and independently re-enumerated and hashed all 346 files with no unrecorded source drift at the final stated recheck.
Concurrent drift found at intermediate checks was corrected by targeted rescans of nine named source paths before final verification.
The table totals, exact occurrence lists, and source hashes are checked against the captured scan data, rather than against the stale registry.
Source arithmetic/lexical discovery is not MCP scenario or live-game evidence.
Skipped meaningful coverage: complete logical-transaction/component mapping, helper expansion, actual constant/variable resolution, active-load override resolution, native price/display/payment scenarios, receipt/refund/settlement and delayed commitment execution, AI/probability scenario audits, and save-state/game validation.
These checks exceed the authorized declaration-refresh scope; the attempted decision MCP route also returned no result.
No final universal-registry status or gameplay completion is claimed, and no simplification of the original full-registry goal is accepted.
The parent must review the pending RSA patch, rebuild semantic component records for current owners and native raids, resolve any fixed-policy exception acceptance, obtain required owner/MCP evidence, and rerun this discovery against the final frozen commit.
The parent also owns updating stale handoffs and registry metadata outside this write scope.
Skills used: `chaos-redux-subagents` for ownership and disposition boundaries, and `chaos-redux-decisions-missions` for the declaration/payment evidence boundary; no skills were created or modified.
No commit was created by this curator; final integration and commit remain with the parent while implementation and required review are incomplete.
