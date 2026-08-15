# Event 018 resource-discovery option tooltip repair

## Scope and result

This patch is limited to the opening discovery events `chaosx.nr18.1` and `chaosx.nr18.2`.

The repeated affected-state and resource lines came from the discovery packages running in visible `immediate` blocks. Those packages initialize or update the field, add its resources, refresh state modifiers, and write internal ledgers before the player chooses an option. HOI4 therefore expanded the same shared state-scoped effects beneath every option. The option-specific posture effects were already inside `hidden_effect` blocks and were not the source of the repetition.

Both shared `immediate` blocks are now enclosed by `hidden_effect`. The resource rolls, targeting, field initialization, evolution package selection, flags, AI weights, and follow-up events are unchanged. Each option still has exactly one `custom_effect_tooltip`, rewritten to state its governance choice and material tradeoff directly.

## Changed files and identifiers

- `events/018_random_resource.txt`
  - `chaosx.nr18.1` shared opening package presentation
  - `chaosx.nr18.2` shared enrichment package presentation
- `localisation/english/018_random_resource_l_english.yml`
  - `chaosx.nr18.1.a.tt`
  - `chaosx.nr18.1.b.tt`
  - `chaosx.nr18.1.c.tt`
  - `chaosx.nr18.1.e.tt`
  - `chaosx.nr18.2.a.tt`
  - `chaosx.nr18.2.b.tt`

## Display before and after

Before, every option inherited the visible expansion of the same immediate resource package. The affected state and underlying state effects appeared repeatedly, followed by a vague custom tooltip.

After, the shared package is hidden from option presentation. The player sees one concise custom tooltip per choice. National authority emphasizes domestic control and resistance to foreign leverage. The domestic charter exchanges faster development for foreign interest. The concession route permits negotiations over rights and access. The reserve route trades development for lower excavation risk. Enrichment can be integrated with rising depth and pressure, or suspended where conditions allow at the cost of output and possible contract review.

## Localisation audit summary

- Missing keys: none in the six assigned option tooltips.
- Duplicate keys: none in the assigned keys.
- Scripted localisation issues: none found in the assigned keys.
- Dynamic text: `chaosx.nr18.1.a.tt` now uses `[ROOT.GetAdjective]` to identify whose hands retain the field. Existing event-target name and resource-name tokens were preserved.
- Cross-surface mismatch: none introduced. The rewritten tradeoffs match the field-project completion effects and the opening posture flags.
- Encoding: `localisation/english/018_random_resource_l_english.yml` remains UTF-8 with BOM.
- Sourced quotations: no quotation-bearing surface was changed or inspected in this bounded pass.

## Prose repair summary

- Vagueness: replaced phrases such as `organize investment` and `favors restraint` with concrete control, output, pressure, risk, and contract consequences.
- Bloat: each option has one short tooltip with no repeated affected-state dump.
- Obvious explanation: removed text that only restated the option label.
- Repetition: the common resource package is no longer expanded beneath every choice.
- Overcomplication: no nested qualifications or administrative filler remain in the six tooltips.
- Style repair: no em dash, semicolon, staged contrast, implementation note, or hidden-route disclosure was added.

## Validation and MCP evidence

The mandatory read-only Event Chain Viewer inspected `chaosx.nr18.1` before the patch and rendered its option neighborhood. The baseline revision was `6fd03271dc18a3eed51a243381014469936297690c66b696b6e532c8c2a788cb`.

- Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f85ac8863732221b74583b778339a2d9a0eb0c9d78a2009e7fd27f3daa7e388/9019e8936c9aa1a591e808378c14006c7f1c30a115431acb1a7e5f9240029a83/event-trace-6fd03271dc18.json`
- Options artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bdcf9e08c5c84bd320d3d38f0900df6800c28c8e7ce44afe5e83da3d50cbc5e/8a44f7b17ce6e6bd73110ef87b61bdde6019c3d2af481ce1cb25c39cec5985ed/event-options-6fd03271dc18.json`

After the patch, focused event lint reported zero blocking diagnostics for `events/018_random_resource.txt` at revision `5bd3d3e1d2ccb9cd401178dc6b502a6e6de2f30873d54cd605d63876d592ca9f`.

- Post-patch lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54ad3194c66469943a1b37d955566c48e0192bdb962a96add19294c3a164c6ab/e84bf9e5c01f5353741c601212899a000359762b73b514cd8278730e8a1cec80/event-lint-5bd3d3e1d2cc.json`
- Post-patch options artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3036225343018be48a73bb4368435828d2ad522d603b35df681cb42977f6a6e/73bdb0ed84c1455234de619e13241154cde36578f43b77e3ab04751de344b8d9/event-options-5bd3d3e1d2cc.json`

The viewer returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` because its workspace-wide helper projections remain incomplete. This limits whole-chain conclusions but does not block the bounded option presentation repair.

## Remaining risks and skipped validation

No live event-popup rendering is available to this agent, so the final visual confirmation that the repeated affected-state list is absent remains user-owned. No gameplay, AI, target, probability, or resource amount changed, so no probability comparison was required. There are no unresolved wording decisions in the assigned six tooltips.
