# **PySpikon** 
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

Download [Git](https://git-scm.com/downloads), then run this in cmd/shell:
```
git clone https://github.com/pyjonhact/pyspikon.git
```
Now you are able to run PySpikon on Linux

### Using
To use it, run:
```bash
cd pyspikon
python pyspikon.py path-to-file new-file-path
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
Live Editor, is the real-time converter of PySpikon, each second your code output is updated, to use it type `--live-editor` in the end of your command.

![Demo of Live Editor](https://i.imgur.com/2Ssoaz6.gif)

# Contributing and Crediting
Please credit this repo if you create a modified version and publishED it. If you find any bug report in Issues, if you have a suggestion, post it in Disscussion. 
