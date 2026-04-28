<p align="center">
  <img src="logo/hilisforeveryone.png" alt="HIL is for Everyone" width="400">
</p>

# HIL is for Everyone

**Companion repository for the NI Connect 2026 session of the same name.**

A starter kit for engineers, test leads, and managers who want to begin a
Hardware-in-the-Loop (HIL) journey for embedded testing — whether you're
spinning up your first rack or making the case to leadership for one.

This repo is meant to be your Monday-morning starting point: the slides we
showed, the spreadsheets we used to justify the investment, real working
code you can adapt, and an AI assistant that helps you map DUT signals to
HIL rack wiring.

---

## About the session

**Hardware in the Loop is for Everyone**
NI Connect 2026 — May 14, 2026 — Fort Worth, TX

**Presenters**
- Chase Fearing — Sub-Zero Group, Inc.
- Steve Zastrow — Sub-Zero Group, Inc.
- Tanner Blair — Aliaro
- Ben Robinson — NI

---

## What's in this repo

| Section | What you'll find |
| --- | --- |
| [`presentation/`](presentation/) | The slide deck (PDF) and a link to the session recording. |
| [`business-case/`](business-case/) | NPV calculator, ROI framework, value-proposition template, and supporting materials to help you build an internal case for HIL investment. |
| [`code-samples/`](code-samples/) | A Python `pytest` example that automates VeriStand test execution, plus a VeriStand custom-steps example for NI TestStand. |
| [`hil-wiring-assistant/`](hil-wiring-assistant/) | An AI agent that helps you map DUT signals to HIL rack wiring. |

---

## Who this is for

- **Engineers** evaluating whether HIL is right for your product line.
- **Test leads** ready to automate but unsure where to start.
- **Managers** who need numbers — payback period, ROI, headcount impact —
  before approving a capital request.
- **Anyone** who has heard "HIL" thrown around and wants a concrete,
  approachable on-ramp.

You do not need to own a HIL rack to get value here. The business-case
materials and the wiring assistant work just as well during planning as
they do during execution.

---

## How to use this repo

1. **Watch or re-read the session.** Start in [`presentation/`](presentation/).
2. **Make the case.** Take the spreadsheets in [`business-case/`](business-case/),
   plug in your numbers, and bring them to your next budget conversation.
3. **Try the code.** The samples in [`code-samples/`](code-samples/) are
   meant to be copied, adapted, and run.
4. **Plan your wiring.** Point the [`hil-wiring-assistant/`](hil-wiring-assistant/)
   at your DUT signal list and let it propose a rack-side mapping.

---

## License

This project is released under the [MIT License](LICENSE). Use it, fork it,
adapt it for your team — that's the point.

---

## Questions or feedback

Open an issue on this repo, or find one of the presenters at NI Connect.
