# Kivo — counter assistant prototype

Phygital, voice-first assistant for kirana stores (IIT Bombay design project). Wizard-of-Oz web prototype for testing and filming.

## Run

```bash
python -m http.server 8770
```

Open http://localhost:8770 (a wide window leaves room for the presenter controls).

## Presenter controls (outside the device)

- **Space** / big mic: someone says “Kivo…” (runs command 1)
- **1–6**: pick what Kivo heard (4 plants a 15→50 mishearing, Kivo asks before saving; 6 is Rohan's credit check). Commands said while Kivo is busy are queued
- **B**: background talk; Kivo hears but stays quiet
- **T** / tent button: customer at the counter. Kivo folds into tent mode: customer side (their credit, UPI QR, their own transactions) and owner side (current bill → khata or UPI) shown side by side, nothing spoken. Pick the customer in the wizard panel
- **L** replay, **N** next moment, **Esc** home, **H** hide controls
- Wizard panel: switch who is at the counter (Sandeep and Aai are owners; Rohan is the son: sees everything, and Kivo shows his work to the owner when they return). **Lipi** toggles on-screen text between Devanagari and Roman

## Voice

Clips in `voice/` are Indian female neural voices (Swara for Hindi, Aarohi for Marathi). Edit lines in `voice/lines.js`, then:

```bash
pip install edge-tts
python voice/make_voice.py --all
```
