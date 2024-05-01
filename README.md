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
