# Anvil UW Patcher
Anvil UW Patcher is a byte patcher tool that brings ultrawide support for cutscenes in Ubisoft's AnvilNext engine based Games.

## Usage

First download the latest release Patcher.exe from the [Releases Page](https://github.com/RaulMGS/Anvil-UW-Patcher/releases)

In order to patch a game executable, open your terminal of choice (cmd, powershell etc.) at the location of the patcher, then run the patcher as a command:

```patcher.exe "path/to/your/game.exe" aspect_ratio```

Available aspect ratios are 21:9 and 32:9

**Examples:**

```patcher.exe "E:/Steam/steamapps/common/Assassins Creed Odyssey/ACOdyssey.exe" 21:9```
will patch the game to run cutscenes in 21:9 aspect

```patcher.exe "E:/Steam/steamapps/common/Assassins Creed Odyssey/ACOdyssey.exe" 32:9```
will patch the game to run cutscenes in 32:9 aspect

**Reverting:**

The patcher always backs up the original exe file as "game.exe.bak" . 

In order to revert the executable to its original state just navigate to your game folder, delete the existing game.exe file and rename the game.exe.bak file back to game.exe.

**Updating the game:**

Most of the times, the game has to be patched again after an update.

## Game Support
- Supports both Uplay and Steam game binaries.
- The script has only been tested with Assassin's Creed Odyssey.

## Before and Afters

![img](https://i.imgur.com/wxE3zFe.jpeg)

![img](https://i.imgur.com/PqKjMz9.jpeg)
