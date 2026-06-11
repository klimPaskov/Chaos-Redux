# Holy Realm Super-Event Specification

This event has three planned super-events. The super-event research agent must find real quotes and usable audio. The spec does not claim final quote or music selection.

## Super-event 1: The Awakened One

Role: transformation.

Trigger:

- Bodhi Progress 108.
- Dhyana Depth 4.
- Defilements below 20.
- Required teaching missions complete.
- Focus `The Unshaken Seat` complete.
- Buddhahood has not already occurred.

Purpose:

This is the moment the Bodhisattva becomes the Buddha. It changes the leader, portrait, mandala, country identity, and available powers.

Title direction:

- The Awakened One.
- The Wheel Stands Still.
- Beneath the Unshaken Seat.

Description direction:

Describe reports from capitals, soldiers, envoys, and pilgrims. The world should not fully understand what happened. The description should explain that the Bodhisattva is no longer treated as a normal ruler.

Button direction:

Short, reverent, and restrained. Possible direction, not final researched text:

- The wheel turns.
- Sit still.
- Let the bell sound.

Quote direction:

Use a real Buddhist text or a historically verifiable religious or philosophical quote about awakening, cessation, freedom from craving, or the end of suffering. The quote must be checked against a reliable source. Avoid invented spiritual lines.

Image direction:

Generated symbolic super-event image. A luminous seated figure or emptying mandala above a Himalayan horizon. Avoid direct claims that this is the historical Gautama Buddha unless the event intentionally uses that identity. No generated text.

Audio direction:

Music should feel sacred, spacious, and slow. Research public domain or clearly licensed chant, hymn, bell-based music, or instrumental spiritual music. Composition and recording rights must be documented separately.

Follow-up:

- Apply `The Awakened Seat`.
- Unlock Buddha Powers category.
- Change portrait and mandala state.
- Record event log entry.

## Super-event 2: Powers of the Awakened

Role: first display of powers.

Trigger:

- Buddha exists.
- First Buddha power is used against a valid chaos country.
- `Revealed Powers of the Buddha` not yet shown.

Purpose:

This is the moment the rest of the world understands the new leader can do more than teach. It justifies the major anti-chaos buff.

Title direction:

- Powers of the Awakened.
- The River Became Earth.
- The Wall Was Only Air.

Description direction:

Use the specific first power if possible. If the first power is Walking on Water, describe a river line that should have held. If it is Passing Through Walls, describe fortifications failing to matter. If it is One Becomes Many, describe simultaneous appearances. Keep the tone calm and alarming.

Button direction:

- The armies stopped speaking.
- No wall remained.
- A silence crossed the river.

Quote direction:

Research real sources related to concentration, spiritual power, or the lesser nature of miracles compared with liberation. A quote that reminds the player these powers are not the highest goal would fit best.

Image direction:

Generated symbolic or documentary-style supernatural war image. A chaos army at a river, mountain wall, or fort, stopped by a serene light. No gore focus. No modern props.

Audio direction:

More forceful than the first super-event, but still not bombastic. Bells, low strings, chant, or percussion can work if licensed.

Follow-up:

- Apply timed `Revealed Powers of the Buddha`.
- Add anti-chaos war support or morale effects.
- Notify chaos countries and compact members.
- Record event log entry.

## Super-event 3: The Final Silence

Role: terminal world-end or non-terminal ultimate Nirvana route.

Trigger:

- Final Silence ritual completes.
- Buddha exists.
- Dhyana Depth 4.
- Meditation Charge and low Defilements checks passed.
- If chaos value over 1000 and no world-end exists, terminal branch.
- Otherwise non-terminal spiritual victory branch.

Purpose:

This is the end of the Buddha's worldly action. The world either enters a terminal silence under Chaos Redux world-end rules or survives into an aftermath where the Empty Seat remains.

Title direction:

- The Final Silence.
- The Last Bell.
- When the Wheel Stopped.

Description direction:

The description should be spare. Avoid overexplaining metaphysics. Describe practical observations: fronts go quiet, chaos signals fail, witnesses stop reporting commands, bells carry through radio static, the mandala is empty.

Button direction:

- Nothing answered.
- The bell is gone.
- The seat is empty.

Quote direction:

Research real passages related to Nirvana, cessation, or final peace. Do not invent a quote. If using scripture, verify translation and attribution.

Image direction:

Generated symbolic super-event image. Empty seat, lotus, extinguished lamps, still mountain horizon, world map in quiet shadow. No explosion. No spectacle for its own sake.

Audio direction:

Sparse, final, and musical. A slow chant, bell composition, or public domain sacred music can work. The audio should not be pure ambience unless explicitly approved and documented.

Terminal effects:

- Set `world_end`.
- Set `world_end_final_silence`.
- Set matching super-event visibility.
- Set `global.current_super_event_audio_id`.
- Use settings-aware playback helper.
- Stop incompatible future random events and end branches.
- Update event log, docs, and spreadsheet.

Non-terminal effects:

- Transform leader to Empty Seat.
- Disable Buddha power activations.
- Add aftermath reconstruction decisions.
- Apply major anti-chaos suppression and recovery.
- Keep world-end flag unset.

## Super-event research requirements

For each super-event, the research package must include:

- Final title, description, button text, and quote.
- Quote source and attribution confidence.
- Button text source if it is a cultural or scriptural reference.
- Audio title, creator, performer if relevant, source, license, duration, usage terms, and conversion notes.
- Image direction and source mode.
- Final audio id and super-event slot after implementation assigns them.
- Documentation row for music track list.

No placeholder audio should remain in a completed super-event.
