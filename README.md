DEPRECATED! This code is terrible and glitched, don't use it (planning to fork it). 

# **PySpikon** 

![](https://img.shields.io/badge/Code-Python-blue?logo=python)
![GitHub](https://img.shields.io/github/license/pyjonhact/pyspikon)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pyjonhact/pyspikon)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/pyjonhact/pyspikon?include_prereleases)
[![Mindstorms-Software-Toolkit](https://circleci.com/gh/Mindstorms-Software-Toolkit/pyspikon.svg?style=svg)]()

![PySpikon - Python to Spike converter command-line program and library](https://i.imgur.com/a3p47S7.png)

PySpikon (a.k.a PySpikeConverter) is a Python-based program that allows you to convert .llsp files into .py files, it uses the *"project.json"* contained into your .llsp to create a Python file directly from the command-line.


PySpikon é um programa baseado em Python que te permite converter arquivos .llsp em arquivos .py, ele usa o *"project.json"* contido em seu .llsp para criar um arquivo Python direto da linha de comando

# First version released: 0.6.1!

This version is stable, but its still not complete.

# Contents
1 [Setup](#setup)

&nbsp;&nbsp;&nbsp;&nbsp;1.1. [Installing](#installing)

&nbsp;&nbsp;&nbsp;&nbsp;1.2. [Using](#using)

2 [Characteristics](#characteristics)

&nbsp;&nbsp;&nbsp;&nbsp;2.1 [Supported Robots](#supported-robots)

&nbsp;&nbsp;&nbsp;&nbsp;2.2 [Features and Supported Blocks](#features-and-supported-blocks)

3 [Live Editor](#live-editor)

4 [Contributing and Crediting](#contributing-and-crediting)

# Setup

### Installing

You can download PySpikon M.I.A setup [here](https://pyjonhact.github.io/MindstormsSoftwareToolkit/downloads/).*

**OBS: To run it, you need Python 3.6+*

### Using
To use it, go to the folder where you installed PySpikon, then run:
```bash
cd pyspikon/pyspikon
python pyspikon.py path-to-file new-file-path [--live-editor]
```
The output will be named "output.py"

# Characteristics

### Supported Robots
- [ ] Lego® Mindstorms® NXT (9797)
- [ ] Lego® Mindstorms® EV3 (45544)
- [X] Lego® Education® Spike™ Prime (45678)
- [ ] Lego® Mindstorms® Robot Inventor (51515)

### Features and Supported Blocks
PySpikon supports almost all blocks from LEGO Education SPIKE, except for Events and MyBlocks.
| Blocks | Supported? |
| --- | --- |
| Individual Motors | Yes! |
| Motor Pairs | Yes! |
| Light Blocks | Yes! |
| Sound Blocks | Yes! |
| Events | No |
| Control | Yes! |
| Sensors | So-so |
| Operators | So-so |
| Variables | Yes! |
| MyBlocks | No |

PySpikon has features like Live Editor, i will explain better in next sections

# Live Editor
Live Editor is the real-time converter of PySpikon, each second your code output is updated, to use it type `--live-editor` in the end of your command.

![Demo of Live Editor](https://i.imgur.com/2Ssoaz6.gif)

# License
Here is GPL v3 (PySpikon's license) in a nutshell:
* You can copy and modify this program (fork).
* But you need to credit it.
* If you use it in a closed-source project, you need to change your license to GPL v3.
* If you break this rules you will lose the rights, except if you fix it.
