"""Write the Event 014 imagegen regeneration prompts.

This helper only keeps the 65 exact prompts and their compact design metadata in
sync. It does not create artwork or alter runtime assets.
"""

from __future__ import annotations

import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
PROMPTS = PACKAGE / "prompts"
SPECS = PROMPTS / "prompt_specs.json"


DETAILS = {
    "CBA": "an irregular lower-jaw reliquary with five mismatched square teeth, chipped bone contours, two dark riveted cheek plates, a red cord notch, and a hooked metal suspension loop",
    "CBA_communism": "five individually shaped jaw segments interlocked around two unequal cleaver blades; give every blade a different chipped spine, rivet hole, and binding tab around a quartered bone socket",
    "CBA_democratic": "eight mismatched dentine plates pinned around a scalloped assembly shield, with three deep ballot-like tally cuts, a split crown seam, and visible iron fasteners",
    "CBA_fascism": "an asymmetric iron boar mask with opposed tusks, four square jaw vents, a broken ear spur, layered cheek guards, and uneven brow rivets",
    "CBA_neutrality": "a long scavenged carving blade with a pierced bone grip, hooked pommel, three deep ledger nicks, red binding wraps, and an irregular jaw-shaped guard",
    "CBB": "a crown of three nonidentical cleaver blades seated in a curved lower-jaw band, with chipped tips, tooth notches, unequal rivets, and a split central socket",
    "CBB_communism": "a squat ration press whose outer millstone is assembled from six broad jaw teeth, with a perforated mallet, side crank socket, wedge blocks, and scarred iron braces",
    "CBB_democratic": "a scalloped council shield carrying a forked standard with unequal tines, two bowl-shaped side lugs, a jaw-notch at the base, and three visible tooth rivets",
    "CBB_fascism": "one curled tusk locked inside a squared iron jaw clamp, including hinge bolts, four tooth slots, a torn binding strap, and a hooked lower spur",
    "CBB_neutrality": "a fused hook-and-cleaver device with a hooked upper arm, chipped lower plate, triangular bone socket, three offset rivets, and two bite-shaped voids",
    "CBC": "a blunt boar head with one torn ear, mismatched tusks, layered cheek armor, a split snout plate, three jaw cutouts, and bright pin-like eyes",
    "CBC_communism": "a plated fist gripping a short carving fork, with individually jointed fingers, chipped tines, a cuff built from jaw segments, and an off-center wrist rivet",
    "CBC_democratic": "a civic shield assembled from three tooth slabs over an iron frame, with a central dark void, two side notches, stitched edge tabs, and a small red hinge",
    "CBC_fascism": "a horned boar skull with one broken horn, long nasal plate, blade-like cheek spurs, four tooth apertures, and an exposed forehead rivet",
    "CBC_neutrality": "two mismatched capped tusks strapped around a stepped chopping block, with a jaw-shaped top notch, iron binding bands, and a small hanging blade wedge",
    "CBD": "a hammered feast bowl crowned by four irregular tooth finials, with unequal loop handles, a cracked base plate, riveted seams, and a deep black drop-shaped void",
    "CBD_communism": "two different butcher mallets locked through a jaw arc, with chipped striking faces, binding plates at the crossing, a square bone clasp, and jagged handle cuts",
    "CBD_democratic": "a covered platter built as a heraldic reliquary, with a jaw-shaped handle, serrated tray rim, unequal side latches, and three dark vent cuts",
    "CBD_fascism": "a lopsided hyena head with torn ears, saw-tooth mane, squared lower jaw, bolted cheek plate, deep eye cutouts, and one broken fang",
    "CBD_neutrality": "a curved bone ledger beam with stitched end caps, pierced by a narrow carving blade through a jaw-shaped buckle, plus three blank hanging tally tags",
    "CBE": "an off-center tooth wheel assembled from eight mismatched jaw plates, each with chipped edges, individual riveted braces, a broken outer gap, and an irregular iron void",
    "CBE_communism": "four unequal cleavers interlocked as a harsh windmill-like ration machine, with different blade holes, binding wedges, and a square jawbone hub with exposed pins",
    "CBE_democratic": "a bone-spine balance with two uneven feast-bowl pans, toothed rims, mismatched hooks, a jaw-shaped fulcrum, and small riveted counterweights",
    "CBE_fascism": "three distinct bone fangs anchored into a single iron gum plate, with side bolts, red negative-space cuts, chipped points, and a small central jaw hinge",
    "CBE_neutrality": "an oversized feast knife with a toothed cleaver spine, pierced bone grip, five offset rivets, hooked pommel, and a jaw-plate guard",
    "CBF": "a bear-claw reliquary made from a riveted iron palm, three unequal bone talons, stitched cuff plates, a tooth-shaped cutout, and one red fastening cord",
    "CBF_communism": "two visibly different meat forks locked through a jaw-shaped butcher block, with bent tines, chipped handles, asymmetric bindings, and a central square clasp",
    "CBF_democratic": "a scavenged civic shield with an irregular bite-shaped crown, three inset teeth, stitched side straps, a split lower notch, and four mismatched fasteners",
    "CBF_fascism": "an asymmetric horned beast skull with one shortened horn, bolted cheek plates, four uneven teeth, a cleaver-like forehead scar, and a dark nasal socket",
    "CBF_neutrality": "an iron cauldron device with a jaw rim, three uneven square teeth, two differently hooked handles, riveted belly plates, and one cracked central foot",
    "CBG": "a monumental serrated cleaver with two bite-shaped blade holes, a pierced bone grip wrapped in red cord, hooked heel, chipped spine, and riveted cheek plate",
    "CBG_communism": "a broken ring assembled from jaw segments around a square perforated meat hammer, with side lugs, a split bone handle, iron braces, and an open gap",
    "CBG_democratic": "three different carving tools—a short cleaver, boning knife, and hook blade—locked into a central jaw socket, with asymmetric grips and separate rivet patterns",
    "CBG_fascism": "a long raven skull with a broken crest, pinned eye socket, bolted jaw hinge, feather-like blade notches, and a dark split running down the beak",
    "CBG_neutrality": "two mismatched boar tusks with iron caps and binding straps enclosing a stepped chopping block cut with four tooth slots and a red center peg",
    "CBH": "a heavy cleaver whose blade carries three unequal tooth apertures, a split spine, ring pommel, hooked heel, bone grip, and a row of offset iron rivets",
    "CBH_communism": "a broad cleaver and a hooked cleaver bound through a jawbone block, with a central riveted clasp, chipped opposing edges, and uneven handle wraps",
    "CBH_democratic": "a crowned cauldron with an irregular tooth rim, two nonmatching handles, three short feet, a white tooth window, seam plates, and visible side pins",
    "CBH_fascism": "a squared lower jaw with five uneven teeth beneath a three-spike crown joined by a riveted brow, fractured cheek pieces, and a narrow red gum cut",
    "CBH_neutrality": "an asymmetric three-pronged feast fork piercing a shield assembled from jaw plates, with hooked outer tines, stitched seams, tooth rivets, and a split point",
    "CBL": "a monumental sovereign jaw with seven uneven teeth, black riveted cheek plates, a red serrated gum crown, hooked outer tips, and several deliberate bone fractures",
    "CBL_communism": "six visibly unique cleaver blades arranged as a turbine-like ration assembly around a jaw-socket hub, with different holes, chipped tips, and binding wedges",
    "CBL_democratic": "an irregular council table viewed as heraldry, with eight jaw-notched edge stations, four bone leg tabs, a scarred central shield plate, and asymmetric fasteners",
    "CBL_fascism": "a horned crown whose two mismatched horns interlock with a four-tooth jaw rim, with a riveted forehead plate, red eye voids, and jagged side lugs",
    "CBL_neutrality": "a bone-spine balance whose pans are a cleaver cradle and forked jaw bowl, with unequal suspension hooks, a tooth finial, riveted fulcrum, and chipped base",
    "CBL_CENTRAL_COMMAND": "a three-tier command tower inside a battered shield, with jaw-shaped gate, riveted corner braces, signal spikes, split battlements, and one red command slit",
    "CBL_CENTRAL_COMMAND_communism": "three distinct command batons—cleaver tip, jaw stamp, and hooked end—interlocked within a broken tooth gear, with bolts, wedges, and an open outer gap",
    "CBL_CENTRAL_COMMAND_democratic": "a four-point command compass with a cleaver east point, tooth-spear north, jaw-tab south, hook west, and a layered riveted center boss",
    "CBL_CENTRAL_COMMAND_fascism": "an asymmetric spiked command helm with a five-vent square jawguard, hinged cheek plates, narrow red brow slit, and three unequal crown spikes",
    "CBL_CENTRAL_COMMAND_neutrality": "a notched jaw staff and hooked command rod crossed through a toothed crown buckle, with two short binding tabs, offset rivets, and chipped finials",
    "CBL_HOST_CONFEDERATION": "three overlapping shields of different silhouettes bearing jaw, claw, and butcher-hook cutouts, joined by riveted tabs around a compact central jaw without chains",
    "CBL_HOST_CONFEDERATION_communism": "three asymmetric host pennon-plates arranged around a gold tooth pin, each plate shaped by a jaw notch, pierced fastening hole, and a different cleaver-like edge",
    "CBL_HOST_CONFEDERATION_democratic": "five nonmatching host cauldrons with toothed rims and interlocking handles around a scarred gold shield, each bowl carrying a different notch and rivet pattern",
    "CBL_HOST_CONFEDERATION_fascism": "three outward-facing tusked beast heads with distinct boar, hound, and carrion-bird profiles fused through one central jaw plate, with separate scars and bolts",
    "CBL_HOST_CONFEDERATION_neutrality": "a hook knife, broad cleaver, and narrow carving blade interlocked through a triangular jaw plate, with different bone grips, chipped edges, and offset rivets",
    "CBL_RITUAL_STATE": "a chalice built from a lower jaw, with four square tooth finials, riveted stem, black drop cutout, two blade-like side fins, and a chipped pedestal",
    "CBL_RITUAL_STATE_communism": "two unlike ceremonial blades bound to a hexagonal bone-ledger plate, with deep tally gashes, tooth-shaped corners, a square clasp, and visible binding pins",
    "CBL_RITUAL_STATE_democratic": "an overhead heraldic altar table as an irregular four-lobed slab, with four distinct jaw-seat projections, central dark bowl, tooth inlays, and riveted edge plates",
    "CBL_RITUAL_STATE_fascism": "an invented skeletal war helm with asymmetric brow, blade crest, empty eye slots, four uneven jaw teeth, riveted cheek hinges, and one broken temple plate",
    "CBL_RITUAL_STATE_neutrality": "a jaw-shaped brass brazier with three different blade-like flames, toothed rim, two hooked feet, riveted side plates, and a dark central ember void",
    "ZZZ_CANNIBALISM_HANNIBAL": "an austere serving cloche with a jawbone base, square tooth finial, unequal side latches, three narrow vent slits, scalloped platter edge, and dark hinge pins",
    "ZZZ_CANNIBALISM_HANNIBAL_communism": "an elegant boning knife and three-pronged fork locked into a jaw-shaped medallion, surrounded by mismatched pinned teeth rather than a generic wreath",
    "ZZZ_CANNIBALISM_HANNIBAL_democratic": "a fork transformed into a heraldic table scepter: crown-like unequal tines, jaw-shaped hand guards, pierced stem, scalloped shield boss, and silver fastening pins",
    "ZZZ_CANNIBALISM_HANNIBAL_fascism": "a tall predatory mouth shield with six unequal square teeth, red saw-edged gums, hinged cheek plates, a deep black palate, and a chipped upper rim",
    "ZZZ_CANNIBALISM_HANNIBAL_neutrality": "an ornate jaw-rimmed chalice with a stem assembled from stacked bone plates, clawed foot, small hooked side grips, tooth inlays, and a dark bowl void",
}


CBA_PROMPT = """Use case: logo-brand
Asset type: HOI4 fictional country flag source master for CBA.tga
Primary request: Create exactly one complete, original flat flag design for a fictional cannibal warlord host. This must visibly look authored by an image generator through a distinctive illustrative heraldic emblem, not a locally drawn geometric placeholder.
Flag layout: full-bleed rectangular flag in exact 82:52 proportion. Use an asymmetrical charcoal-black and dried-blood-red field divided by a broad bone-white diagonal scar.
Heraldic device: a single oversized scavenger jaw reliquary, centered slightly toward the hoist: an irregular lower jaw with five mismatched square teeth, chipped outer bone contours, two dark riveted cheek plates, a small red cord notch, and a hooked metal suspension loop. The emblem should have a strong outer silhouette yet retain several irregular illustrative internal cuts and hardware details.
Style/medium: clean flat vexillology, screen-printed heraldic illustration, 3 to 5 perfectly flat opaque colors, crisp hard edges, no gradients. The emblem must be original and materially more detailed than a generic jaw icon.
Composition/framing: render only the orthographic graphic design itself, edge to edge, no exterior margin and no presentation border. Make the emblem large enough to remain identifiable at 10x7.
Distinctness: do not use a circle badge, plain crossed tools, a single triangle, a basic stripe with one generic icon, or any real national or political emblem.
Cultural constraints: invented secular post-collapse heraldry only; no real-world extremist marks, no borrowed Indigenous sacred motifs, no claims about living traditions.
Avoid absolutely: words, letters, numbers, fake writing, watermark, signature, fabric, cloth, folds, ripples, waving, flagpole, rope, sky, room, landscape, people, lighting, shadows, gradients, texture, weathering, painterly surface, 3D, bevels, perspective, mockup, transparent background."""


def prompt_for(spec: dict[str, str]) -> str:
    stem = spec["stem"]
    if stem == "CBA":
        return CBA_PROMPT
    return f"""Use case: logo-brand
Asset type: HOI4 fictional country flag source master for {stem}.tga
Primary request: Create exactly one complete, original flat flag design for {spec['family_role']}. This must visibly look authored by the built-in image generator through a distinctive illustrative heraldic emblem, not a locally drawn geometric placeholder.
Flag architecture: {spec['design']}
Authored emblem construction: Render the principal device as {DETAILS[stem]}. Preserve its irregular illustrative cuts, layered construction, and identifying hardware rather than simplifying it into primitive geometry.
Style/medium: clean flat vexillology, screen-printed heraldic illustration, 3 to 5 perfectly flat opaque colors, crisp hard edges, no gradients. Keep a strong outer silhouette but retain several internal notches, plates, holes, bindings, or fasteners that prove an authored emblem.
Composition/framing: exact front-on rectangular flag in 82:52 proportion, filling the image edge to edge. Render only the orthographic graphic design itself, with no exterior margin or presentation border. Keep the principal device large enough to remain identifiable at 10x7.
Distinctness: materially different composition and symbol from every other variant in this identity family. Do not use a generic circle, plain crossed tools, a single triangle, a basic stripe with one generic icon, a palette swap, copied emblem, recolor, or flipped variant. Do not copy any real national flag or political-party emblem.
Cultural constraints: invented secular post-collapse heraldry only; no real-world extremist marks, no borrowed Indigenous sacred motifs, and no claims about living traditions.
Avoid absolutely: words, letters, numbers, fake writing, watermark, signature, fabric, cloth, folds, ripples, waving, flagpole, pole sleeve, rope, sky, room, landscape, people, lighting, shadows, gradients, texture, weathering, painterly surface, 3D, bevels, perspective, mockup, transparent background."""


def main() -> None:
    specs = json.loads(SPECS.read_text(encoding="utf-8-sig"))
    stems = [spec["stem"] for spec in specs]
    if len(stems) != 65 or set(stems) != set(DETAILS):
        raise RuntimeError("Regeneration detail map must match all 65 flag stems")
    for spec in specs:
        spec["imagegen_detail"] = DETAILS[spec["stem"]]
        spec["generation_revision"] = "built-in-imagegen-regeneration-2026-07-15"
        (PROMPTS / f"{spec['stem']}.txt").write_text(
            prompt_for(spec) + "\n", encoding="utf-8"
        )
    SPECS.write_text(json.dumps(specs, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"prompt_count": len(specs), "revision": specs[0]["generation_revision"]}))


if __name__ == "__main__":
    main()
