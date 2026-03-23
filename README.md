![Version](https://img.shields.io/badge/version-v1.0-blue)
![License](https://img.shields.io/badge/license-BSL_1.1-orange)
![Layer](https://img.shields.io/badge/layer-Security-red)
# ÀṣẹVault

ÀṣẹVault is the cryptographic shrine of the Technosis ecosystem — securing sovereign identity, ritual keys, and agent credentials through BIP-39 entropy and Ed25519 signatures.

One-file shrine. 155 opcodes. Mint Àṣẹ on proof. Sabbath guards baked in.

Run: python ÀṣẹVault_COMPLETE.py
Add: add('SKILLS', 'twilio_call', 'Speak Àṣẹ mint on phone')
Save: save()

## Twilio Bridge (Voice)

Enable voice calls for minting events.

1.  **Install deps:** `pip install twilio python-dotenv`
2.  **Config:** Copy `.env.example` to `.env` and fill in Twilio creds.
3.  **Usage:** 
    - Bridge script: `twilio_bridge.py`
    - Swibe skill: `swibe/skills/twilio_call.swibe`

## Inbound (Future)
- Listen for calls
- Mint on "mint" voice command (requires webhook setup)

## The Cryptographic Shrine

ÀṣẹVault is the cryptographic shrine and source of truth for the Technosis ecosystem. It manages the core virtual machine state, handles opcode execution for non-critical tasks, and serves as a secure vault for digital assets and receipts.


---

## Part of the Technosis Sovereign Ecosystem

This component is a core piece of a larger architecture for creating and coordinating sovereign AI. For more information, see the [organism-core repository](https://github.com/Bino-Elgua/organism-core).

Àṣẹ.
