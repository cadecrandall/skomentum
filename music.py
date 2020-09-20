import urllib.request
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import ffmpeg

# Creates an empty AudioSegment
result = AudioSegment.silent(duration=0)

# # boost volume by 6dB
# beginning = first_10_seconds + 6
#
# # reduce volume by 3dB
# end = last_5_seconds - 3
# range is 21.0 to 26.7

# Loop over 1-13 because this is the range that sounds pleasing to hear
brightness = 18
for n in range(4, 8):
    brightness = brightness + n
    # Generate a sine tone with frequency 200 * n
    gen = Sine(200 * n)
    # AudioSegment with duration 200ms, gain -3
    sine = gen.to_audio_segment(duration=200).apply_gain(-3)
    # Fade in / out
    sine = sine.fade_in(50).fade_out(100)
    # Changes the volume based on the brightness of the star

    if 21 <= brightness < 22:
        sine = sine
    if (22 <= brightness < 23):
        sine = sine + 10
    if 23 <= brightness < 24:
        sine = sine + 20
    if 24 <= brightness < 25:
        sine = sine + 30
    if 25 <= brightness < 26:
        sine = sine + 40
    if 26 <= brightness < 27:
        sine = sine + 50

    # Append the sine to our result
    result += sine
# Play the result
play(result)
# save the result as an mp3 file
result.export("test.mp3", format="mp3")
