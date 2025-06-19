import threading
import time

class Keyframe:
    def __init__(self, frame, transforms):
        self.frame = frame
        self.transforms = transforms  # {node_id: matrix}

class AnimationClip:
    def __init__(self, name):
        self.name = name
        self.keyframes = []

    def add_keyframe(self, frame, transforms):
        self.keyframes.append(Keyframe(frame, transforms))

    def interpolate(self, frame):
        # Linear between nearest keyframes for each node_id
        if not self.keyframes:
            return {}
        kfs = sorted(self.keyframes, key=lambda k: k.frame)
        prev_kf, next_kf = kfs[0], kfs[-1]
        for i in range(len(kfs) - 1):
            if kfs[i].frame <= frame <= kfs[i + 1].frame:
                prev_kf, next_kf = kfs[i], kfs[i + 1]
                break
        t = (frame - prev_kf.frame) / float(next_kf.frame - prev_kf.frame) if next_kf.frame != prev_kf.frame else 0
        interp = {}
        for nid in prev_kf.transforms:
            m0 = prev_kf.transforms[nid]
            m1 = next_kf.transforms.get(nid, m0)
            interp[nid] = [[m0[r][c] * (1-t) + m1[r][c] * t for c in range(4)] for r in range(4)]
        return interp

class AnimationEngine:
    def __init__(self, scene, frame_rate=24):
        self.scene = scene
        self.clips = {}
        self.current_clip = None
        self.playing = False
        self.frame = 0
        self.frame_rate = frame_rate
        self.thread = None

    def add_clip(self, name, clip):
        self.clips[name] = clip

    def play(self, name):
        self.current_clip = self.clips[name]
        self.frame = 0
        self.playing = True
        if not self.thread or not self.thread.is_alive():
            self.thread = threading.Thread(target=self._run)
            self.thread.start()

    def stop(self):
        self.playing = False

    def _run(self):
        while self.playing:
            if self.current_clip:
                transforms = self.current_clip.interpolate(self.frame)
                self.scene.apply_transforms(transforms)
                self.scene.render()
                self.frame += 1
            time.sleep(1.0 / self.frame_rate)