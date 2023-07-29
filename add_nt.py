import read_nt as rn
import write_nt as wn
from datetime import datetime

# добавление новых заметок 

def add_note():
    notes = rn.read_notes()
    max_id = max([note['id'] for note in notes]) if notes else 0
    new_note = {
        'id': max_id +1,
            'title':input('Введите заголовок: '),
            'body': input('Введите текст: '),
            'created_at':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'update_at':''
    }
    notes.append(new_note)
    wn.write_notes(notes)