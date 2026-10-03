# Portrait production reference

`chaosx_portrait_creator` owns every character portrait from brief to installed runtime asset. This reference is the operational sequence and the fail-closed state contract for that work. The canonical family, gate, and review rules stay in the parent skill: [Portrait source-mode gate](../SKILL.md#portrait-source-mode-gate), [Portrait subject ownership gate](../SKILL.md#portrait-subject-ownership-gate), [Fictional portraits](../SKILL.md#fictional-portraits), [Country-leader, commander, operative, and named-officeholder portraits](../SKILL.md#country-leader-commander-operative-and-named-officeholder-portraits), [Advisor and high-command portrait icons](../SKILL.md#advisor-and-high-command-portrait-icons), and [Animated sprites, scripted GUI assets, and animated portraits](../SKILL.md#animated-sprites-scripted-gui-assets-and-animated-portraits).

## Production sequence

1. Inspect the matching installed-vanilla portrait references and lock the runtime basename, canvas, role, and consumers before requesting or producing art.
2. Classify the subject. Grounded people and institutions require attributed Internet source research. Fictional or impossible subjects use native ImageGen.
3. Name the mode in the brief or manifest for a grounded portrait, then follow [Grounded source mode states](#grounded-source-mode-states).
4. For a fictional or impossible portrait, invoke native ImageGen yourself and follow [Generate and refine source art](../SKILL.md#generate-and-refine-source-art) for narrow edits, reference roles, accepted-candidate lineage, and full-resolution/native-size review against the brief and vanilla references.
5. Process the approved portrait, convert it to the required PNG/DDS variants, preserve stable runtime identifiers, update portrait-specific `.gfx` and existing character portrait references, and write the manifest and handoff.

Never generate or substitute the identity of a real or grounded person. If no defensible grounded source exists, mark the portrait blocked. Do not edit unrelated gameplay, localisation, or UI.

## Grounded source mode states

Select the mode in the brief or manifest and record it in the manifest entry.

| Mode | Meaning | Exit condition |
| --- | --- | --- |
| `source_placeholder` | Accepted unchanged attributed source, explicit head-and-shoulders crop, deterministic `156x210` resize, DDS wiring, and preserved identity. | Remains explicitly pending HOI4-style replacement until the user supplies it. |
| `replacement_pending` | An explicit styled-final request is still outstanding. | Allowed only while that request is open. |
| `styled_final` | Independent validation and installation of the user-supplied provider output at the same runtime path. | Requires the locked workflow revision, provider/job evidence, and independent identity/framing/provenance review. |
| `not_needed` | The requirement set carries no portrait row. | No portrait is produced. |
| `blocked` | No defensible grounded source or required evidence exists. | Report the blocker instead of substituting a face. |

No HOI4 repaint is required for `source_placeholder` preparation. A queued job or preview is never `styled_final`, and never open, operate, configure, queue, or monitor RunPod. The user alone runs the provider for grounded HOI4-style finals and supplies the result.

## Parallel portrait receipts and final selection

Parallel portrait workers report only their bounded tranche's files and independent acceptance evidence/status.
Global completion counts belong to the parent; cite them only from a current authoritative parent inventory with its revision and observation time, never copy an earlier parent count.
A missing or parse-failed receipt leaves another owner's status unknown, not unproduced or pending.
Preserve timestamped pre/post snapshots, observed changed paths, and known concurrent changes in disjoint regions without resetting shared work or attributing another owner's changes to yourself.
A later global count must not rewrite historical pre/post facts.

Record whether current runtime DDS bytes match the selected candidate separately from art acceptance; a matching hash alone never proves final approval.
Source versions and canonical PNG packages may retain unselected alternates, so final global review must follow the explicit selected source/version and processed PNG -> candidate DDS -> runtime paths mapping, never the first glob match or an unsuffixed filename.
When moving receipts to canonical paths, update pointers in every referring manifest, handoff, and referenced metadata record while preserving immutable original source/candidate lineage and the receipt's original path/revision.
