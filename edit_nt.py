import read_nt as rn
import write_nt as wn
from datetime import datetime

# Редактирование заметки

def edit_note():
    notes = rn.read_notes()
    note_id = int(input('Введите id заметки:'))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input('Введите новый заголовок: ')
            note['body'] = input('Введите новый текст: ')
            note['update_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break
    else:
        print('Заметка не найдена')
    wn.write_notes(notes)