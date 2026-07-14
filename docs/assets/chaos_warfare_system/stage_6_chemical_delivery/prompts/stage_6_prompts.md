# Stage 6 chemical-delivery equipment prompts

The original 18 source masters were generated independently with the built-in official imagegen workflow. Each prompt requested one sober WWII-era industrial visual on a flat `#00ff00` chroma-key field for local alpha extraction. Prompts prohibited readable text, logos, people, victims, injury, explosions, gas clouds, modern materials, and cartoon treatment. The equipment visual target was a compact hand-painted HOI4 equipment card with worn olive-drab metal, dark iron, brass fittings, aged wood, strong silhouette, and readability at `131x52`; the separate idea icon targets the compact `64x64` HOI4 idea-icon contract. The five bounded additions below bring the package total to 23 assets, including one `32x32` raid map/type icon.

## Prompt keys and distinct subjects

- `archetype_chemical_agent_payload`: three sealed cylindrical pressure containers in a wooden transport cradle with valves and clamps.
- `chlorine_agent_lot_1`: four tall ribbed chlorine cylinders in a welded rack with brass valve caps and canvas restraints.
- `phosgene_agent_lot_1`: three squat sealed steel drums with locking rings, pressure gauge, and capped hose.
- `mustard_agent_lot_1`: dark amber-brown sealed drums and an amber glass-lined canister in an open wooden crate.
- `lewisite_agent_lot_1`: three compact metal jerrycans with broad sealed necks, wire handles, and copper sampling cup.
- `tabun_agent_lot_1`: padded steel transit case containing six sealed glass ampoules in felt compartments.
- `sarin_agent_lot_1`: two slender stainless chemical bottles joined by a rigid manifold in a timber rack.
- `soman_agent_lot_1`: three dark glass ampoules in ribbed protective sleeves inside a riveted shock case.
- `malodor_agent_lot_1`: two sealed canisters with perforated diffuser caps, valve block, and small shipping box.
- `behavioral_agent_lot_1`: dark laboratory transit case with rows of amber ampoules, hinged lid, and sample tray.
- `archetype_chemical_artillery_ammunition`: open shell crate holding large artillery shells with filling ports and brass driving bands.
- `chemical_shell_lot_1`: one oversized artillery shell on a timber rack with fuse, filling valve, two smaller shells, and handling cradle.
- `archetype_chemical_air_payload`: two finned aerial payload canisters in a steel maintenance cradle with feed manifold and brackets.
- `choking_chemical_air_payload_lot_1`: long cylindrical aerial canister with tail fins and capped underside dispersal nozzles.
- `blister_chemical_air_payload_lot_1`: two broad teardrop aerial bombs with sealed nose caps and short fin tails on a wooden rack.
- `nerve_chemical_air_payload_lot_1`: two slim high-capacity aerial spray tanks with conical noses, stabilizing fins, and closed manifolds.
- `incapacitating_chemical_air_payload_lot_1`: four small sealed aerial canisters in a perforated carrier frame with suspension bar.
- `idea_cbrn_first_chemical_shock`: defender-side first-exposure emblem with a field respirator, brass alarm bell, and orderly procedure cards; no attacker imagery or readable text.

The equipment source masters remain in `../source_png/equipment/` and the idea source master remains in `../source_png/ideas/`, all with the `_source.png` suffix. The prompts are generation provenance, not in-game text; no generated label is relied upon by the package.

## Stage 6 bounded additions

These five additions were generated in five separate built-in official imagegen calls and saved first as green-field source masters in the current generation cache. Each prompt required a flat `#00ff00` chroma-key field, no readable text, no people or victims, no injury, no explosions, no gas cloud, no watermark, and no reuse of another asset's composition. The four archetypes use the `131x52` equipment-card target; the raid icon uses the inspected vanilla `32x32` map/type target.

- `archetype_choking_chemical_air_payload`: cache source `exec-6bf7fc3f-5848-4664-9d84-4a48f2e461b5.png`; one long olive-drab finned aerial canister in a steel cradle with a conspicuous underside row of capped dispersal nozzles and feed manifold, emphasizing choking-vapor handling.
- `archetype_blister_chemical_air_payload`: cache source `exec-0d3f8a4b-d5f0-480b-876b-63055c61845a.png`; two broad sealed teardrop aerial bombs with heavy nose caps, short fins, timber rack, and a restrained amber-brown sealed canister, emphasizing persistent contamination handling.
- `archetype_nerve_chemical_air_payload`: cache source `exec-555abb81-8854-4d67-a7cf-9c06de1e8472.png`; two slim blue-black high-capacity spray tanks with conical noses, fins, closed manifolds, sealed ports, and a riveted frame, emphasizing nerve-agent sealed handling.
- `archetype_incapacitating_chemical_air_payload`: cache source `exec-079e7346-22c9-4a5a-98c9-1673f6cc8297.png`; four small sealed finned canisters held in a perforated suspended carrier with latches and shock padding, emphasizing modular incapacitating-agent preparation.
- `cbrn_chemical_air_operation`: cache source `exec-6ce2d928-5b48-43f2-8412-145d93b4d196.png`; a purpose-built square emblem of a dark WWII-era attack aircraft releasing three amber droplets over a target ring, designed for raid map/type readability and not derived from an equipment card.

All five current source masters are preserved under `../source_png/equipment/` or `../source_png/raids/` with the `_source.png` suffix. The prompt record is generation provenance, not in-game text; no generated label is relied upon by the package.
