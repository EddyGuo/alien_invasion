# Environment Setting
- By PyCharm 2018.1.1 (Community Edition)  
- Anaconda3-5.1.0-Windows-x86_64
- Windows 7 6d #PC-181.4445.76, built on April 10, 2018

## Anaconda
Add Anaconda to PATH environment variable.

## Pycharm
### Project Interpreter
- File->Setting->Project: pythonlearning->Project Interpreter
- Add a new Virtulenv Evironment  
  Location: username\venv\pythonlearning  
  Base Interpreter: username\Anaconda3\python.exe
- Tick the following options:  
- [x] Inherit global site-packages  
- [x] make available to all projects

### Install Markdown Plugins
- File->Setting->Plugins->Install Jetbrains Plugings
- Search markdown and Install but I can't connect the server
- Click Http Proxy Setting and pick `Manual Proxy Configuration` as well as `SOCKS`
- I have configured the proxy host name using Shadowsocks, so I just make these settings here  
  Host name: 127.0.0.1  
  Host Port: 1080

### VCS(Version Control System)
- VCS->Git
- You can use the git and github here to add, commit, push your project