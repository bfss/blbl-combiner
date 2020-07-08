import os
import json
import subprocess

root = 'download'
if not os.path.exists('output'):
    os.makedirs('output')
    
all_downloaded_folders = os.listdir(root)
for df in all_downloaded_folders:
    fol_dir = root + os.sep + df
    all_bvs = os.listdir(fol_dir)
    for bv in all_bvs:
        bv_dir = fol_dir + os.sep + bv
        with open(os.path.join(bv_dir,'entry.json'), 'r', encoding='utf-8') as f:
            data = json.load(f)
        type_tag = data.get('type_tag')
        title = data.get('title') + '-' + bv
        video_dir = bv_dir + os.sep + type_tag
        src_audio = video_dir + os.sep + 'audio.m4s'
        src_video = video_dir + os.sep + 'video.m4s'
        dst = 'output' + os.sep + title + '.mp4'
        print(dst)
        ff = 'ffmpeg' + os.sep + 'ffmpeg.exe'
        cmd = ff + " -i " + src_audio + " -i " + src_video + " -c:v copy -strict experimental " + dst
        try:
            s = subprocess.check_output(cmd,shell=True)
        except:
            pass