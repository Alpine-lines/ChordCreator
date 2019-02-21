notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def major(root):
    index = notes.index(root)
    return f'{root} {notes[(index+4) % 12]} {notes[(index+7) % 12]} - {root}  {notes[(index+7) % 12]} {notes[(index+4) % 12]}'


def minor(root):
    index = notes.index(root)
    return f'{root} {notes[(index+3) % 12]} {notes[(index+3) % 12]} - {root}  {notes[(index+7) % 12]} {notes[(index+3) % 12]}'


def inversions(root):
    major_notes = major(root).split(' ')[:3]
    minor_notes = minor(root).split(' ')[:3]
    return [
        f'{major_notes[1]} {major_notes[2]} {major_notes[0]}',
        f'{major_notes[1]} {major_notes[0]} {major_notes[2]}',
        f'{major_notes[2]} {major_notes[0]} {major_notes[1]}',
        f'{major_notes[2]} {major_notes[1]} {major_notes[0]}',
        f'{minor_notes[1]} {minor_notes[2]} {minor_notes[0]}',
        f'{minor_notes[1]} {minor_notes[0]} {minor_notes[2]}',
        f'{minor_notes[2]} {minor_notes[0]} {minor_notes[1]}',
        f'{minor_notes[2]} {minor_notes[1]} {minor_notes[0]}'
    ]
