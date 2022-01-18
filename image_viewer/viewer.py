#!/usr/bin/env python3

'''
3D point cloud viewer

see README.md for usage
'''

import open3d as o3d

# comment out filenames below as desired for comparison
filenames = [
    'tof.xyzrgb',
    'v2.xyzrgb',
    'msh.xyzrgb',
]

vis = o3d.visualization.VisualizerWithKeyCallback()
vis.create_window()

def set_view(key):
    'Change to top or front view.'
    def _view(vis):
        ctr = vis.get_view_control()
        front = {'front': [0, -1, 0], 'side': [1, 0, 0], 'top': [0, 0, 1]}
        up = [0, 1, 0] if key == 'top' else [0, 0, 1]
        ctr.set_front(front[key])
        ctr.set_up(up)
    return _view

key_callbacks = {
    ord('F'): set_view('front'),
    ord('G'): set_view('side'),
    ord('U'): set_view('top'),
}

for key, callback in key_callbacks.items():
    vis.register_key_callback(key, callback)

for filename in filenames:
    pcd = o3d.io.read_point_cloud(filename)
    vis.add_geometry(pcd)

opt = vis.get_render_option()
opt.background_color = [0, 0, 0]

vis.run()

