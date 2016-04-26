"""Amity Model

Usage:
  amity.py create_room (<room_names> <room_types>)...
  amity.py add_person <first_name> <last_name> <STAFF/FELLOW> [<wants_accommodation>]
  amity.py reallocate_person <person_identifier> <new_room_name>
  amity.py load_people <filename>
  amity.py print_allocations [-o=filename]
  amity.py print_unallocated [-o=filename]
  amity.py print_room <room_name>
  amity.py save_state [--db=sqlite_database]
  amity.py load_state <sqlite_database>
  amity.py clear_room <room_name>
  amity.py remove_room <room_name>  
  amity.py reset
  amity.py -h | --help

Examples:
  amity.py create_room Moon office
  amity.py create_room Cedar living
  amity.py add_person HASSAN OYEBOADE FELLOW N
  amity.py add_person SUNDAY NWUGURU FELLOW Y
  amity.py add_person PROSPER OTEMUYIWA STAFF
  amity.py reallocate_person F3WEDS32WED obeche
  amity.py load_people input.txt
  amity.py print_allocations [-o=allocations.txt]
  amity.py print_unallocated [-o=unallocated.txt]
  amity.py save_state [--db=mydatabase.db]
  amity.py load_state <sqlite_database>
  amity.py clear_room cedar
  amity.py remove_room orion
  amity.py reset



Options:
    -h, --help  Show this screen and exit.
"""
from model.docopt import docopt
from model.amity_model import Amity

if __name__ == '__main__':
  arguments = docopt(__doc__)
  if arguments['create_room']:
    room_names = arguments['<room_names>']
    room_types = arguments['<room_types>']
    for room_name, room_type in zip(room_names,room_types):
      Amity().create_room(room_name,room_type)

  elif arguments['add_person']:
    Amity().add_person(arguments['<first_name>'], arguments['<last_name>'], arguments['<STAFF/FELLOW>'], arguments['<wants_accommodation>'])
  elif arguments['print_allocations']:
    Amity().print_allocations()
  elif arguments['print_unallocated']:
    Amity().print_unallocated()
  elif arguments['print_room']:
    Amity().print_room(arguments['<room_name>'])
  elif arguments['clear_room']:
    Amity().clear_room(arguments['<room_name>'])
  elif arguments['reallocate_person']:
    Amity().reallocate_person(arguments['<person_identifier>'], arguments['<new_room_name>'])
  elif arguments['remove_room']:
    Amity().remove_room(arguments['<room_name>'])
  elif arguments['load_people']:
    Amity().load_people(arguments['<filename>'])
  elif arguments['reset']:
    Amity().reset()
  