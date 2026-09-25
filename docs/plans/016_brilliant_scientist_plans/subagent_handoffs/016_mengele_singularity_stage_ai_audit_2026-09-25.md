# Event 016 Mengele Singularity stage AI audit

Date: 2026-09-25.

Disposition: `unresolved` for effective willingness and historical before/after comparison.

The requested read-only `chaosx_ai_probability_auditor` remained in a running MCP call after a bounded stop request and was closed without a handoff.
The parent then performed the minimal read-only MCP inspect, evaluate, and compare calls and recorded their exact limits here.
No gameplay balance target was selected or changed during this audit.

## Source and scenarios

The new timed decisions are `mengele_event016_singularity_theory`, `mengele_event016_singularity_prototype`, `mengele_event016_singularity_deployment`, and `mengele_event016_singularity_weaponization` in `common/decisions/016_mengele_singularity_stage_decisions.txt`.
Each declares `ai_will_do` base `constant:brilliant_scientist_project_board.ai_high` and a `has_war = yes` modifier with `constant:brilliant_scientist_project_ai.preferred_factor`.
The constants are 10 and 2 respectively in `common/script_constants/016_brilliant_scientist_project_constants.txt`, so source arithmetic suggests raw willingness 10 in peace and 20 in war when the modifier applies.
These are source inputs, not MCP-confirmed effective scores or decision-click probabilities.

The named scenario set `016-mengele-singularity-stage-ai` contains `016-SING-STAGES-PEACE` and `016-SING-STAGES-WAR`, with `state.has_war` false and true respectively.
The candidate pool contains exactly the four new stage decisions.
The compact scenarios do not establish each row's provider, receipt, DLC, facilities, resources, or category-wide competing-decision state.

## MCP evidence

`hoi4.probability_inspect` on the stage decision file with requested adapter `decision_ai_will_do` returned `PROBABILITY_SOURCE_DISCOVERED`, suggested adapter `mission_ai_will_do`, and four matching candidates under that suggested adapter.
Its source revision was `dff699fe35315748c4203db7a2ee99dd42f76b5fa903397053df5fba872c6196`, source hash `3d8be13b0874b94c9cdb28636ac86a22019ee4b06815bddfb847e3de27881b1a`, and inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acf4224568006165d434ddb6444ed8d09f3c23443fe9a51c3aa4883f26d7f30d/12e931c8311afea8faab92c59459b09026b82e63a671bde63a3ee8983a070b76/probability-inspect-3d8be13b0874.json`.

`hoi4.probability_evaluate` using `mission_ai_will_do`, the four candidates, `raw_value`, and those same two scenarios returned `PROBABILITY_ANALYZED_PARTIAL` with eight candidate-scenario records and four unresolved items.
Its analysis ID was `probability-6710b17d3c059f441cb7a43b`, scenario hash `1dd01ebdc096d94812d724bd18f8c9161f6705db5ecbc8f019371e59ed523be2`, and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f6d9a874a5e57a2de2c8602ddee8838e542bb58521c9cca88d2e36c77353c51/1898b07bbd2a0d0567122fa4791a3134fd8600fff0dbe0091ca24e8c5ea915f9/probability-6710b17d3c059f441cb7a43b.json`.
The tool summary did not expose the unresolved rows or numerical outcomes, and the linked artifact was not readable through the available resource server, so no effective score is asserted.

An attempted absent-before `hoi4.probability_compare` could not be constructed through the exposed opaque source schema: string input was rejected as expecting an object, and guessed `inline`, `text`, `content`, and `source` object keys were rejected as unrecognized.
The stage decision file is absent from the committed before state, so a current-versus-current comparison is not a historical patch comparison.
The same-source comparison under `mission_ai_will_do` and the same two scenarios returned `PROBABILITY_ANALYZED_PARTIAL`, `comparisonChanges=0`, eight candidate-scenario records, and four unresolved items; its analysis ID was `probability-386b63750889df054c5aff43` and scenario hash was the same `1dd01ebdc096d94812d724bd18f8c9161f6705db5ecbc8f019371e59ed523be2`.
The comparison JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7cca91965045c9ca0dbc41ff8c9f76ac029943e5c0df870f5766904a09eb2e7/7891d678e8e310a62104cc4c1b0410518097ef7bc9a0161b9b2d186c01fa0c9d/probability-386b63750889df054c5aff43.json`.

The same-source comparison confirms the route accepted the current source but proves no historical AI delta.
Stage willingness, peace-war balance, ranking among competing decisions, and executable availability remain unaccepted pending a supported scenario adapter and a readable outcome artifact.
