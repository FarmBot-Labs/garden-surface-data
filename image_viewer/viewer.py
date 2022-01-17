import open3d as o3d

# use `1` and `4` on keyboard to switch between color views while in viewer
# comment out filenames below as desired for comparison

filenames = [
    'tof.xyzrgb', # (blue) time of flight sensor values
    'v2.xyzrgb',  # (red) v2 dataset z coordinates
    'msh.xyzrgb', # (green) Measure Soil Height chosen surface heights
]

vis = o3d.visualization.Visualizer()
vis.create_window()

for filename in filenames:
    pcd = o3d.io.read_point_cloud(filename)
    vis.add_geometry(pcd)

opt = vis.get_render_option()
opt.background_color = [0, 0, 0]

vis.run()

