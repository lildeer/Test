import read_nt as rn
import add_nt as an
import edit_nt as en
import delete_nt as dn
import read_filt as rnf


def start():
    while True:
        print('Выбрать опцию:')
        print('1.Посмотреть список заметок')
        print('2.Добавить новую заметку')
        print('3.Редактировать заметку')
        print('4.Удалить заметку')
        print('5.Отфильтровать заметки')
        print('0.Выход')
        choice = input()
        if choice == '1':
            notes = rn.read_notes()
            for note in notes:
                print(f'{note["id"]}.{note["title"]}({note["created_at"]})')
                print(note['body'])
        elif choice == '2':
            an.add_note()
        elif choice == '3':
            en.edit_note()
        elif choice == '4':
            dn.delete_note()
        elif choice == '5':
            notes = rnf.read_notes_filter()
            for note in notes:
                print(f'{note["id"]}. {note["title"]} ({note["created_at"]})')
                print(note['body'])
        elif choice == '0':
            break
        else:
            print('Попробуйте еще раз')