# hyper-resolution
Bash script using xrandr to create hyper resolution on your display

## How to use
Launch the script in your terminal with the wanted scale value as argument.
``` bash
./hypr.sh 1.25 # Set hyper resolution to 125% of your standard one. (e.g. 1366x768 --> 1708x960)
./hypr.sh 1   # Revert to standard display resolution
```

## Alias
The easiest way to use this script is to set an alias. Add the following line in your `.bash_aliases`
``` bash
alias hypr="/PATH/OF/THE/SCRIPT/hypr.sh"
```
