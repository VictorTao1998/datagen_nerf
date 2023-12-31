import copy
import os
import os.path as osp

import yaml

target_dir = "/home/rayu/Nautilus/yamls/active_zero2/rendering/"
old_yaml_path = "/home/rayu/Nautilus/yamls/active_zero2/rendering/job-render-obj-fixangle-fixpattern-01.yaml"
old_yaml = yaml.safe_load(open(old_yaml_path, "r"))

total = 10
for i in range(1, total + 1):
    new_yaml = copy.deepcopy(old_yaml)
    new_yaml["metadata"]["name"] = f"rayc-job-render-primitive-v2-{i:02d}"
    new_yaml["spec"]["template"]["spec"]["containers"][0]["args"] = [
        f"/root/miniconda3/bin/conda init && source /root/miniconda3/etc/profile.d/conda.sh && conda activate activezero2 && cd /rayc-fast/activezero2/ &&ulimit -c 0 &&python data_rendering/render_script.py --sub {i} --total {total} --primitives-v2 --target-root /messytable-slow/messy-table-dataset/primv2_rdang_fixpat"
    ]

    with open(osp.join(target_dir, f"job-render-primitivev2-{i:02d}.yaml"), "w") as fnewyaml:
        yaml.safe_dump(new_yaml, fnewyaml)
