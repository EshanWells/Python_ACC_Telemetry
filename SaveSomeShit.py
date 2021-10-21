import mmap
import csv

shMemDumpPhysics = mmap.mmap(-1, 712, u"Local\\acpmf_physics")
shMemDumpGraphic = mmap.mmap(-1, 1320, u"Local\\acpmf_graphics")
shMemDumpStatic = mmap.mmap(-1, 700, u"Local\\acpmf_static")

def saveSomeShit():
    fields = ["Some Shit"]
    file = open("SavedShit.csv", "w+", newline = "")
    with file:
        write = csv.writer(file)
        write.writerows(shMemDumpPhysics)
        write.writerows(shMemDumpGraphic)
        write.writerows(shMemDumpStatic)

saveSomeShit()
        