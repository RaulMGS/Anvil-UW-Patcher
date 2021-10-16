# Anvil UW Patcher
Anvil UW Patcher is a byte patcher tool that brings ultrawide support for cutscenes in Ubisoft's AnvilNext engine based Games. Currently tested for Assassin's Creed Odyssey and Assassin's Creed Valhalla.

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
- Assassin's Creed Odyssey - Ultrawide Cutscene Black Bars Removed.
- Assassin's Creed Valhalla - Ultrawide Cutscene Black Bars Removed.
- Supports both Uplay and Steam game binaries.

## Before and Afters

![img](https://i.imgur.com/wxE3zFe.jpeg)

![img](https://i.imgur.com/PqKjMz9.jpeg)

## Modifying and Packaging

**NOTE 1:** the project requires python 3.10 but it can probably run on older Python 3.x versions as well since it doesn't use any recently added Python API.

If anyone wants to modify and pack the script or just to pack the patcher.exe on their own, just clone the repository and do the desired changes. 

**NOTE 2:** pyinstaller is required for the packing process and can be installed by running ```pip install pyinstaller```

The build.ps1 script should be run on powershell to package the executable.

After packing the script, the standalone patcher.exe can be found in the dist folder of the project.
