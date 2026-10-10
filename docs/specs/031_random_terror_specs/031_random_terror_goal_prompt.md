# Goal: finish Event 31 Random Terror

Finish Event 31 against the accepted design in `docs/specs/031_random_terror_specs/`.
Event 31 already runs and is enabled by default, so this is continuation work, not a rebuild.

Follow `CLAUDE.md` and the named Chaos Redux skills.
Read the package README for the acceptance basis, status table and open questions, then work through the ordered list in [the continuation prompt](031_random_terror_coding_prompt.md).
Each item points to the part that owns its requirement and to the completion-audit finding it closes.

Preserve the README's stable accepted terms, the representation rule, and the scope boundaries (no dedicated Event 31 GUI, no custom unit, no 3D model).
Leave the README open questions to the user or parent.

Use project subagents through the [routing table](031_random_terror_subagent_routing_prompts.md), probability evidence through the AI scenario matrix, and the MCP retry limits in `CLAUDE.md`.
Agents do not launch the game.

Update the event documentation, the part status sections and the agent decisions file as items close.
End with a completion report that lists every remaining finding and every simplification.
