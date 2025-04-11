# AERITH

*Aerith is my personal command console — a hacker-inspired, full-screen terminal interface designed to run and orchestrate all my personal microtools, services, and dev workflows.*

It’s not just a launcher. It’s a digital command center — built for flow, style, and control.

---

## 🎯 Vision

Aerith is the OS-like terminal I wish existed.

- 🟢 Retro hacker-glow UI (powered by [Textual](https://github.com/Textualize/textual))
- 💻 CLI-driven command routing (via [Typer](https://github.com/tiangolo/typer))
- 🧩 Modular tool system (local scripts or remote service hooks)
- 🧠 Reads from `version.json` for all build metadata — never hardcoded
- 🤖 Grows with me as I build more microservices, automations, and workflows

---

## 🚀 Getting Started

1. **Install dependencies**
   ```bash
   pip install textual typer
   ```

2. **Run Aerith**
    python aerith.py -start

3. **What you'll see**
    - boot sequence
    - A green-themed full-screen UI
    - A greeting prompt

## Project Structure

aerith/
├── aerith.py          # Entry point CLI
├── version.json       # App metadata
├── core/              # TUI engine, boot logic, runners
├── tools/             # Microtools (scripts or service starters)
├── config/            # Tool registry, themes, etc (future)
└── logs/              # Output logs (optional)

# Phased Roadmap

1. Bootable CLI + Basic Textual UI
2. Command routing, prompt interaction
3. Microtool execution (local only)
4. Tool Registry System
5. Remote Project Control
6. Theming, animation, personal touches

## Disclaimer
This project is personal. Built for flow, not for the world. But you're welcome to form, follow, remix or send me feedback.

## Author
Built with obsession for coding
by Mark Beltran