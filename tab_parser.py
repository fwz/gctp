# -*- encoding: utf8 -*-
import time
from optparse import OptionParser

match_tones = ["C#", "C", "D#", "D", "E", "F#", "F", "G#", "G", "A#", "A", "B"]
all_tones = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


class TabParser:

    def __init__(self):
        self.delay_counter = 0

    def play(self, lines, target_tone, delay):
        tone_line = True
        tone_diff = 0
        meta = {}

        for l in lines:
            l = l.strip()
            if l.startswith("--"):
                # meta line, read keys, title, singer, gene, etc.
                (k, v) = [w.strip() for w in l[2:].split(":")]
                meta[k] = v

                if k == "key":
                    tone_diff = (all_tones.index(target_tone) + 12 - all_tones.index(meta["key"])) % 12
                    print "origin key: " + v
                    if tone_diff != 0:
                        print "tuned key: " + transfer_key(v, tone_diff)

                else:
                    print": ".join([k, v])

            elif l.strip() == "":  # blank line
                print l
            else:
                res = ""
                if tone_line:

                    # find all tones
                    check_offset = 0
                    org_length = len(l)

                    while check_offset < org_length:

                        key_flag = False

                        for t in match_tones:
                            if l[check_offset:].startswith(t):
                                check_offset += len(t)
                                res += transfer_key(t, tone_diff)
                                key_flag = True
                                break

                        if not key_flag:
                            res += l[check_offset]  # remain unchanged
                            check_offset += 1

                content = res if tone_line else l
                self.print_with_delay(content=content, delay=delay)
                self.delay_counter += 1
                tone_line = not tone_line

    def print_with_delay(self, delay, content):
        """
        initial 20 line, do not delay
        :param delay:
        :param content:
        :return:
        """
        print content
        if self.delay_counter > 20:
            time.sleep(delay)


def transfer_key(tone, diff):
    i = all_tones.index(tone)
    return all_tones[(i+diff) % 12]

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-t", "--tone", dest="tune", help="the tone you wanna switched to", default="c")
    parser.add_option("-d", "--delay", dest="delay", help="0 for instant roll, 3 for normal roll speed", default="0")
    parser.add_option("-f", "--file_path", dest="file_path", help="chord file path", default="data/小人物-金玟岐.gctp")
    (options, args) = parser.parse_args()

    tp = TabParser()

    with open(options.file_path) as f:
        lines = "".join(f.readlines())
        tp.play(lines=lines.split("\n"), target_tone=options.tune.upper(), delay=float(options.delay))
