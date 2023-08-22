@echo off
set LASTEST="#7266"
cd "./%LASTEST%"
setlocal enabledelayedexpansion

for %%f in (*.*) do (
    set "filename=%%~nf"
    set "extension=%%~xf"
    
    if "!filename!"=="basic" (
        if "!extension!"==".py" (
            echo Running basic.py using Python
            echo:
            python basic.py
        ) else if "!extension!"==".rs" (
            echo Compiling and running basic.rs using Rust
            rustc basic.rs
            echo:
            basic.exe
        ) 
    )
)

endlocal
