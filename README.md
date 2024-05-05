![Static Badge](https://img.shields.io/badge/Discord%20Bot-Type?label=Type&labelColor=282c2c&color=F0B132) ![Static Badge](https://img.shields.io/badge/discord.py-Framework?label=Framework&labelColor=282c2c&color=00A8FC) ![GitHub last commit](https://img.shields.io/github/last-commit/Annhilati/fragment?logo=github&label=Latest%20Development&labelColor=282c2c&color=248046) ![GitHub License](https://img.shields.io/github/license/Annhilati/fragment?label=License&labelColor=282c2c)
## Build (installing requirements)
```sh
sh build.sh
```

## Start
```sh
sh start.sh
```
or execute `main.py`

#### Hexadezimalfarbe in Farbinteger umwandeln
```py
def f(hex_color):
    if hex_color.startswith("#"):
        hex_color = hex_color[1:]
    return int(hex_color, 16)

print(f("#3BA561"))

```
