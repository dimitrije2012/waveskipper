# Wave Skipper Prototype 🎮🌊

This is a small game prototype I built in Python using the [Ursina](https://www.ursinaengine.org/) engine.  
The goal was to create a wave-skipping mechanic where the player jumps over a rising wave to survive. The game is playable (barely), but it's very much a rough early prototype.

---

## 🧠 About This Project

I started this project when I was 13 as a way to learn more about game development using Python and Ursina. It’s built entirely from scratch, in a single `.py` file, using only VS Code — no Unity or external tools.

- There's no fancy art or models — the wave is just a colored cube, and the sky and textures are Ursina defaults.
- Originally, I had an issue where the wave would rise too fast for the player to jump over. I fixed that, but now the jump is a bit *too* strong. So the game is very easy, but technically playable now.
- I don't plan to finish this game, but I’m uploading it to share what I learned and show a snapshot of where I’m at right now as a developer.

---

## 🛠 Tech Stack

- **Language:** Python 3.13
- **Engine:** Ursina
- **Editor:** Visual Studio Code
- **Assets:** None — just default textures, default skybox, and simple geometry

---

## 🤖 ChatGPT Assistance

Around 15-20-ish % of the code was written with help from ChatGPT — mostly to experiment with ideas, troubleshoot physics, and get around Ursina quirks I didn’t fully understand yet.  
I made sure to read through and tweak everything so I actually understood how it works, and it helped me learn a lot in the process.

---

## 🎯 Why Upload This?

Even though this isn’t a finished or polished game, I’m sharing it because:
- It was my first time using a game engine
- I learned how to prototype mechanics, work with 3D objects, and manage basic gameplay logic
- I want to document my learning as I go — not just the final results

---

## 🚧 Known Issues

- Jump height is a bit too high, making the game too easy
- The wave still rises indefinitely with no real difficulty scaling
- No menus, no restart, no scoring — just raw prototype logic

---

## 📸 Screenshots

![Wave Skipper Screenshot](image.png)
![Wave Skipper Screenshot](image1.png)

---

## 🗂 File Structure

game.py  # the main and only game file
README.md        # you're reading it
