import os
import sys
import subprocess

def houdini_env(project_path, hou_main_path, hou_doc_path, render_path):
    e = os.environ
    pwd = os.path.dirname(os.path.abspath(__file__))
    
    hfs = hou_main_path
    e['HH'] = os.pathsep.join([os.path.join(hfs, 'houdini'), os.path.expanduser(hou_doc_path)])
    e['HOUDINI_PATH'] = ';'.join([os.path.join(pwd, 'houdini'), e['HH'], e.get('HOUDINI_PATH', '')])
    e['HOUDINI_TOOLBAR_PATH'] = ';'.join([e.get('HOUDINI_PATH', ''), e['HH'], os.path.join(pwd, 'houdini')])
    e['JOB'] = project_path + "\\02_work\\fx\\01_houdini"
    e['RENDER_PATH'] = render_path
    e['HOUDINI_MAXTHREADS'] = "-1"
    e['HOUDINI_USER_PREF_DIR'] =  ';'.join(os.path.join(pwd, 'houdini'))




 #e['HOUDINI_TOOLBAR_PATH'] = ';'.join([os.path.join(pwd, 'houdini'), e['HH'], e.get('HOUDINI_PATH', '')])
    




