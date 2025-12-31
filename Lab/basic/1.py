# Basic Memory Management Simulator (Paging + Segmentation + Simple FS)
# Short version (~250 lines)

import tkinter as tk
from tkinter import ttk, simpledialog, messagebox


# ---------------- MEMORY -----------------

class Frame:
    def __init__(self, i):
        self.id = i
        self.free = True
        self.proc = None
        self.info = ""


class Memory:
    def __init__(self, n=32):
        self.frames = [Frame(i) for i in range(n)]

    def free_frames(self):
        return [f for f in self.frames if f.free]

    def allocate(self, count):
        free = self.free_frames()
        if len(free) < count:
            return None
        return free[:count]

    def clear_proc(self, pid):
        for f in self.frames:
            if f.proc == pid:
                f.free = True
                f.proc = None
                f.info = ""


# -------------- PAGING ------------------
class Paging:
    def __init__(self, mem, frame_kb=4):
        self.mem = mem
        self.frame_kb = frame_kb

    def load(self, pid, size):
        pages = (size + self.frame_kb - 1) // self.frame_kb
        frames = self.mem.allocate(pages)
        if not frames:
            return None
        table = {}
        for p, f in enumerate(frames):
            f.free = False
            f.proc = pid
            f.info = f"P{p}"
            table[p] = f.id
        return table


# -------------- SEGMENTATION --------------
class Segmentation:
    def __init__(self, mem):
        self.mem = mem

    def load(self, pid, segs):
        seg_map = {}
        for sid, size in enumerate(segs):
            need = (size + 3) // 4
            run = []
            for f in self.mem.frames:
                if f.free:
                    run.append(f)
                    if len(run) == need:
                        break
                else:
                    run = []
            if len(run) < need:
                return None
            for f in run:
                f.free = False
                f.proc = pid
                f.info = f"S{sid}"
            seg_map[sid] = [f.id for f in run]
        return seg_map


# ---------------- FILE SYSTEM ----------------
class Block:
    def __init__(self, i):
        self.id = i
        self.free = True
        self.file = ""


class FileSystem:
    def __init__(self, n=64):
        self.blocks = [Block(i) for i in range(n)]
        self.files = {}

    def create_contig(self, name, size):
        run = []
        for b in self.blocks:
            if b.free:
                run.append(b)
                if len(run) == size:
                    break
            else:
                run = []
        if len(run) < size:
            return False
        for b in run:
            b.free = False
            b.file = name
        self.files[name] = [b.id for b in run]
        return True

    def delete(self, name):
        if name not in self.files:
            return
        for i in self.files[name]:
            b = self.blocks[i]
            b.free = True
            b.file = ""
        del self.files[name]


# ------------------- GUI -------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Memory Manager")

        self.mem = Memory(32)
        self.page = Paging(self.mem)
        self.seg = Segmentation(self.mem)
        self.fs = FileSystem(64)

        self.processes = {}
        self.pid = 1

        self.make_ui()
        self.draw()

    def make_ui(self):
        f = ttk.Frame(self.root)
        f.pack(side="left", fill="y")

        ttk.Button(f, text="New Paging Proc", command=self.new_paging).pack(fill="x")
        ttk.Button(f, text="New Segment Proc", command=self.new_seg).pack(fill="x")
        ttk.Button(f, text="Terminate Proc", command=self.terminate).pack(fill="x")
        ttk.Separator(f).pack(fill="x", pady=5)
        ttk.Button(f, text="Create File", command=self.new_file).pack(fill="x")
        ttk.Button(f, text="Delete File", command=self.del_file).pack(fill="x")

        self.canvas = tk.Canvas(self.root, width=600, height=300, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.text = tk.Text(self.root, height=8)
        self.text.pack(fill="x")

    # ------ Process Ops -------
    def new_paging(self):
        size = simpledialog.askinteger("Size KB", "Enter size (KB):")
        if not size:
            return
        table = self.page.load(self.pid, size)
        if not table:
            messagebox.showwarning("Fail", "Not enough frames!")
            return
        self.processes[self.pid] = ("paging", table)
        self.pid += 1
        self.draw()

    def new_seg(self):
        n = simpledialog.askinteger("Segments", "Number of segments:")
        if not n:
            return
        segs = []
        for i in range(n):
            s = simpledialog.askinteger("Segment", f"Size of segment {i}:") or 1
            segs.append(s)
        m = self.seg.load(self.pid, segs)
        if not m:
            messagebox.showwarning("Fail", "Cannot allocate contiguous segments!")
            return
        self.processes[self.pid] = ("seg", m)
        self.pid += 1
        self.draw()

    def terminate(self):
        pid = simpledialog.askinteger("PID", "Enter PID:")
        if pid not in self.processes:
            return
        self.mem.clear_proc(pid)
        del self.processes[pid]
        self.draw()

    # ------- File Ops --------
    def new_file(self):
        name = simpledialog.askstring("File", "Name:")
        size = simpledialog.askinteger("Size", "Blocks:")
        if not self.fs.create_contig(name, size):
            messagebox.showwarning("Fail", "Not enough contiguous blocks!")
        self.draw()

    def del_file(self):
        name = simpledialog.askstring("Delete", "File name:")
        self.fs.delete(name)
        self.draw()

    # ------- Drawing ---------
    def draw(self):
        self.canvas.delete("all")
        w = 600
        h = 300
        cw = w // 32
        for f in self.mem.frames:
            x1 = f.id * cw
            y1 = 0
            x2 = x1 + cw
            y2 = 100
            color = "white" if f.free else "lightgreen"
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
            if not f.free:
                self.canvas.create_text(
                    x1 + 5,
                    y1 + 5,
                    anchor="nw",
                    text=f"P{f.proc}{f.info}",
                    font=("Arial", 8),
                )

        # disk
        bw = w // 64
        for b in self.fs.blocks:
            x1 = b.id * bw
            y1 = 150
            x2 = x1 + bw
            y2 = 250
            col = "white" if b.free else "lightblue"
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=col)

        self.show_info()

    def show_info(self):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, "Processes:")
        for pid, (typ, info) in self.processes.items():
            self.text.insert(tk.END, f"PID {pid} {typ}: {info}")
        self.text.insert(tk.END, "Files:")
        for name, blks in self.fs.files.items():
            self.text.insert(tk.END, f"{name}: {blks}")


# -------- Main ----------
root = tk.Tk()
App(root)
root.mainloop()
