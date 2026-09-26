# Cloning and Paleogenetics Blocked-Cost Binding

Disposition: implemented in the shared working tree; integration commit is blocked by concurrent Event 016 stage-decision edits.

The eight new blocked-cost and cost-hover keys in each of `localisation/english/016_mengele_cloning_stage_l_english.yml` and `localisation/english/016_mengele_paleogenetics_stage_l_english.yml` now use the same `[This.GetMengeleStageValue...]` getters as their normal cost rows. These 16 keys formerly contained 30 raw `[?constant:brilliant_scientist_project_...]` expressions. The getters and their numeric value keys already exist in `common/scripted_localisation/016_mengele_stage_value_localisation.txt` and the two stage-localisation files; no new getter was required. Source checks found no unresolved getter reference or remaining raw constant in either stage-localisation file, and both retain their UTF-8 BOM.

The 16 keys themselves and the corresponding Event 016 stage-decision changes are still uncommitted work from a separate owner. This CBRN binding patch cannot be committed alone without also committing those additions. The parent left them in place and did not stage or commit the other owner's changes. Native blocked-row and hover rendering, stage payment execution, and an owner-reviewed integration commit remain open.
