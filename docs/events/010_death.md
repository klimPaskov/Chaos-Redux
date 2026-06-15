# Event 010 - Death

Event 010 is `Death`, a minor fire-once event rooted at `chaosx.nr10.1`. It has no cluster and uses `DTH` as the conflict-free country tag. Death is a nonhuman special chaos country ruled by Zol with the `God of Death` leader trait, uses an all-black map color and flag set, starts from a remote low-population island, and receives no starting divisions, starting manpower, starting equipment, or public opening notification.

## Flow

The hidden root event creates or reactivates Death, consumes one eligible island state, records Death in the event log, and schedules delayed missing-island reports for the former owner/controller and nearby coastal or naval observers. Those reports are indirect, arrive months after the origin, and open Missing Island decisions for recipient countries without revealing Death or Zol.

All consumption paths call `death_consume_current_state` in `common/scripted_effects/010_death_effects.txt`. The shared effect records the previous population, removes population and state value, transfers owner/controller to Death, adds a Death core, applies active wasteland state effects, records civilian deaths when the deaths system is enabled, updates consumed-state counters, withers lingering divisions, and checks reveal, defeat, world-end, and whole-world-consumed gates.

Death reveals itself only when it consumes a mainland coastal state above the configured population threshold. The reveal fires super-event `62`, makes Death a world threat source, declares war on neighboring countries, and enables containment decisions. After reveal, Death can wither neighboring states only when no non-Death divisions are present, and can attempt cooldown-limited coastal jumps when pushed back.

World-end starts only when Death has consumed a whole continent and Chaos is above the Death world-end threshold. This fires super-event `63`, swaps Zol to the world-end portrait, creates one coastal foothold on each continent that does not already contain Death, and unlocks the strongest host behavior. Real world-end footholds spawn local Last Shore hosts immediately; the triggerable scenario keeps its separate intensity-scaling host pass. If every populated state is consumed, super-event `65` fires.

Defeat is custom. Death is defeated only when it controls no states, not by ordinary capitulation shortcuts. Defeat clears the world-threat source, removes Death units/templates, and leaves wastelands as recaptured dead zones. Super-event `64` fires only after public reveal and a major crisis threshold: at least 10 million consumed population, at least three mainland states consumed, or a world-end attempt.

## Gameplay Surfaces

- Event script: `events/010_death.txt`
- Constants: `common/script_constants/010_death_constants.txt`
- Effects: `common/scripted_effects/010_death_effects.txt`
- Triggers: `common/scripted_triggers/010_death_triggers.txt`
- State modifiers: `common/dynamic_modifiers/010_death_state_modifiers.txt`
- Decisions: `common/decisions/categories/010_death_categories.txt`, `common/decisions/010_death_decisions.txt`
- Country package: `common/country_tags/chaosx_countries.txt`, `common/countries/Death.txt`, `common/characters/DTH.txt`, `history/countries/DTH - Death.txt`, `history/units/DTH_1936.txt`
- Focus tree: `common/national_focus/010_death_focus_tree.txt`
- Localisation: `localisation/english/010_death_l_english.yml` plus shared GUI, ideas, achievements, music, event-name, and scenario localisation files
- Triggerable scenario: SCN-006 in the shared triggerable scenario files
- Event log: Death actor mapping, event details, and five milestone evolutions in the shared event-log scripted effects/localisation
- Country identity: all DTH ideology and base flags use the black Death flag set; party localisation resolves to `The Last Office`

## Decisions And AI

Missing Island decisions are limited to countries that receive delayed reports. They can send a survey boat, check records, issue quiet quarantine instructions, or dismiss the matter. Surveying can expose Death before the world learns its name and opens the quiet-defeat achievement path.

The Death Country category appears after public reveal, for countries with relevant borders/compact membership, and for report recipients with coastal-watch candidates. It contains public war recognition, Living Compact coordination, coastal patrols, wasteland gear, Last Shores response, quarantine line actions, coastal-watch state preparation, wasteland surveys, dead-zone outposts, Dark Methods, Black Oath, Herald, and Black Apostolate route decisions. Strengthening a quarantine line also starts a timed hold-line mission; if the line survives the mission period, global front readiness improves and spread pressure falls, while an early break raises spread pressure.

Dark Methods are a living-country desperation route. A threatened country can open Black Book offices, bind unburied names into weak capped hosts, interrogate empty roads for Death pressure intelligence, seal names in iron, and burn the Black Book before exposure becomes a domestic scandal. The route uses exposure, bound names, and mourning debt variables, keeps AI use conservative, and records the hidden Book Burner achievement only when the country used a Dark Method, burned the book before the high-exposure threshold, and later helped defeat Death.

The Black Oath is a separate betrayal route. A desperate country can whisper to Zol, take the oath, leave the Living Compact, receive the Herald of Zol cosmetic identity and national idea, and unlock Herald decisions. Heralds can offer a prison census, open dead ports, feed border states to Death through the shared consumption helper, or break the oath and become a direct Death target. Name debt, black favor, living disgust, sacrificed states, and dead ports control the route. If a Herald reaches the hidden thresholds after world-end, it can proclaim the Black Apostolate cosmetic identity and achievement hook.

After Death is defeated, active war and compact decisions close. Recaptured wasteland decisions remain available so living countries can survey dead zones and build outposts. Dead-zone outposts count toward `death_the_names_do_not_come_back` only after the custom defeat path has fired.

AI weights are intentionally conservative before reveal, stronger for threatened countries after reveal, and strongest for compact/Last Shores responses. Dark Methods have low AI weights and are biased toward direct-threat or world-end desperation; Black Oath AI is heavily restricted to unstable, non-major, threatened countries in world-end conditions, and the Black Apostolate proclamation is player-only. Death itself has staged ghost behavior: no starting units, weak passive hosts at the lower host tier, stronger but still inferior hosts at the higher tier, and aggressive parity hosts only for world-end. Host effects provision only the small dummy manpower and infantry equipment required for each scripted host at creation time; Death has no starting pool and does not recruit normally.

The Death focus tree is a fixed-purpose 26-node lane tree, not a normal country tree. It has an opening trunk, Shroud/Hunger/Census pre-reveal lanes, a real `Public Death` convergence focus gated by public reveal, Coastal/Wasteland/Host post-reveal lanes, and a terminal Last Shores/World Consumed branch. The forbidden routes live on living-country decisions instead of adding another DTH focus branch.

## Assets

Registered sprites:

- `GFX_portrait_DTH_zol`, `GFX_portrait_DTH_zol_world_end`, and `GFX_portrait_DTH_zol_world_end_animated` in `interface/chaosx_characters.gfx`, files under `gfx/leaders/010_death/`
- `GFX_report_event_death_mail_boat`, `GFX_report_event_death_lighthouse`, `GFX_report_event_death_census`, `GFX_news_event_death_mainland_reveal`, `GFX_news_event_death_defeated` in `interface/chaosx_pictures.gfx`
- `GFX_super_event_death_reveal`, `GFX_super_event_death_world_end`, `GFX_super_event_death_defeat`, `GFX_super_event_death_world_consumed` in `interface/chaosx_super_events.gfx`
- `GFX_super_event_death_black_oath` in `interface/chaosx_super_events.gfx`, file `gfx/super_events/super_event_death_black_oath.dds`
- Black Atlas sprites and frame-sheet definitions in `interface/010_death.gfx`, used by `interface/010_death_black_atlas.gui`
- Decision, focus, and idea sprites in `interface/010_death.gfx` and `interface/chaosx_ideas.gfx`
- Achievement sprites in `interface/chaosx_achievements.gfx`

Final asset details are recorded in `docs/assets/010_death/generated_art_manifest.md`. Static assets are wired for Death, Herald of Zol, Black Apostolate, the researched Black Oath super-event, and the world-end Zol portrait fallback. The Black Atlas scripted GUI is wired to stable sprite names and uses frame-sheet animation surfaces. The optional world-end Zol animation package is complete as an eight-frame source-frame sheet and registered animated sprite; world-end gameplay uses the static fallback for the country leader portrait.

## Future Plans

- Add deeper post-defeat memorial/reconstruction decisions for recaptured wastelands without restoring erased population.
- Replace any generated static fallback asset only by keeping the existing sprite names and final paths stable.
