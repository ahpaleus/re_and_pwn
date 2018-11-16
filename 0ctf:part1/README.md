## 0ctf quals 2017: py

https://github.com/ctfs/write-ups-2017/tree/master/0ctf-quals-2017/reverse/py-137

Some notes from guessed opcodes (result from 'python dec.py test.py'):
```
99	| 64 <- LOAD_CONST ('!@#$%^&*')
01	| 01 <- POP_TOP	  '!@#$%^&*'
-00	| 00 <- STOP_CODE
68  | 7d <- STORE_FAST (key_a)
-01	| 01 <- POP_TOP	 	
-00	| 00 <- STOP_CODE
99	| 64 <- LOAD_CONST ('abcdefgh')
+02	| 02 <- ROT_TWO !!!!!!!!!!!!!!!?
00	| 00 <- STOP_CODE

68  | 7d <- STORE_FAST (key_b)
02
00	| 00 <- STOP_CODE

99	| 64 <- LOAD_CONST
03
00	| 00 <- STOP_CODE

68  | 7d <- STORE_FAST
03
00	| 00 <- STOP_CODE

61	| 7c <- LOAD_FAST
01	| key_a
00

99	| 64 <- LOAD_CONST
04  (4)
00

46 	| multiplication?
99	| 64 <- LOAD_CONST // '|', 'EOF'
05  ('|')
00

27	| 17 <- BINARY_ADD
61	| 7c <- LOAD_FAST // var
02	| key_b
00

61	| 7c <- LOAD_FAST // var
01	| key_a
00

27	| 17 <- BINARY_ADD
61	| 7c <- LOAD_FAST // var
03	| key_c
00

27	| 17 <- BINARY_ADD

99	| 64 <- LOAD_CONST // '|', 'EOF'
06  (2)
00
46  | multiplication?
27	| 17 <- BINARY_ADD
99	| 64 <- LOAD_CONST // '|', 'EOF'
05 	('|')
00
27 	| 17 <- BINARY_ADD
61 	| 7c <- LOAD_FAST // var
02 	(key_b)
00
99 	| 64 <- LOAD_CONST // '|', 'EOF'
06 	| (2)
00
46
27	| 17 <- BINARY_ADD
99	| 64 <- LOAD_CONST // '|', 'EOF'
07 	| ('EOF')
00
27 	| 17 <- BINARY_ADD
68  | 7d <- STORE_FAST 
04 	| save to 'secret' variable
00
9b
00
00
60
01
00
61 	| 7c <- LOAD_FAST
04
00
83
01
00
68  | 7d <- STORE_FAST
05
00
61 	| 7c <- LOAD_FAST
05
00
60
02
00
61 	| 7c <- LOAD_FAST
00
00
83
01
00
53
```


Solution:
```
# python solution.py
Decrypted:
flag{Gue55_opcode_G@@@me}
```