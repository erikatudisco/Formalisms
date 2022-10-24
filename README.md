# Setup
Parts taken from https://nbis-reproducible-research.readthedocs.io/en/course_2104/setup/
 and https://coderefinery.github.io/installation/

## Shell and Git

### Setup for Mac / Linux users
- We will use terminal to some extent.
- Choose one of your choice, the built-in or another!

- Chances are that you already have git installed on your computer. You can check by running e.g. git --version. 
- If you don't have git, install it following the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). 
- If you have a very old version of git you might want to update to a later version.


### Setup for Windows users

There are several different ways to run the course material on a Windows
computer. Neither is perhaps optimal, and the material itself has not been
adapted specifically for Windows. Nevertheless, in principle everything
*should* be possible to run. A few ways you could setup:

- Install Git Windows: https://gitforwindows.org/ (**easiest if you want to start fast and plan to work in windows environment**)
  - See Windows part at https://coderefinery.github.io/installation/shell-and-git/#installation
- Run as Linux through a virtual machine (and see the Linux setup above)
- Use the Windows 10 PowerShell, install git 
  - https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-PowerShell
- Use the Linux Bash Shell (WSL) on Windows 10 (**perhaps best practice if you plan to run Linux as well**
  - instructions below 

#### Running in the Linux Bash Shell on Windows 10

This will give you access to a full command-line bash shell based on Linux on your
Windows 10 PC. For the difference between the Linux Bash Shell and the PowerShell on Windows
10, see *e.g.* [this article](
https://searchitoperations.techtarget.com/tip/On-Windows-PowerShell-vs-Bash-comparison-gets-interesting).

Install Bash on Windows 10 (WSL), following the instructions at *e.g.* **1** of these
resources:

- [Installing the Windows Subsystem and the Linux Bash](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
- [Installing and using Linux Bash on Windows](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)
- [Installing Linux Bash on Windows](https://itsfoss.com/install-bash-on-windows/)

### Configure git
Follow these instructions. https://nbis-reproducible-research.readthedocs.io/en/course_2104/setup/#installing-git

## Github
Sign up for GitHub account:
https://coderefinery.github.io/installation/github/

## Git/Github connection through ssh keys (This may take a while to get working, but is worth it)
https://coderefinery.github.io/installation/ssh/

- Test: `ssh -T git@github.com`
- If not working, these are the approximate steps to be done in your terminal. It can vary between systems, so link above is more certain.
```console
ssh-keygen -t ed25519 -C "email address"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
- [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)


## Miniconda3
- We encourage you to use miniconda3 for working with conda environment.
- Please follow the steps here: https://coderefinery.github.io/installation/conda/
- We will inform you during the lessons about Conda repos to use.

## PlantUML
- We will use the tool PlantUML to render UML code to graphical diagrams and flowcharts. 
- If you want PlantUML to render directly from a file on GitHub please install the extension PlantUML viewer to your web browser.
  - Firefox: PlantUML viewer
  - Chrome: Pegmatite
  - Microsoft Edge Markdown Diagrams
- When done you should see the code below as a diagram.

```plantuml
@startuml
!theme superhero
title:"USECASE Diagrams"
skinparam actorStyle awesome
Lecturer -d->(Present slides on UML)
Participant-d->(learn UML from SLIDES)
@enduml
```
