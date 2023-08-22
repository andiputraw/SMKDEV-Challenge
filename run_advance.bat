@echo off
set LASTEST="#7266"
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
        ) 
    )
)

endlocal
