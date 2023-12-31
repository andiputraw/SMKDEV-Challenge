@echo off
set LASTEST="#10829"
cd "./%LASTEST%"
setlocal enabledelayedexpansion

for %%f in (*.*) do (
    set "filename=%%~nf"
    set "extension=%%~xf"
    
    if "!filename!"=="advanced" (
        if "!extension!"==".py" (
            echo Running advanced.py using Python
            echo:
            python advanced.py
        ) else if "!extension!"==".rs" (
            echo Compiling and running advanced.rs using Rust
            echo:
            rustc advanced.rs
            advanced.exe
        ) else if "!extension!"==".go" (
            echo Compiling and running advanced.go using Golang
            echo:
            go run advanced.go
        ) else if "!extension!"==".js" (
            echo Running advanced.js using nodejs
            echo:
            node advanced.js
        ) 
    )
)

endlocal
