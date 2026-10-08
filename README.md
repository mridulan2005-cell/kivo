# Kivo — counter assistant prototype

Phygital, voice-first assistant for kirana stores (IIT Bombay design project). Wizard-of-Oz web prototype for testing and filming.

## Run

```bash
python -m http.server 8770
```

Open http://localhost:8770 (a wide window leaves room for the presenter controls).

## Presenter controls (outside the device)

- **Space** / big mic: someone says “Kivo…” (runs command 1)
- **1–5**: pick what Kivo heard (4 plants a 15→50 mishearing)
- **B**: background talk; Kivo hears but stays quiet
- **L** replay, **N** next moment, **Esc** home, **H** hide controls
- Wizard panel: switch who is at the counter (Sandeep / Aai / Ravi-helper)

## Voice

Clips in `voice/` are Indian female neural voices (Swara for Hindi, Aarohi for Marathi). Edit lines in `voice/lines.js`, then:

```bash
pip install edge-tts
python voice/make_voice.py --all
```
