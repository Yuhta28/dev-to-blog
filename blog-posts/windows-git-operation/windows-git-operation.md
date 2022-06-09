---
title: Customize Windows Terminal and Git operations
published: false
description: Make Windows Terminal useful by terminal design and git operations
tags: windows, git, terminal
---

## Introduction

Windows Terminal is a powerful tool for managing your development environment. The settings as they are are sufficient, but you can customize your own settings for more convenient operation.  
So, I will introduce my terminal settings.

## Requirements

In advance, you need to install the following software:

- PowerShell 7.x
- Git for Windows
- WSL2
- Scoop

If you don't have these software, you can install them by following the link below.

### PowerShell 7.x

https://github.com/PowerShell/PowerShell/releases/download/v7.2.4/PowerShell-7.2.4-win-x64.msi

### Git for Windows

https://github.com/git-for-windows/git/releases/download/v2.36.1.windows.1/Git-2.36.1-64-bit.exe

### WSL2

https://docs.microsoft.com/en-us/windows/wsl/install

### Scoop

https://scoop.sh/

## Windows Terminal Settings

The default background color of Windows Terminal is black, making it difficult to tell which terminal is which when you install some WSL distribution or PowerShell. You change the color of the terminal and the font of the text. ![](./assets/image1.png)  
I define my own color and font in the following way.

- color scheme:

  - One Half Dark

- font style:
  - Nerd Font

Nerd Font has a wide selection of development-oriented icons that are useful.  
https://www.nerdfonts.com/#home

### Installation Page

https://eng.fontke.com/font/24644369/
