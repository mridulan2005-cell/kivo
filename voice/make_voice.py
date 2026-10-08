"""Generate Kivo's voice clips (natural Indian female neural voices) from voice/lines.js.

    pip install edge-tts
    python voice/make_voice.py            # only missing clips
    python voice/make_voice.py --all      # regenerate everything
"""
import asyncio, json, pathlib, sys
import edge_tts

HERE = pathlib.Path(__file__).parent
VOICES = {"hi": "hi-IN-SwaraNeural", "mr": "mr-IN-AarohiNeural"}
PITCH, RATE = "-2Hz", "-4%"    # near-natural pitch, a touch slower = warm, calm delivery

async def main(force):
    src = (HERE / "lines.js").read_text(encoding="utf-8")
    lines = json.loads(src[src.index("{"): src.rindex("}") + 1])
    for e in lines.values():
        out = HERE / f"{e['id']}.mp3"
        if out.exists() and not force:
            continue
        await edge_tts.Communicate(e["text"], VOICES[e["lang"]], rate=RATE, pitch=PITCH).save(str(out))
        print("made", out.name)

asyncio.run(main("--all" in sys.argv))
