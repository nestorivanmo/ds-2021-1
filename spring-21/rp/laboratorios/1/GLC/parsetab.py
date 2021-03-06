
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ONE ZEROstatement : ZERO statement ONEstatement : ZERO ONE'
    
_lr_action_items = {'ZERO':([0,2,],[2,2,]),'$end':([1,4,5,],[0,-2,-1,]),'ONE':([2,3,4,5,],[4,5,-2,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,2,],[1,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ZERO statement ONE','statement',3,'p_statement_assign','ejemplo1.py',30),
  ('statement -> ZERO ONE','statement',2,'p_statement_assign2','ejemplo1.py',33),
]
