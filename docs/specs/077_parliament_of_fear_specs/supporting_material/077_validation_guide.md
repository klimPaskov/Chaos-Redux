# Validation guide

The package defines 93 implementation acceptance scenarios and 18 probability scenario families. Every CSV row is explicitly unrun in the actual game and MCP runtime.

The included `077_reference_model.py` and `077_reference_model_tests.py` test a small standalone abstraction of seat conservation, evidence identity, action commitment, cleanup, and source attribution. They do not parse Clausewitz, execute event scripts, inspect native character behavior, render GUI, model the full incident process, or establish game balance.

Run the reference tests with:

```bash
python 077_reference_model_tests.py
```

The source package's static checks verify document structure, required prompt names, goal length, source-manifest hashes, links, and the presence of all achievement IDs and test rows. These are packaging checks.

After implementation, use the full project event, probability, GUI, localisation, asset, achievement, and completion workflows. Live testing requires the appropriate runtime and user-authorized access. The debug-playtest skill was read, but autonomous desktop playtesting was not invoked by this planning request.

Expected evidence includes exact tool inputs and outputs, before and after scope or GUI comparisons, native-size asset reviews, save and reload checks, multiplayer behavior, and a completed independent improvement-loop handoff. A screenshot alone does not prove that an irreversible action is safe.
