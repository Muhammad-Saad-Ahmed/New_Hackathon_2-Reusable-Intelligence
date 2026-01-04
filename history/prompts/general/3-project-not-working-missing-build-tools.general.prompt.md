---
id: 3
title: "Project Not Working: Missing Build Tools"
stage: general
date: 2025-12-31
surface: agent
model: gemini-1.5-flash-latest
feature: none
branch: main
user: user
command: "this project is not working??"
labels: ["debugging", "backend", "dependencies", "build-tools"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests: []
---

## Prompt

this project is not working??

## Response snapshot

I couldn't start the backend because of an error when installing the required Python packages.

The installation of `pydantic-core` failed because it needs to be compiled from source, and the necessary C++ build tools (specifically `link.exe`) are not installed on your system.

**To fix this, you need to install the Microsoft C++ Build Tools.**

1.  Download the Visual Studio Build Tools installer from here: [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2.  Run the installer and select "C++ build tools" from the "Workloads" tab.
3.  Complete the installation.

After the installation is complete, please let me know, and I will try to install the dependencies and run the backend again.

## Outcome

- ✅ Impact: Identified the root cause of the project not working and provided a solution.
- 🧪 Tests: N/A
- 📁 Files: 0 files changed.
- 🔁 Next prompts: Awaiting user to install build tools.
- 🧠 Reflection: Successfully diagnosed the issue and provided clear instructions to the user.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
