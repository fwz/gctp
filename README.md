## Guitar Chord Tab Parser
A naive script to transpose and roll chord tab in terminal

## Usage
```
Usage: tab_parser.py [options]

Options:
  -h, --help            show this help message and exit
  -t TUNE, --tone=TUNE  the tone you wanna switched to
  -d DELAY, --delay=DELAY
                        0 for instant, 3 for normal roll speed
  -f FILE_PATH, --file_path=FILE_PATH
                        chord file path


```

To transpose a chord to target chord, use the `-t` param.

For example, the following `C chord` tab:

```
C       Dm7
()看人潮来了 又(散)了
G/B      Cadd9
()看荧幕亮了 又(暗)了
Am       Em7
()一字一句 认真(消)遣了
F           G
沸腾(着)  沉默(了)
```

will be transpose to `F#` if we use `python tab_parser.py -t F#`

```
F#       G#m7
()看人潮来了 又(散)了
C#/F      F#add9
()看荧幕亮了 又(暗)了
D#m       A#m7
()一字一句 认真(消)遣了
B           C#
沸腾(着)  沉默(了)

