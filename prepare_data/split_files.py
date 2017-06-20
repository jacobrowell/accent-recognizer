import subprocess
import os
import glob


dirs = [
    '/home/eugen/student/diploma/code/c20/audioFiles/task80',
    # '/home/eugen/student/diploma/code/c20/audioFiles/task81',
    # '/home/eugen/student/diploma/code/c20/audioFiles/task82',
]
#
for d in dirs:
    for speaker in os.listdir(d):
        wav_names = glob.glob('{}/{}/*.wav'.format(d, speaker))

        for name in wav_names:
            duration = subprocess.check_output(
                'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0" -sexagesimal'.format(name),
                shell=True).strip()
            minutes = int(duration.split(':')[1])

            for i in range(0, minutes):
                start = '00{}'.format(i)[-2:]
                duration = '01'
                infile = name
                outfile = '{}/{}/part_{}.wav'.format(d, speaker, i)
                subprocess.call(
                    'ffmpeg -y -ss 00:{}:00 -t 00:{}:00 -v quiet -i {} {}'.format(start, duration, infile, outfile),
                    shell=True)
                # somehow this command trims file, dropping it
                # subprocess.call('ffmpeg -y -i {} -ac 1 {} -v quiet'.format(outfile, outfile), shell=True)
