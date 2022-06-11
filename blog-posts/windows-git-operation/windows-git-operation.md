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

The default background color of Windows Terminal is black, making it difficult to tell which terminal is which when you install some WSL distribution or PowerShell. You change the color of the terminal and the font of the text. ![image1](./assets/image1.png)  
I define my own color and font in the following way.

- color scheme:

  - One Half Dark

- font style:
  - Nerd Font

Nerd Font has a wide selection of development-oriented icons that are useful.  
https://www.nerdfonts.com/#home

### Installation Page

https://eng.fontke.com/font/24644369/

In my opinion, it is a little difficult to install the font in Windows by [official page](https://support.microsoft.com/en-us/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1). You can install the one to drag and drop by Windows personal settings page. ![](./assets/image3.png) ![image2](./assets/image2.png)

Set color scheme via GUI or describe it in JSON file.

```json
{
  "background": "#282C34",
  "black": "#282C34",
  "blue": "#61AFEF",
  "brightBlack": "#5A6374",
  "brightBlue": "#61AFEF",
  "brightCyan": "#56B6C2",
  "brightGreen": "#98C379",
  "brightPurple": "#C678DD",
  "brightRed": "#E06C75",
  "brightWhite": "#DCDFE4",
  "brightYellow": "#E5C07B",
  "cursorColor": "#FFFFFF",
  "cyan": "#56B6C2",
  "foreground": "#DCDFE4",
  "green": "#98C379",
  "name": "One Half Dark",
  "purple": "#C678DD",
  "red": "#E06C75",
  "selectionBackground": "#FFFFFF",
  "white": "#DCDFE4",
  "yellow": "#E5C07B"
}
```

Also, you generate it by this generator site.  
https://windowsterminalthemes.dev/

Copy color scheme setting and paste it to the `setting.json` file, making the terminal so nice. ![image4](./assets/image4.png)

## Git Customization

Next, I will customize the git operation. I think you make good use of the prompt display and tab completion functions to make the prompt easier to read when you use Git in the terminal. For example, you would describe `.bashrc` or `.zshrc` if you are using Mac.  
There are several useful tools in PowerShell to help your Git Operation, and I will introduce them.

### oh-my-posh

https://ohmyposh.dev/

Oh My Posh is a custom prompt engine for any shell(bash, zsh or PowerShell) that has the ability to adjust the prompt string with a function or variable.

```powershell
scoop install oh-my-posh
```

#### jandedobbeleer(My favorite theme)

![image5](./assets/image5.png)

After installing it, you describe `oh-my-posh` command loading the oh-my-posh theme at terminal startup in `$PROFILE`.

```powershell
# $PROFILE
oh-my-posh init pwsh --config ~/AppData/Local/Programs/oh-my-posh/themes/jandedobbeleer.omp.json | Invoke-Expression
```

There are various the oh-my-posh themes. You could find favorite theme.  
https://ohmyposh.dev/docs/themes

### posh-git

https://github.com/dahlbyk/posh-git#overview

posh-git is a PowerShell module that integrates Git and PowerShell by providing Git status summary information that can be displayed in the PowerShell prompt.

```powershell
scoop install posh-git
```
